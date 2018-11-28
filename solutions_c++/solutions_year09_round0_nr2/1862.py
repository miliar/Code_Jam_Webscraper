#include <cstdio>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <list>
using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef pair<int, int> PII;
typedef vector<PII> VPII;

#define REP(x, n) for(int x = 0; x < (n); ++x)
#define FOR(x, b, e) for(int x = b; x <= (e); ++x)
#define FORD(x, b, e) for(int x = b; x >= (e); --x)
#define VAR(v, n) typeof(n) v = (n)
#define FOREACH(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define SIZE(x) ((int)(x).size())
#define PB push_back
#define PF push_front
#define MP make_pair
#define FI first
#define SE second

const int INF = 1000000001;
const double EPS = 10e-9;

const int Max = 1200;
int a,b,zz,w,k,t[Max][Max], q[Max][Max],s;
map<int, int> M;
PII f[Max*Max];

int main() {

scanf("%d", &zz);
FOR(z,1,zz) {
  scanf("%d%d", &w, &k);

  FOR(i,1,w) FOR(j,1,k) scanf("%d", &t[i][j]);
  REP(i, max(w,k)+5) {
    t[0][i]=t[i][0]=t[w+1][i]=t[i][k+1]=INF;
    q[0][i]=q[i][0]=q[w+1][i]=q[i][k+1]=0;
  }

  FOR(i,1,w) FOR(j,1,k) {
    s = min( min(t[i-1][j], t[i+1][j]), min(t[i][j-1], t[i][j+1]));

    if(s >= t[i][j]) q[i][j]=0; else
    if(t[i-1][j]==s) q[i][j]=1; else
    if(t[i][j-1]==s) q[i][j]=2; else
    if(t[i][j+1]==s) q[i][j]=3; else q[i][j]=4;
  }

  s=0;
  FOR(i,1,w) FOR(j,1,k) if(q[i][j]==0) {
    f[0]=MP(i,j); a=0; b=1; s--;

    while(a<b) {
      int x,y;
      x=f[a].FI; y=f[a].SE; q[x][y]=s;

      if(q[x-1][y]==4) f[b++]=MP(x-1,y);
      if(q[x][y+1]==2) f[b++]=MP(x,y+1);
      if(q[x+1][y]==1) f[b++]=MP(x+1,y);
      if(q[x][y-1]==3) f[b++]=MP(x,y-1);

      a++;
    }
  }

  s=0; M.clear();

  printf("Case #%d:\n", z);
  FOR(x,1,w) {
    FOR(y,1,k) {
      if(M.find(q[x][y])==M.end()) M[q[x][y]]=s++;
      printf("%c ", (int)'a' + M[q[x][y]]);
//      if(y<k) printf(" ");
    }
    printf("\n");
  }
}

return 0;
}
