#include <algorithm>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string> 
#include <vector>

using namespace std;

int num_bits (int n) {
  int ret = 0;
  while (n) {
    ++ret;
    n&=n-1;
  }
  return ret;
}

int main() {
  int num_cases ;
  cin >> num_cases;
  for (int case_num = 1; case_num <= num_cases; ++case_num) {
    cout << "Case #" << case_num << ": ";
    int n,m;
    cin >> n >> m;
    int best = 0;

    vector<int> rows (n,0);
    for (int i = 0 ; i < n; ++i) {
      string seatline;
      cin >> seatline;
      // cerr << seatline << "\n";
      for (int j = 0; j < m; ++j) {
        if (seatline[j]=='x') rows[i] |= 1<<j;
      }
    }
    
    vector<vector<int> > num_seated (n, vector<int> (1<<m,0));
    for (int mask = 0 ; mask < (1<< m); ++ mask) {
      if (mask & rows[0]) continue;
      bool good = true;
      for (int j = 1; j < m; ++j) {
        if ((mask>>j&1) && (mask>>(j-1)&1)) good = false;
      }
      if (!good) continue;
      int cstudents = num_bits (mask);
      best = max (best, cstudents);
      num_seated[0][mask] = cstudents;
    }
    // cerr << num_seated[0][5] << "\n";
    
    for (int i = 1; i < n; ++i) {
      for (int mask = 0 ; mask < (1<< m); ++ mask) {
        if (mask & rows[i]) continue;
        int cstudents = num_bits (mask);
        bool good = true;
        
        for (int j = 1; j < m; ++j) {
          if ((mask>>j&1) && (mask>>(j-1)&1)) good = false;
        }
        if (!good) continue;
        best = max (best, cstudents);
        
        for (int mask2 = 0; mask2 < (1<<m); ++mask2) {
          good = true;
          for (int j = 0; j < m; ++j) {
            if ((mask>>j&1)) {
              if (j>0 && (mask2>>(j-1)&1)) good = false;
              if (mask2>>(j+1)&1) good  = false;
            }
          }
          if (good) {
            num_seated[i][mask] = max (num_seated[i][mask], num_seated[i-1][mask2] + cstudents);
            best = max (best, num_seated[i][mask]);
          }
          
        }
      }
    }
    // cerr << num_seated[1][5] << "\n";
    cout << best << "\n";
  }
}

      
