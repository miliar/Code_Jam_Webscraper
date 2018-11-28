#include <fstream>
#include <iostream>
#include <stdio.h>
#include <math.h>

using namespace std;

struct muc {
  char c;
  int v;
};

int getNext(int currentIndex, char searchFor, int n, muc vals[]) {

  for (int i = currentIndex + 1; i < n; i++) {
    if (vals[i].c == searchFor) {
      return i;
    }
  }
  return -1;
}

int solve(int n, muc vals[]) {
  
  int currIndex = 0, currentIndex = 0;
  int currentO = 1;
  int currentB = 1;
  int total = 0;
//  cout << "CASE:" << endl;
  while (currIndex < n) {
    currentIndex = currIndex;
    currIndex ++;
    // We want to satisfy the request on position currentIndex
    int nextDude = getNext(currentIndex, vals[currentIndex].c == 'O' ? 'B' : 'O', n, vals);

    if (vals[currentIndex].c == 'O') {
      int offset = fabs(vals[currentIndex].v - currentO) + 1;
      total += offset;
      currentO = vals[currentIndex].v;
      if (nextDude == -1) continue;
      if (vals[nextDude].v > currentB) {
        currentB += min(offset, vals[nextDude].v - currentB);
      } else {
        currentB -= min(offset, currentB - vals[nextDude].v);
      }
    } else {
      int offset = fabs(vals[currentIndex].v - currentB) + 1;
      total += offset;
      currentB = vals[currentIndex].v;
      if (nextDude == -1) continue;
      if (vals[nextDude].v > currentO) {
        currentO += min(offset, vals[nextDude].v - currentO);
      } else {
        currentO -= min(offset, currentO - vals[nextDude].v);
      }
    }
//    cout << "NEXTDUDE " << nextDude << " " << currentO <<  " " << currentB <<  "   " << total << endl;
  }
//  cout << total << " ENDCASE " << endl; 

  return total;
}

int main() {
  ifstream f("bt.in");  
  ofstream g("bt.out");

  int t, n;
  muc vals[5000];
  f >> t;

  for (int i = 0; i < t; i++) {
    f >> n;
    for (int j = 0; j < n; j++) {
      f >> vals[j].c >> vals[j].v;
    }
    int res = solve(n, vals);
    g << "Case #" << i + 1 << ": " << res << endl;
  }
  

  f.close();
  g.close();

  return 0;
}

