#include<vector>
#include<stack>
#include<set>
#include<map>
#include<queue>
#include<deque>
#include<bitset>
#include<complex>
 
#include<sstream>
#include<fstream>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cassert>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<climits>
 
#define oo            (int)13e7
#define s(n)          scanf("%d",&n)
#define sl(n)         scanf("%lld",&n)
#define sf(n)         scanf("%lf",&n)
#define fill(a,v)     memset(a, v, sizeof a)
#define ull           unsigned long long
#define ll            long long
#define bitcount      __builtin_popcount
#define all(x)        x.begin(), x.end()
#define pb( z )       push_back( z )
#define gcd           __gcd
using namespace std;

int R, C, D;
const int mxn = 512;
char _w[mxn][mxn];
int w[mxn][mxn];
int a[mxn][mxn];

ll wx[mxn][mxn];
ll wy[mxn][mxn];
ll ms[mxn][mxn];

int main(int argc, char** argv) {
  //freopen("B-small-attempt0.in", "r", stdin); freopen("B-small-attempt0.out", "w", stdout);
  //freopen("B-small-attempt1.in", "r", stdin); freopen("B-small-attempt1.out", "w", stdout);
  //freopen("B-small-attempt2.in", "r", stdin); freopen("B-small-attempt2.out", "w", stdout);
  
  freopen("B-large.in", "r", stdin); freopen("B-large.out", "w", stdout);
  int T;
  cin>>T;
  for (int t=1; t <= T; t++) {
    cin>>R>>C>>D;
    for (int x=1; x <= R; x++) {
      scanf("%s", _w[x]);
      for (int y=1; y <= C; y++) {
        w[x][y] = _w[x][y-1] - '0' + D;
        wx[x][y] = ( w[x][y] * x ) + wx[x-1][y] + wx[x][y-1] - wx[x-1][y-1];
        wy[x][y] = ( w[x][y] * y ) + wy[x-1][y] + wy[x][y-1] - wy[x-1][y-1];
        ms[x][y] = w[x][y] + ms[x-1][y] + ms[x][y-1] - ms[x-1][y-1];
      }
    }
    printf("Case #%d: ", t);
    bool done = 0;
    for (int S=min(R,C); !done && S >= 3; --S) {
      bool ok = 0;
      for (int x=1; !ok && x+S-1 <= R; x++)
      for (int y=1; !ok && y+S-1 <= C; y++) {
        
        int ux = x+S-1;
        int uy = y+S-1;
        int lx = x-1;
        int ly = y-1;
        
        ll Sum   = ms[ux][uy] - ms[ux][ly] - ms[lx][uy] + ms[lx][ly] - w[ux][uy] - w[ux][ly+1] - w[lx+1][uy] - w[lx+1][ly+1];
        ll Xpart = wx[ux][uy] - wx[ux][ly] - wx[lx][uy] + wx[lx][ly] - ux*w[ux][uy] - ux*w[ux][ly+1] - (lx+1)*w[lx+1][uy] - (lx+1)*w[lx+1][ly+1];
        ll Ypart = wy[ux][uy] - wy[ux][ly] - wy[lx][uy] + wy[lx][ly] - uy*w[ux][uy] - (ly+1)*w[ux][ly+1] - uy*w[lx+1][uy] - (ly+1)*w[lx+1][ly+1];
        
        if ( 2*Xpart == Sum * ( 2*x + S - 1) )
        if ( 2*Ypart == Sum * ( 2*y + S -1 ) ) {
          ok = 1;
        }
      }
      if (ok) {
        printf("%d\n", S);
        done = 1;
      }
    }
    if (!done) {
      puts("IMPOSSIBLE");
    }
  }
	return 0;
}
