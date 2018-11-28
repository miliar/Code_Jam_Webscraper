// pre-written code {{{
#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>
#include <numeric>
#include <iostream>
#include <cassert>
#include <set>
#define FOR(i,n) for(int _n=n,i=0;i<_n;++i)
#define FR(i,a,b) for(int _b=b,i=a;i<_b;++i)
#define CL(x) memset(x,0,sizeof(x))
#define PN printf("\n");
#define MP make_pair
#define PB push_back
#define SZ size()
#define ALL(x) x.begin(),x.end()
#define FORSZ(i,v) FOR(i,v.size())
#define FORIT(it,x) for(__typeof(x.begin()) it=x.begin();it!=x.end();it++)
using namespace std;
typedef vector<int> VI;
typedef vector<string> VS;
typedef long long LL;
///////////////////////////////////////////////////////////////////////////////////
// }}}

int dx[]={-1,0,0,+1};
int dy[]={0,-1,+1,0};

int n,m;
int a[105][105];
int f[105][105];
char w[105][105];

inline bool dnu(int x, int y){ return (0<=x && x<n && 0<=y && y<m); }

void kam(int x, int y, int &xxx, int &yyy){
   xxx=x; yyy=y;
   int naj=a[x][y];
   FOR(i,4){
      int xx=x+dx[i];
      int yy=y+dy[i];
      if(!dnu(xx,yy)) continue;
      if(naj>a[xx][yy]){ naj=a[xx][yy]; xxx=xx; yyy=yy; }
   }   
}

int ries(int x, int y){
   if(f[x][y]!=(x*m+y)) return f[x][y]; 
   int xxx,yyy; kam(x,y,xxx,yyy);
   if(x==xxx && y==yyy) return f[x][y];
   return f[x][y]=ries(xxx,yyy);
}


void solve(){
   scanf("%d %d",&n,&m);
   FOR(i,n) FOR(j,m) scanf("%d",&a[i][j]);
   FOR(i,n) FOR(j,m) f[i][j]=(i*m+j);

   char c='a';
   map<int,char> z;
   FOR(i,n){
      FOR(j,m) {
         int r=ries(i,j);
         if(!z.count(r)) { z[r]=c; c++; }
         if(j) printf(" ");
         printf("%c",z[r]);
      }
      PN;
   }

}

int main(){
  int pvs; scanf("%d",&pvs);
  FR(ppp,1,pvs+1){
     printf("Case #%d:\n",ppp);

     solve();
  }
}


// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
