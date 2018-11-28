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
char s[105][105];
int a[105],b[105];
double wp[105],owp[105];


double WP(int x){
   FOR(i,n) if(s[x][i]=='0') b[x]++; else if(s[x][i]=='1') a[x]++;
   return (double)a[x]/(double)(a[x]+b[x]);
}

double OWP(int x){
   int k=0;
   double ret=0.0;
   FOR(i,n) if(s[x][i]!='.'){
      k++;
      int aa=a[i],bb=b[i];
      if(s[x][i]=='1') bb--; else aa--;
      ret+=(double)aa/(aa+bb);
   }
   return ret/k;
}

double OOWP(int x){
   int k=0;
   double ret=0.0;
   FOR(i,n) if(s[x][i]!='.'){
      k++;
      ret+=owp[i];
   }
   return ret/k;
}

void solve(){
   CL(a); CL(b);
   scanf("%d\n",&n);
   FOR(i,n) scanf("%s\n",s[i]);
   FOR(i,n) wp[i]=WP(i);
//   FOR(i,n) printf("%.5lf ",wp[i]); PN;
   FOR(i,n) owp[i]=OWP(i);
//   FOR(i,n) printf("%.5lf ",owp[i]); PN; 
//   FOR(i,n) printf("%.5lf ",OOWP(i)); PN;
   PN;
   FOR(i,n) printf("%.9lf\n", 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * OOWP(i));
}

int main(){
  int pvs; scanf("%d\n",&pvs);
  FR(ppp,1,pvs+1){
     printf("Case #%d: ",ppp);

     solve();
  }
}


// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
