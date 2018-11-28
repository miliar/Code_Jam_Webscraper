/*
ID: Plagapong
LANG: C++
TASK: mountain
*/

#include<iostream>
#include<fstream>
#include<algorithm>
#include<string>
#include<cmath>
#define NOPE "Impossible"

using namespace std;
int garbage;
int n;
int x[2005];
int h[2005];
int stack[2005], shead;

void preprocess() {
  // Preprocess
  
}

void clearVars() {
  // Clear variables
  for (int i = 0; i < 2005; i++) {
    h[i] = -1;
  }
}

void process() {
  // Code here!
  garbage = scanf("%d", &n);
  for (int i = 1; i < n; i++) { 
    garbage = scanf("%d", &x[i]);
  }
  // Work backward
  h[n] = 1000000000;
  for (int i = n; i > 0; i--) {
    if (h[i] == -1) {
      printf("Something's wrong! ");
    }
    bool overcome = false;
    shead = 0;
    for (int j = i-1; j > 0; j--) {
      if (overcome) {
        if (x[j] == i) {
          printf(NOPE);
          return;
        }
      } else {
        if (x[j] > i) {
          overcome = true;
        } else if (x[j] == i) {
          stack[shead++] = j;
        }
      }
    }
    // Assign heights
    if (shead > 0) {
      int j = stack[shead - 1];
      int maxh = h[i] - 1;
      for (int k = i+1; k <= n; k++) {
        if (h[k] > h[i]) {
          int limit = h[i];
          int delta = h[k] - h[i];
          if ((delta * (i-j)) % (k-i) != 0) {
            limit = limit - delta * (i-j) / (k-i) - 1;
          } else {
            limit = limit - delta * (i-j) / (k-i);
          }
          maxh = min(maxh, limit);
        }
      }
      h[stack[shead - 1]] = maxh;
      for (int k = shead - 2; k >= 0; k--) {
        int delta = h[i] - maxh;
        if ((delta * (stack[k] - stack[k+1])) % (i - stack[k+1]) == 0) {
          maxh = maxh + (delta * (stack[k] - stack[k+1])) / (i - stack[k+1]) - 1;
        } else {
          maxh = maxh + (delta * (stack[k] - stack[k+1])) / (i - stack[k+1]);
        }
        h[stack[k]] = maxh;
      }
    }
  }
  for (int i = 1; i < n; i++) printf("%d ", h[i]); printf("%d", h[n]);
}


int main() {
  preprocess();
  int times;
  cin >> times;
  for (int i = 1; i <= times; i++) {
	cout << "Case #" << i << ": ";
	clearVars();
	process();
	cout << endl;
  }
  return 0;
}
