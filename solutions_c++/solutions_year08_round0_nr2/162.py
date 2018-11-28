#include <cstdio>
#include <cmath>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>
#include <numeric>
#include <iostream>
#include <cassert>
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


int T;
int n,m;

const int maxi=60*24+65;
int f[maxi],g[maxi];


int ries(int *f){
   int poc=0;
   int ret=0;
   FOR(i,maxi){
      ret=min(ret,poc+f[i]);      
      poc+=f[i];
   }
   return -ret;
}

void solve(){
   scanf("%d",&T);
   scanf("%d %d",&n,&m);
   CL(f); CL(g);
   int a,b,c,d;
   FOR(i,n){ scanf("%d:%d %d:%d",&a,&b,&c,&d); f[60*a+b]--; g[60*c+d+T]++; }
   FOR(i,m){ scanf("%d:%d %d:%d",&a,&b,&c,&d); g[60*a+b]--; f[60*c+d+T]++; }
   printf(" %d %d\n",ries(f),ries(g));
}

main(){
  int pvs; scanf("%d",&pvs);
  FR(ppp,1,pvs+1){
     printf("Case #%d:",ppp);

     solve();
  }
}


