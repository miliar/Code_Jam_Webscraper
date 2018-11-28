// Compile:
// g++ -std=c++0x C.cpp
// 
// Execute:
// ./a.out < C-small-attempt0.in

#include <string>
#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <set>

using namespace std;

int numDigits(int num) {
  int size = 1;
  int newnum = num;
  while(newnum /= 10) {
    size++;
  }
  return size;
}

// Return total cycles of n in (n,B]
int totalCycles(int n, int B) {
  // If not same length, abort;
  if (numDigits(n) != numDigits(B)) {
    return false;
  }

  int numCycles  = numDigits(n)-1;
  int cycle = n;

  vector<int> cycles;
  vector<int>::iterator it;
  for (int i=0; i<numCycles; ++i) {
    int lastDigit = cycle % 10;
    int otherDigits = cycle / 10;
    cycle = lastDigit * pow(10, numCycles) + otherDigits;
    if (lastDigit != 0 && cycle > n && cycle <= B) {
        cycles.push_back(cycle);
    }
  }
  // Remove dups.
  set<int> cycles2(cycles.begin(), cycles.end());
  return cycles2.size();
}


int main() {
  int N; 
  cin >> N;
  for (int i=0; i<N; i++) {
    int A, B; 
    cin >> A >> B;
    int counter = 0;
    for (int n=A; n<B; ++n) {
      counter += totalCycles(n, B);
    }
    cout << "Case #" << i+1 << ": " << counter << endl;
  }
  return 0;
}

