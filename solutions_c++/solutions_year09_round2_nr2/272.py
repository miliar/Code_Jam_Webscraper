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

string s;
string t;

string solve(){
   char ss[50]; 
   scanf("%s\n",ss); s=ss; t=ss; sort(ALL(t));
   string ret="";
   for(int i=s.SZ-1;i>=1;i--){
      if(s[i-1]<s[i]){
         ret=s.substr(0,i-1);
         string g=s.substr(i-1); sort(ALL(g));
         FORSZ(j,g) if(g[j]>s[i-1]){
            ret+=g[j];
            ret+=g.substr(0,j);
            ret+=g.substr(j+1);
            return ret;
         }
      }
   }
//   printf("idem %s\n",t.c_str());
   FORSZ(i,t) if(t[i]!='0'){
      ret+=t[i];
      ret+="0";
      ret+=t.substr(0,i);
      ret+=t.substr(i+1);
      return ret;
   }
}

int main(){
  int pvs; scanf("%d\n",&pvs);
  FR(ppp,1,pvs+1){
     printf("Case #%d: ",ppp);

     printf("%s\n",solve().c_str());
  }
}


// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
