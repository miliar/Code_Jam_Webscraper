#include <algorithm>
#include <cstdio>
#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <set>
#include <cassert>
#include <ctime>
#include <cstdlib>
#include <cmath>
#include <cstring>

#define eps 1e-9

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define sz(v)((v).size())

#define task_name "c"


using namespace std;


typedef long long ll;

#define maxn 510

ll c[maxn][maxn], mod = 100003, dp[maxn][maxn];

ll get( int n, int k ) {
  ll &res = dp[n][k];

  if (res >= 0) {
    return res;
  }

  res = 0;

  if (k == 1) {
    return res = 1;
  }
  
  for (int i = 1; i <= k - 1; i++) {
    res = (res + get(k, i) * c[n - k - 1][k - i - 1]) % mod;
  }
  return res;
}

int main( void )
{
  freopen(task_name ".in", "r", stdin);
  freopen(task_name ".out", "w", stdout);

  int tn;
  scanf("%d", &tn);

  c[0][0] = 1;
  for (int i = 0; i + 1 < maxn; i++) {
    for (int j = 0; j <= i; j++) {
      c[i + 1][j] = (c[i + 1][j] + c[i][j]) % mod;
      c[i + 1][j + 1] = (c[i + 1][j + 1] + c[i][j]) % mod;
    }
  }

  memset(dp, -1, sizeof(dp));

  for (int tt = 1; tt <= tn; tt++)
  {
    printf("Case #%d: ", tt);
    int n;
    scanf("%d", &n);
    ll res = 0;
    for (int k = 1; k <= n - 1; k++) {
      res = (res + get(n, k)) % mod;
    }
    cout << res << endl;
  }

   
  
  return 0;
}