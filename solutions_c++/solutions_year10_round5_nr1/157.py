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

int n;
int d;
int maxi;
int b[1000000];
VI p;
int s[100];

void solve(){
   scanf("%d %d",&d,&n);
   int least=0;
   FOR(i,n) scanf("%d",&s[i]);
   FOR(i,n) least=max(least,s[i]+1);
   if(n==1) { printf("I don't know.\n"); return; }
   int maxi=1; FOR(i,d) maxi*=10;
   set<int> ret;   
   FORSZ(i,p){
      if(p[i]>=maxi) break;
      if(p[i]<least) continue;
      //treba urcit A,B
      FR(A,0,p[i]){
         int B=(s[1]-(A*s[0])%p[i]+2*p[i])%p[i];
//         if( (s[0]*A+B)%p[i]!=s[1]) printf("ZLE %d %d %d\n",A,B,p[i]);
         int ss=s[0];
         bool ok=true;
         FOR(j,n){            
            if(s[j]!=ss) { ok=false; break; }
            ss*=A; ss+=B; ss%=p[i];
         }
         if(ok) ret.insert(ss);
      }         
   }
   if(ret.SZ>1 || ret.SZ==0) printf("I don't know.\n"); else printf("%d\n",*ret.begin());
}

int main(){
  CL(b);
  b[0]=b[1]=true;  
  FR(i,2,10000) if(!b[i])
     for(int j=i+i;j<1000000;j+=i) b[j]=true;
  p.clear();
  FOR(i,10000) if(!b[i]) p.PB(i);
  int pvs; scanf("%d",&pvs);
  FR(ppp,1,pvs+1){
     printf("Case #%d: ",ppp);

     solve();
  }
}


// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
