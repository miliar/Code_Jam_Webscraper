#include <algorithm>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <vector>
#include <sstream>

#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>

#define REP(i, n) for(int i=0; i<(int)n; ++i)
#define FOR(i, c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define ALL(c) (c).begin(),(c).end()
#define each(i, c) FOR(i, c)

#define VAR(a) cout << #a << " : " << a << endl;

typedef long long int lli;

using namespace std;

int main(int argc, char *argv[])
{
  const int N = 2300;
  bool cnt[N][N];
  fill(&cnt[0][0], &cnt[N - 1][N], false);

  char buff[100];

  for (int n = 0; n < (int)N; ++n) {
    for (int m = n + 1; m < (int)N; ++m) {
      sprintf(buff, "%d", n);
      string s(buff);
      sprintf(buff, "%d", m);
      string t(buff);
    
      if (s.size() != t.size()) continue;
  
      for (int i = 0; i <= (int)t.size(); ++i) {
        bool flg = true;
        for (int j = 0; j < (int)s.size() && flg; ++j) {
          int a = j;
          int b = (i + j) % t.size();
          flg = flg && s[a] == t[b];
        }
        if (flg) {
          cnt[n][m] = true;
          break;
        }
      }
    }
  }

  int tc;
  cin >> tc;
  while (tc--) {
    int A, B;
    cin >> A >> B;

    int res = 0;
    for (int n = A; n <= (int)B; ++n) {
      for (int m = n + 1; m <= (int)B; ++m) {
        res += cnt[n][m];
      }
    }

    static int TC = 0;
    cout << "Case #" << ++TC << ": " << res << endl;
  }
  return 0;
}
