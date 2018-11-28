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

map<int,int> o;
set<int> r;  
int ret;
int n;

int vloz(int x, int y){
   o[x]+=y;
   if(o[x]>=2) r.insert(x);   
}

int vyber(int x){
   o[x]-=2; 
   ret++;
   vloz(x-1,1);
   vloz(x+1,1);
   if(o[x]<=1) r.erase(x);
}

void solve(){
  scanf("%d",&n);
  o.clear(); r.clear(); ret=0;
  FOR(i,n){
     int x,y;
     scanf("%d %d",&x,&y);
     vloz(x,y);
  }
  while(!r.empty()){
      int x=*r.begin();
      vyber(x);
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
