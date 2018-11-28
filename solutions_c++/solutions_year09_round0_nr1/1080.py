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

int L,D,N;
char d[5005][25];

void solve(){
   char r[1000]; scanf("%s\n",r);
   set<char> p[L];
   bool z=false;
   int q=0;
   for(int i=0;r[i]!='\0';i++){
      if(r[i]=='(') z=true; else
      if(r[i]==')') { z=false; q++; } else{
         p[q].insert(r[i]); 
         if(!z) q++;
      }
   }

   int ret=0;
   FOR(i,D){
      int ok=1;
      FOR(q,L) if(!p[q].count(d[i][q])) { ok=0; break; }
      ret+=ok;
   }
   printf("%d\n",ret);
}

int main(){
  scanf("%d %d %d",&L,&D,&N);
  FOR(i,D){ scanf("%s\n",d[i]); } 

  int pvs=N; 
  FR(ppp,1,pvs+1){
     printf("Case #%d: ",ppp);
     solve();
  }
}


// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
