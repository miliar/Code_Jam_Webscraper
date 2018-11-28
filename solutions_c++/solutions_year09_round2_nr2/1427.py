#include <cstdio>
#include <iostream>
#include <vector>
#define baseNumber unsigned long long

using namespace std;

class NextNumber {
  public:
  int caseNumber;
  baseNumber number;
  NextNumber (int input);
  vector <int> inputNumberPattern;
  void readNumber();
  void verifyNext();
  vector <int> verifyPattern(baseNumber number);
  bool comparePattern(vector <int> a, vector <int> b);
};

vector <int> NextNumber::verifyPattern(baseNumber number) {
  vector <int> pattern;
  pattern.clear();
  for (int c = 0; c < 10; c++) {
    pattern.push_back(0);
  }
  baseNumber aux = number;
  while (aux > 0) {
    pattern[aux%10]++;
    aux = aux/10;
  }
  return pattern;
}
bool NextNumber::comparePattern(vector <int> a, vector <int> b) {
  for (int c = 1; c < 10; c++) {
    if (a[c] != b[c])
      return false;
  }
  return true;
}

void NextNumber::readNumber() {
  cin >> number;
  inputNumberPattern = verifyPattern(number);
  
}

void NextNumber::verifyNext() {
  vector <int> newNumberPattern;
  number++;
  newNumberPattern = verifyPattern(number);
  while (comparePattern(newNumberPattern, inputNumberPattern) == false) {
    number++;
    newNumberPattern = verifyPattern(number);
  }
  printf ("Case #%d: ",caseNumber);
  cout << number;
  printf("\n");

}

 NextNumber::NextNumber (int input) {
  caseNumber = input;
  readNumber();
  verifyNext();
}

int main() {
  int numOfCases;
  NextNumber *next;
  scanf("%d",&numOfCases);
  for (int c = 1; c <= numOfCases; c++) {
    next = new NextNumber(c);
    delete next;    
  }
}
