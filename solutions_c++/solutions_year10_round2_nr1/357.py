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


VS split(string s, string delim="/") {
  s += delim[0];
  string w; VS res;
  FORIT(it,s) {
    if(find(delim.begin(),delim.end(),*it)==delim.end()) {
      w += *it;
    } else {
      if(w!="") res.push_back(w);
      w="";
    }
  }
  return res;
}

int n,m;
set<VS> je;

void solve(){
   int ret=0;
   je.clear();
   scanf("%d %d\n",&n,&m);
   char r[100000];
   VS empty;
   je.insert(empty);
   FOR(i,n) { scanf("%s",r); VS e=split(r); je.insert(e); }
   FOR(mmm,m){
      scanf("%s",r);
      VS e=split(r);
      while(1){
         if(je.SZ==0) break;
         if(je.count(e)) break;
         ret++;
         je.insert(e);
         e.pop_back();
      }
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
