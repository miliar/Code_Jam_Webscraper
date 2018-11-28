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
const int MAXI=10005;
int d[MAXI],l[MAXI],v[MAXI];
int D;

void solve(){
  scanf("%d\n",&n);
  FOR(i,n) scanf("%d %d",&d[i],&l[i]);
  scanf("%d",&D);
  FOR(i,n) v[i]=0;
  v[0] = d[0];
  int i=0;
  int j=0;
  while(1){    
//    FOR(x,n) printf(" %d",v[x]); PN;
    //ci sa z i-tej da doskocit na j-tu..
    if(j<n && (d[i]+v[i]>=d[j])){
      //da sa doskocit..
      v[j] = max(v[j], min(d[j]-d[i], l[j]));
      j++;
    } else {
      //neda sa doskocit..
      i++;
    }
    if(i>j) break;
  }
//  FOR(i,n) printf(" %d",v[i]); PN;
  bool ret=false;
  FOR(i,n) if(d[i] + v[i] >=D) ret=true;
  printf("%s\n",ret?"YES":"NO");
}

int main(){
  int pvs; scanf("%d",&pvs);
  FR(ppp,1,pvs+1){
     printf("Case #%d: ",ppp);

     solve();
  }
}


// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
