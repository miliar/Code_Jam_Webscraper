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
typedef pair<int,int> pii;

#define all(a) a.begin(), a.end()
#define sz(a) (int)a.size()
#define clr(a, v) memset((a), (v), sizeof(a))
#define forn(i, n) for (int i = 0; i < (n); ++i)
#define mp make_pair

const int inf=1000000000;

int dx[]={0,0,-1,1};
int dy[]={-1,1,0,0};

char w[32][32];
int f[1024][32][32];
string g[1024][32][32];
set<pii> q;
set<pii>::iterator it;
int n, m;


inline int code(int sum, int x, int y) {
 int res=sum;
 res=(res<<5)+x;
 res=(res<<5)+y;
 return res;
}
inline void decode(int st, int& sum, int& x, int& y) {
 y=st&31; st>>=5;
 x=st&31; st>>=5;
 sum=st;
}

const int lim=850;
const int md=300;

void solve(int need) {
 for (int i=0; i<=lim; ++i)
  for (int x=0; x<n; ++x)
   for (int y=0; y<n; ++y)
    f[i][x][y]=inf;

 for (int x=0; x<n; ++x)
  for (int y=0; y<n; ++y) if (w[x][y]>='0' && w[x][y]<='9') {
   int dig=w[x][y]-'0';
   f[md+dig][x][y]=1;
   g[md+dig][x][y]=w[x][y];
   q.insert(mp(1, code(md+dig, x, y)));   
  }

 while (!q.empty()) {
  int st=(*q.begin()).second, dd=(*q.begin()).first;
  q.erase(q.begin());

  


  int sum, x, y;
  decode(st, sum, x, y);

  if (sum==md+2) {
    int z=0;
  }
  
  for (int i=0; i<4; ++i) {
   int nx=x+dx[i], ny=y+dy[i];
   if (nx>=0 && nx<n && ny>=0 && ny<n) {
    for (int j=0; j<4; ++j) {
     int nnx=nx+dx[j], nny=ny+dy[j];
     if (nnx>=0 && nnx<n && nny>=0 && nny<n) {
      int dig=w[nnx][nny]-'0';
      int nsum=sum;
      if (w[nx][ny]=='-') nsum-=dig;
      else nsum+=dig;

      if (nsum>lim) continue;
      if (nsum<0) continue;


      if (f[nsum][nnx][nny] > f[sum][x][y]+2) {
       int nst=code(nsum, nnx, nny);
       it=q.find(mp(f[nsum][nnx][nny], nst));
       if (it!=q.end()) q.erase(it);

       f[nsum][nnx][nny]=f[sum][x][y]+2;
       g[nsum][nnx][nny]=g[sum][x][y];
       g[nsum][nnx][nny]+=w[nx][ny];
       g[nsum][nnx][nny]+=w[nnx][nny];

       q.insert(mp(f[nsum][nnx][nny], nst)); 

      } else if (f[nsum][nnx][nny]==f[sum][x][y]+2) {
        string tmp=g[sum][x][y];
        tmp+=w[nx][ny];
        tmp+=w[nnx][nny];

        if (tmp<g[nsum][nnx][nny]) {

         int nst=code(nsum, nnx, nny);
         it=q.find(mp(f[nsum][nnx][nny], nst));
         if (it!=q.end()) q.erase(it);

         f[nsum][nnx][nny]=f[sum][x][y]+2;
         g[nsum][nnx][nny]=g[sum][x][y];
         g[nsum][nnx][nny]+=w[nx][ny];
         g[nsum][nnx][nny]+=w[nnx][nny];

         q.insert(mp(f[nsum][nnx][nny], nst)); 
         
        }

      }
     }
    }
    
   }
  }



 }


 int res=inf;
 string ans;

 need+=md;

 for (int x=0; x<n; ++x) {
  for (int y=0; y<n; ++y)
   if (res>f[need][x][y] || (res==f[need][x][y] && g[need][x][y]<ans))
    res=f[need][x][y], ans=g[need][x][y];
 }

 puts(ans.c_str());


 
}


int main() {
 freopen("c.in", "r", stdin);
 freopen("c.out", "w", stdout);

 int nt; scanf("%d", &nt);

 for (int tc=1; tc<=nt; ++tc) {

  scanf("%d %d", &n, &m); gets(w[0]);

  for (int i=0; i<n; ++i)
   gets(w[i]);

 

  printf("Case #%d:\n", tc);
  fprintf(stderr, "tc=%d\n", tc);

  for (int i=0; i<m; ++i) { 

   int sum; scanf("%d", &sum);
   solve(sum);



  }


  
 }

 return 0;
}
