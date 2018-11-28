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
using namespace std;
typedef long long LL;
///////////////////////////////////////////////////////////////////////////////////
// }}}

int n, k;

void solve(){
   scanf("%d %d",&n,&k);
   int M=(1<<n);
   if(k%M==M-1) printf("ON\n"); else printf("OFF\n");
}

int main(){
  int pvs; scanf("%d",&pvs);
  FR(ppp,1,pvs+1){
     printf("Case #%d: ",ppp);
     solve();
  }
}


// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
