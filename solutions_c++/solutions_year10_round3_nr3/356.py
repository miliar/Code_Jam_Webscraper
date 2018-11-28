#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <utility>
#include <list>
#include <stack>
#include <string>
#include <queue>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cctype>
using namespace std;

#define REP(i,n) FOR(i,0,n)
#define FOR(i,s,n) for (int i = (int)(s); i < (int)(n); ++i)
#define ALL(c) (c).begin(), (c).end()
#define PB push_back
#define MP make_pair

int M, N;
int table[2050][2050];
int tmp[2050][2050];

int h2i(char c)
{
  if (isdigit(c)) return c - '0';
  else            return c - 'A' + 10;
}

int countBoard(int size)
{
  //REP(i, M) REP(j, N) dp[i][j] = 1;
  int ans = 0;
  REP(i, M-size+1) {
    REP(j, N-size+1) {
      bool success = true;
      int base = table[i][j];
      if (base < 0) continue;

      REP(ii, size) {
        REP(jj, size) {
          //if (i+ii >= M || j+jj >= N) abort();
          int bit = ((ii ^ jj) & 1);
          int p = table[i+ii][j+jj];
          if (p< 0) success = false;
          //if (bit < 0) abort();
          if (success && table[i+ii][j+jj] == (base ? bit : !bit)) {
            success = false;
          }
        }
      }
      if (!success) continue;
      // cout << "(" << i << "," << j << "):" << size << endl;
      ans++;
      REP(ii, size) {
        REP(jj, size) {
          // if (size == 4) {
          //   cout << " " << i+ii << ", " << j+jj << " => " << table[i+ii][j+jj]
          //        << " <=> " << ((ii ^ jj) & 1) << endl;
          // }
          table[i+ii][j+jj] = -1;
        }
      }
          // if (size == 4) {
          //   cout << " ---" << endl;
          // }
    }
  }
  return ans;
}

int main()
{
  int T;
  cin >> T;
  REP(cs, T) {
    REP(i, 2050) REP(j, 2050) table[i][j] = -1;

    cin >> M >> N;
    REP(i, M) {
      REP(j, N/4) {
        char c;
        cin >> c;
        int d = h2i(c);
        REP(k, 4) {
          table[i][j*4 + 3-k] = ((d & (1 << k)) ? 1 : 0);
        }
      }
    }

    // REP(i, M) {
    //   REP(j, N) {
    //     cout << table[i][j];
    //   }
    //   cout << endl;
    // }

    vector<pair<int, int> > ans;
    for (int size = min(M, N); size >= 1; size--) {
      int ret = countBoard(size);
      if (ret) {
        ans.PB(MP(size, ret));
      }
    }
    
    cout << "Case #" << cs+1 << ": " << ans.size() << endl;
    REP(i, ans.size()) {
      cout << ans[i].first << " " << ans[i].second << endl;
    }
  }
  return 0;
}


