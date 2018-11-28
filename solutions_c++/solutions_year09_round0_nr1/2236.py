#include <cstdio>
#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector <string> words;
vector <string> patterns;
vector <int> matchPattern;
int L, D, N;
int comparissionVector[256];

void readInput() {
  scanf("%d %d %d", &L, &D, &N);
  string actualWord;
  for (int c = 0; c < D; c++) {
    cin >> actualWord;
    words.push_back(actualWord);
    matchPattern.push_back(1);
  }
  for (int c = 0; c < N; c++) {
    cin >> actualWord;
    patterns.push_back(actualWord);
  }
}
void cleanMatchPattern() {
  for (int c = 0; c < matchPattern.size(); c++) {
    matchPattern[c] = 1;
  }
}

vector <string> breakPattern(string inputPattern){
  string actualLetters;
  vector <string> returnedLetters;
  int actualPosition = 0;
  while (actualPosition < inputPattern.length()){
    actualLetters.clear();
    if (inputPattern[actualPosition] == '(') {
      actualPosition++;
      while (inputPattern[actualPosition] != ')') {
        actualLetters.push_back(inputPattern[actualPosition]);
        actualPosition++;
      }
    } else {
      actualLetters.push_back(inputPattern[actualPosition]);
    }
    returnedLetters.push_back(actualLetters);
    actualPosition++;
  }
  return returnedLetters;
}

void fullfillComparissonVector(string inputSequence) {
  for (char c = 'a'; c <= 'z'; c++) {
    comparissionVector[c] = 0;
  }
  for (int c = 0; c < inputSequence.length(); c++){
    comparissionVector[inputSequence[c]] = 1;
  }
}

void updateMatchPattern(int actualLetter) {
  for (int c = 0; c < words.size(); c++) {
    if (comparissionVector[words[c][actualLetter]] == 0) {
      matchPattern[c] = 0;
    }
  }
}

void printResult (int actualTest) {
  int number = 0;
  for (int c = 0; c < matchPattern.size(); c++){
    number += matchPattern[c];
  }
  printf("Case #%d: %d\n",(actualTest + 1), number);
}

void solve() {
  vector <string> patternSequence;
  for (int actual = 0; actual < N; actual++) {
    cleanMatchPattern();
    patternSequence.clear();
    patternSequence = breakPattern(patterns[actual]);
    for (int actualLetter = 0; actualLetter < L; actualLetter++){
      fullfillComparissonVector(patternSequence[actualLetter]);
      updateMatchPattern(actualLetter);
    }
    printResult(actual);
  }
}

int main() {
  readInput();
  solve();
  scanf("%*c");
}
