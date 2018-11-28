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

int r[15][1<<10];
bool uz[15][1<<10];
char a[15][15];
int n,m;

int ries(int q, int mask){
   if(q==0) return 0;
   int &ret=r[q][mask];
   if(uz[q][mask]) return ret;
   uz[q][mask]=true;
   FOR(nmask,1<<m){
      if((nmask|mask)!=mask) continue;  
      bool zle=false;
      FOR(i,m) if(nmask&(1<<i)) {
         if(i>0)   if(nmask&(1<<(i-1))) zle=true;
         if(i<m-1) if(nmask&(1<<(i+1))) zle=true;
         if(a[q-1][i]=='x') zle=true;
      }
      if(zle) continue;
//      if(m==3) printf("nmask: %d\n",nmask);
      int zmask=0;
      int moje=0;
      FOR(i,m) if(nmask&(1<<i)){
         moje++;
         if(i>0)   if(nmask&(1<<i)) zmask|=(1<<(i-1));
         if(i<m-1) if(nmask&(1<<i)) zmask|=(1<<(i+1));
      }
      zmask^=((1<<m)-1);
      ret=max(ret,moje+ries(q-1,zmask));
   }
   return ret;
}

void solve(){
   scanf("%d %d",&n,&m);
   FOR(i,n) scanf("%s\n",a[i]);
   CL(r); CL(uz);
   printf("%d\n",ries(n,(1<<m)-1));
}

main(){
  int pvs; scanf("%d",&pvs);
  FR(ppp,1,pvs+1){
     printf("Case #%d: ",ppp);

     solve();
  }
}


// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
