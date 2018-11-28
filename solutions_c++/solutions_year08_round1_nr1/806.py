#include <math.h>
#include <list>
#include <vector>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <iterator>
#include <numeric>
#include <cmath>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <cctype>
#include <cstdio>

using namespace std;
#define INF 1000000000

struct pos {
  int x;
  int y;
};


int numberCases;
ifstream inFile;
char charIn[10000];
ofstream outFile;
int cnt; 
int cnt2; 
int bestCase = INF;
int inputCount;




int n;
//int x[800], y[800];
vector<int> x, y;
long int bestTot = INF;

void findMin(void) {
  bestTot = 0;
  sort(x.begin(), x.end());
  for (int i = 0; i < x.size(); i++) {
    cout << x[i] << " ";
  }
  cout << endl;
  sort(y.begin(), y.end());
  int i;
  // Find max x
  for (i = 0; i < n; i++) {
    bestTot += x[i]*y[n-i-1];
  }
  cout << bestTot << endl;
}

void runCase(void) {
  inputCount = 0;
  bestTot = INF;
  int input;
  int count;
  x.clear();
  y.clear();

  inFile.getline(charIn, 10000000);
  istringstream inLine(charIn);
  while (inLine >> input) {
    n = input;
  }
  count = 0;
  inFile.getline(charIn, 10000000);
  istringstream inLine2(charIn);
  while (inLine2>>input) {
    x.push_back(input);
  }
  cout << x.size() << endl;
  for (int i = 0; i < x.size(); i++) {
    cout << x[i] << " ";
  }
  cout << endl;
  count = 0;
  inFile.getline(charIn, 10000000);
  istringstream inLine3(charIn);
  while (inLine3>>input) {
    y.push_back(input);
  }
  cout << y.size() << endl;
  findMin();
}

int main (int argc, char **argv) {
  inFile.open(argv[1]);
  outFile.open("output");

  // First line N
  inFile >> numberCases;
  inFile.getline(charIn, 100);

  for (int i = 0; i < numberCases; i++) {
    runCase();
    cout << "Case #" << i+1 << ": " << bestTot << endl;
    outFile << "Case #" << i+1 << ": " << bestTot << endl;
  }

  inFile.close();
  outFile.close();
}
