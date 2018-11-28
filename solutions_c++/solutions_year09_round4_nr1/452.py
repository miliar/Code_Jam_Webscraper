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

char r[50];
VI e;

void solve(){
  int n; scanf("%d\n",&n);
  e.clear();
  FOR(i,n) { 
     scanf("%s",r); 
     int x=0; FOR(i,n) if(r[i]=='1') x=max(x,i+1);
     e.PB(x);
  }

  int ret=0;

  FOR(i,n){
      if(e[i]<=i+1) continue;
      int jj=0;
      FR(j,i,n) if(e[j]<=i+1) { jj=j; break; }
      while(jj!=i){
         swap(e[jj],e[jj-1]); ret++;
         jj--;
      }         
  }
  printf("%d\n",ret);
}

int main(){
  int pvs; scanf("%d\n",&pvs);
  FR(ppp,1,pvs+1){
     printf("Case #%d: ",ppp);

     solve();
  }
  return 0;
}


