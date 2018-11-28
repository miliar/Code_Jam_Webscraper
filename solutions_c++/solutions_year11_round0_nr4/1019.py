#include <iostream>
#include <iomanip>
#include <cmath>
#include <cstring>

using namespace std;

int T, N;
int list[1000];
int visited[1000];
int cycles[1000];
int numCycles;

double expectedHits[1001];
double derangementProb[1001];
double inverseFactorial[1001];

void computeInverseFactorials() {
  inverseFactorial[0] = 1;
  inverseFactorial[1] = 1;
  for (int i = 2; i < 1001; ++i) {
    inverseFactorial[i] = inverseFactorial[i-1] / ((double) i);
  }
}

void computeDerangementProbs() {
  derangementProb[0] = 1;
  for (int i = 1; i < 1001; ++i) {
    if (i > 125) {
      derangementProb[i] = derangementProb[i-1];
    } else {
      if (i % 2 == 0) {
        derangementProb[i] = derangementProb[i-1] + inverseFactorial[i];
      } else {
        derangementProb[i] = derangementProb[i-1] - inverseFactorial[i];
      }
    }
  }
}

double d(int n, int k) {
  return derangementProb[n-k] * inverseFactorial[k];
}

void computeExpectedHits() {
  expectedHits[0] = 0;
  expectedHits[1] = 0;
  for (int i = 2; i < 1001; ++i) {
    expectedHits[i] = d(i,0);
    for (int j = 1; j <= i; ++j) {
      expectedHits[i] += d(i,j) * (1 + expectedHits[i-j]);
    }
    expectedHits[i] /= (1.0 - d(i,0));
    cerr << i << ": " << expectedHits[i] << " " << d(i,0)  << " " << d(i,i-1) << endl;
  }
}

int main() {
  computeInverseFactorials();
  computeDerangementProbs();
  computeExpectedHits();

  cin >> T;
  for (int t = 0; t < T; ++t) {
    // Initialize data
    numCycles = 0;
    memset(visited, 0, 1000 * sizeof(int));
    memset(cycles, 0, 1000 * sizeof(int));
    memset(list, 0, 1000 * sizeof(int));

    cin >> N;
    for (int i = 0; i < N; ++i) {
      int temp;
      cin >> temp;
      list[i] = temp - 1;
    }

    // Find number and size of cycles
    for (int i = 0; i < N; ++i) {
      if (visited[i]) continue;
      int currentIndex = i;
      int cycleSize = 0;
      do {
        ++cycleSize;
        visited[currentIndex] = 1;
        currentIndex = list[currentIndex];
      } while (currentIndex != i);
      cycles[numCycles] = cycleSize;
      ++numCycles;
    }

    double total = 0.0;
    for (int i = 0; i < numCycles; ++i) {
      cerr << cycles[i] << endl;
      total += expectedHits[cycles[i]];
    }

    cout << "Case #" << (t+1) << ": " << total << endl;
  }
}
