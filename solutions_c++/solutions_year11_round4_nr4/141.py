#include <cstdio>
#include <iostream>
#include <vector>
#include <memory.h>
#include <string.h>
#include <sstream>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <string>
using namespace std;

#define pb push_back
#define mp make_pair
#define sz(a) int((a).size())
#define forn(i, n) for (int i=0; i<(n); ++i)
#define foreach(it, a) for (__typeof((a).begin()) it=(a).begin(); it!=(a).end(); ++it)

typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;

const int maxn = 40;

vector<int> g[maxn];
int d[maxn], q[maxn], qs, qf;
int n, m;


int bfs(int S, int T)
{
  forn (i, n) d[i] = -1;
  qs = qf = 0;
  d[S] = 0, q[qf++] = S;
  for (; qs<qf; ++qs)
  {
    int x = q[qs];
    foreach (y, g[x])
      if (d[*y] == -1)
        d[*y] = d[x]+1, q[qf++] = *y;
  }
  return d[T];
}

int bcnt(ll x)
{
  return x == 0 ? 0 : 1+bcnt(x&(x-1));
}

int res;
int lim;
void func(ll mask, int k)
{
  ll nxt = 0;
  forn (i, n) if (mask&(1LL<<i))
    foreach (j, g[i])
      if (~mask&(1LL<<(*j)))
        nxt |= 1LL<<(*j);
  if (k == lim)
  {
//    cout << nxt << endl;
    if (nxt & 2) res = max(res, bcnt(nxt));
//    cout << res << endl;
    return ;
  }      
  forn (i, n) if (d[i] == k+1) if (nxt&(1LL<<i))
    func(mask|(1LL<<i), k+1);
}


int main()
{
  freopen("a.in", "r", stdin);
  freopen("a.out", "w", stdout);
  
  int tc; scanf("%d", &tc);
  for (int tt=1; tt<=tc; ++tt)
  {
    fprintf(stderr, "tc = %d\n", tt);
    cin >> n >> m;
    string s;
    forn (i, n) g[i].clear();
    forn (i, m)
    {
      cin >> s;
      forn (j, sz(s)) if (s[j]==',') s[j] = ' ';
      istringstream sin(s);
      int x, y; sin >> x >> y;
      g[x].pb(y), g[y].pb(x);
    }
    res = 0;
    int d = bfs(0, 1);
    lim = d-1;
    func(1, 0);
    printf("Case #%d: %d %d\n", tt, d-1, res);
        
  }
  
  return 0;
}
