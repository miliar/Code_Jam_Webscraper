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

char s[65];
int n;

void solve(){
   scanf("%s\n",s);
   n=strlen(s);
   VI q;
   for(int i=0,j=n-1;j>=0;j--,i++) if(s[j]=='?') q.PB(i);
   LL h=0;
   FOR(i,n){
      h*=2; if(s[i]=='1') h++; 
   }
   long long ret=-1;
   FOR(mask,(1<<q.SZ)){
      LL hh=h;
      FORSZ(i,q) if(mask&(1<<i)) hh+=((long long)1<<q[i]);
      LL ish=(long long)sqrt(hh);
      if(ish*ish==hh) ret=ish;
      ish++;
      if(ish*ish==hh) ret=ish;
   }
   ret*=ret;
//   printf("%lld\n",ret);
   string vy="";
   while(ret){
      if(ret%2) vy+="1"; else vy+="0";
      ret/=2;
   }
   reverse(ALL(vy));
   printf("%s\n",vy.c_str());
}

int main(){
  int pvs; scanf("%d\n",&pvs);
  FR(ppp,1,pvs+1){
     printf("Case #%d: ",ppp);

     solve();
  }
}


// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
