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

int m;
int V;
int op[10005];
int ch[10005];
int maxi=987654321;
int r[10005][2];


int operacia(int x, int y, int typ){
   if(typ==1) return x&y; else return x|y;
}

int ries(int q, int v){
   int &ret=r[q][v];
   if(ret!=-1) return ret;
   if(q>(m-1)/2) { if(op[q]==v) return 0; else return maxi; }
   ret=maxi;
   FOR(i,2) FOR(j,2){
      int r1=ries(q+q,i);
      int r2=ries(q+q+1,j);
      if(r1==maxi || r2==maxi) continue;
      if(operacia(i,j,op[q])==v) ret=min(ret,r1+r2);
      if(ch[q]) 
      if(operacia(i,j,1-op[q])==v) ret=min(ret,r1+r2+1);
   }
   return ret;
}

void solve(){
   scanf("%d %d",&m,&V);
   FR(i,1,m+1){
      if(i<=(m-1)/2){
        scanf("%d %d",&op[i],&ch[i]);       
      } else scanf("%d",&op[i]);
   }
   FOR(i,m+1) FOR(j,2) r[i][j]=-1;
   int ret=ries(1,V);
   if(ret==maxi) printf(" IMPOSSIBLE\n"); else printf(" %d\n",ret);
}

main(){
  int pvs; scanf("%d",&pvs);
  FR(ppp,1,pvs+1){
     printf("Case #%d:",ppp);

     solve();
  }
}


