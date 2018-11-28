#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <string>
#include <iostream>
#include <algorithm>

using namespace std;

#define pb push_back
#define mp make_pair
#define sz(a) (int)(a).size()
#define all(a) (a).begin(), (a).end()
#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; i--)
#define forit(i, a) for (__typeof((a).begin()) i = (a).begin(); i != (a).end(); i++)

typedef long long ll;
typedef pair <int, int> pii;
typedef vector <int> vi;

#define maxn 10010

int n, res, op[maxn], ch[maxn], f[maxn][2];

void dfs( int v )
{
  if (op[v] == 2)
  {
    f[v][ch[v]] = 0;
    return;
  }
  
  int l = v * 2, r = l + 1;
  dfs(l), dfs(r);
  
  forn(a, 2)
    forn(b, 2)
      forn(x, 2)
      {
        int ff = (x != op[v]) + f[l][a] + f[r][b];
        if (x != op[v] && !ch[v])
          continue;
        
        int c = (x == 0) ? (a | b) : (a & b);
        if (f[v][c] > ff)
          f[v][c] = ff;
      }
}

int main()
{
  freopen("a.in", "r", stdin);
  freopen("a.out", "w", stdout);
  
  int tn;
  scanf("%d", &tn);
  forn(tt, tn)
  {
    scanf("%d%d", &n, &res);
    for (int i = 1; i <= (n - 1) / 2; i++)
      scanf("%d%d", &op[i], &ch[i]);
    for (int i = (n + 1) / 2; i <= n; i++)
      scanf("%d", &ch[i]), op[i] = 2;
    
    memset(f, 0x10, sizeof(f));
    dfs(1);
    
    printf("Case #%d: ", tt + 1);
    if (f[1][res] <= n)
      printf("%d", f[1][res]);
    else
      printf("IMPOSSIBLE");
    puts("");
  }
  
  return 0;
}
