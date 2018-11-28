#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
using namespace std; 

typedef vector<int> vi;
typedef vector<string> vs;
typedef long long ll;

#define all(a) a.begin(), a.end()
#define sz(a) (int)a.size()
#define clr(a, v) memset((a), (v), sizeof(a))
#define forn(i, n) for (int i = 0; i < (n); ++i)
#define mp make_pair

const int inf=1000000000;
const int C=6;

typedef pair<int,int> pii;


priority_queue<pii,vector<pii>,greater<pii> > q;
int f[12][C][1<<C][1<<C];
char tab[32][32];
int n, m, k;


inline int code(int x, int y, int m1, int m2) {
 int res=x;
 res=(res<<C)+y;
 res=(res<<C)+m1;
 res=(res<<C)+m2;
 return res;
}
inline void decode(int st, int& x, int& y, int& m1, int& m2) {
 m2=st&((1<<C)-1); st>>=C;
 m1=st&((1<<C)-1); st>>=C;
 y =st&((1<<C)-1);  st>>=C;
 x=st;
}


inline void push(int x, int y, int m1, int m2, int dd) {
 if (f[x][y][m1][m2]<=dd) return;
 f[x][y][m1][m2]=dd;
 int st=code(x, y, m1, m2);
 q.push(mp(dd, st));
}

int solve () {
 forn (i, 12) forn (j, C) forn (k, (1<<C)) forn (l, (1<<C)) f[i][j][k][l]=inf;


 push(0, 0, 0, 0, 0);

 int res=inf;

 while (!q.empty()) {
  int st=q.top().second, dd=q.top().first;
  q.pop();
  int x, y, m1, m2;
  decode(st, x, y, m1, m2);
  if (dd>f[x][y][m1][m2]) continue;

  if (x==n-1) {
   res=min(res, f[x][y][m1][m2]);
  }

  bool ground=(x+1==n) || (tab[x+1][y]=='#' && (~m2&(1<<y)));
  
  if (!ground) {
   int xx=x+1, d=1;
   while (xx+1<n && tab[xx+1][y]=='.') ++xx, ++d;
   if (d>k) continue;
   if (d==1) {
    push(xx, y, m2, 0, dd);
   } else {
    push(xx, y, 0, 0, dd);
   }
  } else {

    if (x+1<n) {
      if (y>0 && (tab[x][y-1]=='.' || (m1&(1<<(y-1)))) && (tab[x+1][y-1]=='#' && (~m2&(1<<(y-1))))) {
        int nm2=m2|(1<<(y-1));
        push(x, y, m1, nm2, dd+1);
      }

      if (y+1<m && (tab[x][y+1]=='.' || (m1&(1<<(y+1)))) && (tab[x+1][y+1]=='#' && (~m2&(1<<(y+1))))) {
        int nm2=m2|(1<<(y+1));
        push(x, y, m1, nm2, dd+1);
      }

    }

    if (y>0 && (tab[x][y-1]=='.' || (m1&(1<<(y-1))))) {
      push(x, y-1, m1, m2, dd);
    }

    if (y+1<m && (tab[x][y+1]=='.' || (m1&(1<<(y+1))))) {
      push(x, y+1, m1, m2, dd);
    }
  }
   
 }
     

 return res;
}

int main() {
 freopen("a.in", "r", stdin);
 freopen("a.out", "w", stdout);

 int nt; scanf("%d", &nt);

 for (int tc=1; tc<=nt; ++tc) {
  scanf("%d %d %d", &n, &m, &k);
  gets(tab[0]);
  forn (i, n) gets(tab[i]);
  memset(f, 0xff, sizeof(f));
  int res=solve();
  if (res==inf) printf("Case #%d: No\n", tc);
  else printf("Case #%d: Yes %d\n", tc, res);
 }

 return 0;
}
