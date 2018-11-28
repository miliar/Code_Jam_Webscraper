#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cassert>

#include <algorithm>
#include <vector>
#include <set>
#include <map>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)

typedef long long ll;

const int MOD = (int)1e5 + 3;
const int maxn = 503;

int f[maxn][maxn];
int C[maxn][maxn];

inline void add( int &a, int b )
{
  if ((a += b) >= MOD) a -= MOD;
}

inline int mul( int a, int b )
{
  return ((ll)a * b) % MOD;
}

int main()
{
  C[0][0] = 1;
  forn(i, maxn - 1)
    forn(j, maxn - 1)
      add(C[i + 1][j], C[i][j]), add(C[i + 1][j + 1], C[i][j]);

  for (int n = 2; n < maxn; n++)
    for (int k = 1; k < n; k++)
    {
      f[n][k] = (k == 1);
      for (int i = 1; i < k; i++)
        add(f[n][k], mul(f[k][i], C[n - k - 1][k - i - 1]));
    }

  int tn;
  scanf("%d", &tn);
  for (int tt = 1; tt <= tn; tt++)
  {  
    int n, res = 0;
    scanf("%d", &n);
    forn(k, n)
      add(res, f[n][k]);
    printf("Case #%d: %d\n", tt, res);
  }
  return 0;
}
