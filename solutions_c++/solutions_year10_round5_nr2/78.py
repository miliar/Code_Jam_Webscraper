#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <fstream>
#include <map>
#include <set>
#include <string>
#include <vector>
#include <cassert>

#define x first
#define y second
#define pb push_back
#define mp make_pair
#define forit(i, s) for(__typeof(s.begin()) i = s.begin(); i != s.end(); i++)

using namespace std;

typedef long long dbl;
typedef long long ll;
typedef pair <dbl, dbl> pnt;

#define maxn 2000000

int dp[maxn];

int main( void )
{
  int tn;
  cin >> tn;

  for (int tt = 1; tt <= tn; tt++) {
    cerr << tt << endl;
    printf("Case #%d: ", tt);
    ll L;
    cin >> L;
    int n;
    cin >> n;
    memset(dp, 63, sizeof(dp));
    int inf = dp[0];
    dp[0] = 0;
    vector <int> v(n);
    for (int i = 0; i < n; i++)  {
      cin >> v[i];
    }
    sort(v.begin(), v.end());
    for (int i = 0; i < n; i++) {
      for (int j = 0; j + v[i] < maxn; j++) {
        dp[j + v[i]] = min(dp[j + v[i]], dp[j] + 1);
      }
    }
    ll res = (L - maxn + v.back()) / v.back();
    L -= v.back() * res;
    assert(L < maxn);
    if (dp[(int)L] != inf) {
      cout << res + dp[(int)L] << endl;
    } else {
      printf("IMPOSSIBLE\n");
    }
  }

  return 0;
}

