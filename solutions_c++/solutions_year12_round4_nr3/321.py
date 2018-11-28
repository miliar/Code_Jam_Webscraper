#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <queue>
#include <string.h>
#include <algorithm>
#include <set>
#include <cstdio>

using namespace std;

int main() {
  int TC; cin >> TC;
  for (int t = 1; t <= TC; t++) {
    int N; cin >> N;
    vector<int> tops(N-1);
    for(int i = 0; i < N-1; ++i) {
      cin >> tops[i];
      tops[i]--;
    }
    bool possible = true;
    vector<int> cmax(N-1, 30000);
    for(int i = 0; i < N-1; ++i) {
      if(tops[i] > cmax[i]) {
        possible = false;
        break;
      }
      for(int j = i+1; j < tops[i]; ++j) {
        cmax[j] = min(cmax[j], tops[i]);
      }
    }
    if(!possible) {
      cout << "Case #" << t << ": Impossible\n";
      continue;
    }
    vector<int> heights(N, 0);
    bool changed = true;
    while(changed) {
      changed = false;
      for(int i = 0; i < N-1; ++i) {
        int idx = i+1;
        double dy = (heights[i+1] - heights[i]);
        for(int j = i+1; j < N; ++j) {
          if(heights[j] > heights[i] + (j-i)*dy) {
            idx = j;
            dy = (heights[j] - heights[i])/(0.0 + j-i);
          }
        }
        if(idx != tops[i]) {
          //cout << i << ": " << idx << endl;
          changed = true;
          heights[tops[i]] += 100;
          break;
        }
      }
    }
    printf("Case #%d:", t);
    for(int i = 0; i< N; ++i) {
      cout << ' ' << heights[i];
    }
    cout << endl;
  }


  return 0;
}
