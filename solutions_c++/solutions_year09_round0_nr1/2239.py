#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>

const int DEBUG = 0;

using namespace std;

static string s_inputFile = "A-large.in";

static void GetInputStrings(vector<string>* strings);
static void DebugPrintLines(vector<string>& strings);
static void PrintLines(vector<string>& strings);

//static int GetInt(const string& s);

struct Literal {
  long m_charBits;
};

struct Test {
  Literal m_word[20];
};

struct Dict {
  vector<string> m_words;
};

struct Problem {
  vector<Test> m_tests;
  Dict m_dict;
  int m_wordLength;
  int m_numDict;
  int m_numTests;
};

static void GetProblem(vector<string>& strings, Problem* problem);
static void SolveTest(vector<string>& strings, Problem* problem, int& nextTestLine);

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

/*
int GetInt(const string& s) {
  return atoi(s.c_str());
}
*/

void CreateDict(vector<string>& strings, Problem* problem, int& nextTestLine) {
  for(int i = 0; i < problem->m_numDict; i++) {
    problem->m_dict.m_words.push_back(strings[nextTestLine + i]);
  }

  sort(problem->m_dict.m_words.begin(), problem->m_dict.m_words.end());
  nextTestLine += problem->m_numDict;
}

void GetProblem(vector<string>& strings, Problem* problem) {
  istringstream iss(strings[0]);
  // get test nums
  iss >> problem->m_wordLength;
  iss >> problem->m_numDict;
  iss >> problem->m_numTests;

  // get tests
  int nextTestLine = 1; // because input "test num" is 1line
  CreateDict(strings, problem, nextTestLine);
  for(int i = 0; i < problem->m_numTests; i++) {
    cout << "Case #" << i+1 << ": ";
    SolveTest(strings, problem, nextTestLine);
    if(i+1 != problem->m_numTests) {
      cout << endl;
    }
  }
}

void SolveTest(vector<string>& strings, Problem* problem, int& nextTestLine) {
  string testWord = strings[nextTestLine];

  int i = 0;
  bool isInnerChar = false;
  int currentChar = 0;
  Test test;

  for(int i = 0; i < problem->m_wordLength; i++) {
    test.m_word[i].m_charBits = 0;
  }

  while(currentChar != problem->m_wordLength) {
    switch(testWord[i]) {
      case '(':
        isInnerChar = true;
        break;
      case ')':
        isInnerChar = false;
        currentChar++;
        break;
      default:
        long bit = 1;
        bit = bit << (long)(testWord[i] - 'a');
        test.m_word[currentChar].m_charBits |= bit;
        if(isInnerChar) {
        } else {
          currentChar++;
        }
        break;
    }
    i++;
  }

  int result = 0;
  for(int j = 0; j < problem->m_numDict; j++) {
    bool matched = false;
    for(int i = 0; i < problem->m_wordLength; i++) {
      long bit = 1;
      int shift = (problem->m_dict.m_words[j][i] - 'a');
      bit = bit << shift;
      bit &= test.m_word[i].m_charBits;
      bit = bit >> shift;
      matched = bit & 1;
      if(!matched) {
        break;
      }
    }
    if(matched) {
      result++;
    }
  }

  cout << result;

  nextTestLine++;
}
