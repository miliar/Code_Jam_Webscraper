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

int K;
int d[5005];

int dalsi[5005];
int pred[5005];

void solve(){
   scanf("%d",&K);
   CL(d);
   FR(i,1,K) dalsi[i]=i+1; dalsi[K]=1;
   FR(i,2,K+1) pred[i]=i-1; pred[1]=K; 
   int q=1;
   FR(i,1,K){
      FOR(ee,i-1){
         q=dalsi[q];
      }
//      printf(" %d %d %d %d\n",i,q,pred[q],dalsi[q]);   
      d[q]=i;
      int x=pred[q];
      int y=dalsi[q];
      dalsi[x]=y;
      pred[y]=x;
      q=y;
   }
   d[q]=K;
   int n; scanf("%d",&n); FOR(i,n){ int x; scanf("%d",&x); printf(" %d",d[x]); }
   PN;
}

main(){
  int pvs; scanf("%d",&pvs);
  FR(ppp,1,pvs+1){
     printf("Case #%d:",ppp);

     solve();
  }
}


