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

int c,d,n;
char s[105];
map<pair<char,char>,char> combine;
set<pair<char,char> > opposed;
vector<char> ret;
map<char,int> poc;

void solve(){
   combine.clear();
   opposed.clear();
   scanf("%d",&c);
   FOR(i,c) {
      scanf("%s",s);
      combine[MP(s[0],s[1])]=s[2];
      combine[MP(s[1],s[0])]=s[2];
   }
   scanf("%d",&d);
   FOR(i,d){
      scanf("%s",s);
      opposed.insert(MP(s[0],s[1]));
      opposed.insert(MP(s[1],s[0]));
   }
   scanf("%d",&n);
   ret.clear();
   poc.clear();
   scanf("%s\n",s);
   FOR(i,n){
      poc[s[i]]++;
      ret.PB(s[i]);
      if(ret.SZ>=2){
         char x=ret[ret.SZ-2];
         char y=ret[ret.SZ-1];
         if(combine.count(MP(x,y))) {
            poc[ret[ret.SZ-1]]--;
            poc[ret[ret.SZ-2]]--;
            ret.pop_back();
            ret.pop_back();
            ret.PB(combine[MP(x,y)]);
            poc[combine[MP(x,y)]]++;
         }
      }
      FORIT(it,opposed){
         if(poc[it->first]) if(poc[it->second]) {
            poc.clear();
            ret.clear();
         }
      }
   }
   printf("[");
   FORSZ(i,ret){
      if(i) printf(", ");
      printf("%c",ret[i]);
   }
   printf("]"); PN;
}

int main(){
  int pvs; scanf("%d",&pvs);
  FR(ppp,1,pvs+1){
     printf("Case #%d: ",ppp);

     solve();
  }
}


// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
