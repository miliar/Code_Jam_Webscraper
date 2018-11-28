#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>

const int DEBUG = 0;

using namespace std;

static string s_inputFile = "B-large.in";

static void GetInputStrings(vector<string>* strings);
static void DebugPrintLines(vector<string>& strings);
static void PrintLines(vector<string>& strings);

static int GetInt(const string& s);

static char s_currentResult = 'a';

enum SINK_TO {
  SINK_NO = -1,
  SINK_NORTH = 0,
  SINK_WEST,
  SINK_EAST,
  SINK_SOUTH
};

struct Place {
  int m_place;
  int m_north;
  int m_west;
  int m_east;
  int m_south;

  SINK_TO m_sinkTo;
  bool m_isSolved;
  char m_result;
};

struct Test {
  int m_height;
  int m_width;
  Place m_digits[100][100];
};

struct Problem {
  int m_numTests;
  vector<Test> m_tests;
};

static void GetProblem(vector<string>& strings, Problem* problem);
static void GetTest(vector<string>& strings, vector<Test>& tests, int& nextTestLine);

int main() {
  // read input txt and get input strings
  vector<string> inputStrings;
  GetInputStrings(&inputStrings);

  // debug print input
  DebugPrintLines(inputStrings);

  // get problem
  Problem problem;
  GetProblem(inputStrings, &problem);

  return 0;
}

void GetInputStrings(vector<string>* strings) {
  ifstream inputStream(s_inputFile.c_str());

  // append string while input is not EOF
  while(!inputStream.eof()) {
    string inputString;
    getline(inputStream, inputString);
    strings->push_back(inputString);
  }
}

void PrintLines(vector<string>& strings) {
  vector<string>::iterator iter = strings.begin();
  while(strings.end() != iter) {
    cout << *iter << endl;
    iter++;
  }
}

void DebugPrintLines(vector<string>& strings) {
  if(DEBUG) {
    PrintLines(strings);
  }
}

int GetInt(const string& s) {
  return atoi(s.c_str());
}

void GetProblem(vector<string>& strings, Problem* problem) {
  // get test nums
  problem->m_numTests = GetInt(strings[0]);
  // get tests
  int nextTestLine = 1; // because input "test num" is 1line
  for(int i = 0; i < problem->m_numTests; i++) {
    s_currentResult = 'a';
    cout << "Case #" << i+1 << ":" << endl;
    GetTest(strings, problem->m_tests, nextTestLine);
    if(i+1 != problem->m_numTests) {
      cout << endl;
    }
  }
}

void SolveFirstTestLine(string& s, int& height, int& width, int& nextTestLine) {
  istringstream iss(s);
  iss >> height;
  iss >> width;
  nextTestLine++;
}

void GetNextSinkTo(SINK_TO sinkTo, const int h, const int w, int& hNext, int& wNext) {
  switch(sinkTo) {
    case SINK_NO:
      break;
    case SINK_NORTH:
      hNext--;
      break;
    case SINK_EAST:
      wNext++;
      break;
    case SINK_WEST:
      wNext--;
      break;
    case SINK_SOUTH:
      hNext++;
      break;
    default:
      cout << "error";
  }
}

void Solve(Test& test, const int h, const int w, const bool write, char& c) {
  if(test.m_digits[h][w].m_isSolved) {
    c = test.m_digits[h][w].m_result;
  } else {
    if(test.m_digits[h][w].m_sinkTo == SINK_NO) {
      if(!write) {
        s_currentResult++;
      }
      test.m_digits[h][w].m_result = s_currentResult;
      c = s_currentResult;
    } else {
      int hNext = h;
      int wNext = w;
      GetNextSinkTo(test.m_digits[h][w].m_sinkTo, h, w, hNext, wNext);
      Solve(test, hNext, wNext, write, test.m_digits[h][w].m_result);
      c = test.m_digits[h][w].m_result;
    }
    test.m_digits[h][w].m_isSolved = true;
  }
}

void SolveMainTestLine(vector<string>& strings, Test& test, int& nextTestLine) {
  for(int h = 0; h < test.m_height; h++) {
    istringstream iss(strings[nextTestLine]);
    for(int w = 0; w < test.m_width; w++) {
      iss >> test.m_digits[h][w].m_place;
    }
    nextTestLine++;
  }

  for(int h = 0; h < test.m_height; h++) {
    for(int w = 0; w < test.m_width; w++) {
      int lowest = 10001;
      test.m_digits[h][w].m_north = (0 == h) ? 10001 : test.m_digits[h-1][w].m_place;
      lowest = (lowest > test.m_digits[h][w].m_north) ? test.m_digits[h][w].m_north : lowest;
      
      test.m_digits[h][w].m_west  = (0 == w) ? 10001 : test.m_digits[h][w-1].m_place;
      lowest = (lowest > test.m_digits[h][w].m_west) ? test.m_digits[h][w].m_west : lowest;

      test.m_digits[h][w].m_east  = (test.m_width == w + 1) ? 10001 : test.m_digits[h][w+1].m_place;
      lowest = (lowest > test.m_digits[h][w].m_east) ? test.m_digits[h][w].m_east : lowest;

      test.m_digits[h][w].m_south = (test.m_height == h + 1) ? 10001 : test.m_digits[h+1][w].m_place;
      lowest = (lowest > test.m_digits[h][w].m_south) ? test.m_digits[h][w].m_south : lowest;

      if(lowest >= test.m_digits[h][w].m_place) {
        test.m_digits[h][w].m_sinkTo = SINK_NO;
      } else {
        if(lowest == test.m_digits[h][w].m_north) {
          test.m_digits[h][w].m_sinkTo = SINK_NORTH;
        } else if(lowest == test.m_digits[h][w].m_west) {
          test.m_digits[h][w].m_sinkTo = SINK_WEST;
        } else if(lowest == test.m_digits[h][w].m_east) {
          test.m_digits[h][w].m_sinkTo = SINK_EAST;
        } else {
          test.m_digits[h][w].m_sinkTo = SINK_SOUTH;
        }
      }

      test.m_digits[h][w].m_isSolved = false;      
    }
  }

  test.m_digits[0][0].m_result = 'a';
  test.m_digits[0][0].m_isSolved = true;

  for(int h = 0; h < test.m_height; h++) {
    for(int w = 0; w < test.m_width; w++) {
      int hNext = h;
      int wNext = w;
      GetNextSinkTo(test.m_digits[h][w].m_sinkTo, h, w, hNext, wNext);
      Solve(test, hNext, wNext, test.m_digits[h][w].m_isSolved, test.m_digits[h][w].m_result);

      cout << test.m_digits[h][w].m_result;
      if(w + 1 != test.m_width) {
        cout << " ";
      }
    }
    if(h + 1 != test.m_height) {
      cout << endl;
    }
  }  
}

void GetTest(vector<string>& strings, vector<Test>& tests, int& nextTestLine) {
  Test test;
  SolveFirstTestLine(strings[nextTestLine], test.m_height, test.m_width, nextTestLine);
  SolveMainTestLine(strings, test, nextTestLine);
  tests.push_back(test);
}
