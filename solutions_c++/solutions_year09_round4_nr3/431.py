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

int n,m;
VI e[50];
bool a[20][20];
int r[(1<<16)+5];


bool moze(VI a, VI b){
   if(a[0]>b[0]) swap(a,b);
   FORSZ(i,a){
      if(a[i]<b[i]) ; else return false;
   }  
   return true;
}

int bitcnt(int mask){
   int ret=0;
   while(mask>0){ if(mask&1) ret++; mask>>=1; }
   return ret;
}

int ries(int mask){
   if(mask==0) return 0;
   int &ret=r[mask];
   if(ret) return ret;
   if(bitcnt(mask)==1) return ret=1;

   if(bitcnt(mask)==2){
       VI w; FOR(i,n) if(mask&(1<<i)) w.PB(i);      
       if(a[w[0]][w[1]]) return ret=1;
       return ret=2;
   }
/*   
   if(bitcnt(mask)==3){
      VI w; FOR(i,n) if(mask&(1<<i)) w.PB(i);
      int okk=0;
      FORSZ(i,w) FOR(j,i) if(a[i][j]) okk++;
      if(okk==3) return ret=1;
      if(okk) return ret=2;
      return ret=3;
   }
*/


   ret=100;
   int k=bitcnt(mask);
   int koniec=(1<<k);
   for(int mm=1;mm<koniec;mm+=2){
      VI w;
      int j=0;
      int nm=0;
      bool ok=true;
      FOR(i,n) if(mask&(1<<i)){  
         if(mm&(1<<j)) { 
             nm+=(1<<i);
             FORSZ(ii,w) if(!a[w[ii]][i]) { ok=false; break; }
             w.PB(i);
         }         
         if(!ok) break;
         j++;  
      }

      //      FORSZ(i,w) FOR(j,i) if(!a[w[i]][w[j]]) { ok=false; break; }
      if(ok) ret=min(ret,1+ries(mask-nm));
   }
   return ret;
}

void solve(){
  scanf("%d %d",&n,&m);
  FOR(i,n){
     e[i].clear();
     FOR(j,m) { int x; scanf("%d",&x); e[i].PB(x); }
  }
  FOR(i,n) FOR(j,n) if(moze(e[i],e[j])) a[i][j]=true; else a[i][j]=false;
//  FOR(i,n) { FOR(j,n) printf("%d",a[i][j]); PN; }
  CL(r);
  printf("%d\n",ries((1<<n)-1));
}

int main(){
  int pvs; scanf("%d",&pvs);
  FR(ppp,1,pvs+1){
     printf("Case #%d: ",ppp);

     solve();
  }
}


// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
