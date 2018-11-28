#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>

const int DEBUG = 0;

using namespace std;

static string s_inputFile = "A-small.in";

static void GetInputStrings(vector<string>* strings);
static void DebugPrintLines(vector<string>& strings);
static void PrintLines(vector<string>& strings);

//static int GetInt(const string& s);

struct Test {
  vector<int> m_bases;
};

struct Problem {
  vector<Test> m_tests;
  int m_numTests;
};

static void SolveOneTest(vector<string>& strings, Problem& problem, int& nextTestLine);
static void SolveProblem(vector<string>& strings);

static void Initialize();

int main() {
  // read input txt and get input strings
  vector<string> inputStrings;
  GetInputStrings(&inputStrings);

  // debug print input
  DebugPrintLines(inputStrings);

  // initialize(something needed before solving problem)
  Initialize();

  // solve problem
  SolveProblem(inputStrings);

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

/*
int GetInt(const string& s) {
  return atoi(s.c_str());
}
*/

void Initialize() {
}

void SolveProblem(vector<string>& strings) {
  Problem problem;
  istringstream iss(strings[0]);
  // get test nums
  iss >> problem.m_numTests;

  // get tests
  int nextTestLine = 1;
  for(int i = 0; i < problem.m_numTests; i++) {
    cout << "Case #" << i+1 << ": ";
    SolveOneTest(strings, problem, nextTestLine);
    if(i+1 != problem.m_numTests) {
      cout << endl;
    }
  }
}

void SolveOneTest(vector<string>& strings, Problem& problem, int& nextTestLine) {
  vector<long long> bases;

  istringstream iss(strings[nextTestLine]);
  string word;
  iss >> word;

  bool hasChar[40];
  for(int i = 0; i < 40; i++) {
    hasChar[i] = false;
  }

  for(unsigned int i = 0; i < word.size(); i++) {
    char c = word[i];
    int intC = (c >= 'a') ? (c - 87) : c - '0';
    hasChar[intC] = true;
  }

  int base = 0;
  for(int i = 0; i < 40; i++) {
    if(hasChar[i]) {
      base++;
    }
  }

  vector<char> cVec;
  for(unsigned int i = 0; i < word.size(); i++) {
    cVec.push_back(word[i]);
  }

  // sort(cVec.begin(), cVec.end());
  int mapping[40];
  for(int i = 0; i < 40; i++) {
    mapping[i] = -1;
  }
  int b = 0;
  
  for(unsigned int i = 0; i < word.size(); i++) {
    char c = cVec[i];
    int intC = (c >= 'a') ? (c - 87) : c - '0';
    if(-1 == mapping[intC]) {
      mapping[intC] = b;
      b++;
    }
  }

  char top = word[0];
  bool found = false;
  for(unsigned int i = 0; i < word.size(); i++) {
    char c = word[i];
    if(top != c) {
      found = true;
      int intTop = (top >= 'a') ? (top - 87) : top - '0';
      int tmp = mapping[intTop];
      int intC = (c >= 'a') ? (c - 87) : c - '0';
      int tmp2 = mapping[intC];
      
      mapping[intTop] = tmp2;
      mapping[intC] = tmp;
      break;
    }
  }
  if(!found) {
    int intTop = (top >= 'a') ? (top - 87) : top - '0';
    mapping[intTop] = 1;
    base = 2;
  }

  int ba = 1;
  long long res = 0;
  for(unsigned int i = 0; i < word.size(); i++) {
    char c = word[word.size() - i - 1];
    int intC = (c >= 'a') ? (c - 87) : c - '0';
    res += mapping[intC] * ba;
    ba *= base;
  }

  cout << res;

  nextTestLine++;
}
