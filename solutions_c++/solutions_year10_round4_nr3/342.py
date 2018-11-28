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


bool A[101][101];
bool B[101][101];
int n;

void solve(){
   scanf("%d",&n);
   CL(A);
   FOR(i,n){
      int x1,y1,x2,y2;
      scanf("%d %d %d %d",&x1,&y1,&x2,&y2);
      FR(x,x1,x2+1)
         FR(y,y1,y2+1) A[x][y]=true;
   }
   int ret=0;
   int poc=0;
   
   while(1){
     poc=0;
     FOR(i,101) FOR(j,101) if(A[i][j]) poc++;
     if(poc==0) break; 
     ret++;
     CL(B);
     FOR(i,101) FOR(j,101){
        if(A[i-1][j] && A[i][j-1]) B[i][j]=true; else
        if(!A[i-1][j] && !A[i][j-1]) B[i][j]=false; else
        B[i][j]=A[i][j];
     }
     memcpy(A,B,sizeof(A));
   }
   printf("%d\n",ret);
}

int main(){
  int pvs; scanf("%d",&pvs);
  FR(ppp,1,pvs+1){
     printf("Case #%d: ",ppp);

     solve();
  }
}


// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
