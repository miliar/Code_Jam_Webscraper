#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <vector>
#include <cmath>
#include <cstring>
#include <string>
using namespace std;
 
typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;
typedef vector<int> VI;
typedef pair<int,int> PII;
 
#define REP(i,n) for(int i=0;i<(n);++i)
#define SIZE(c) ((int)((c).size()))
#define FOR(i,a,b) for (int i=(a); i<(b); ++i)
#define FOREACH(i,x) for (__typeof((x).begin()) i=(x).begin(); i!=(x).end(); ++i)
#define FORD(i,a,b) for (int i=(a)-1; i>=(b); --i)
#define ALL(v) (v).begin(), (v).end()
 
#define pb push_back
#define mp make_pair
#define st first
#define nd second

bool prime[1100000];
vector<LL> V;
void scase(int CID){
  LL N;
  scanf("%lld",&N);
  int result = upper_bound(V.begin(), V.end(), N) - V.begin();
  printf("Case #%d: %d\n",CID, N==1?0:result);
}
int K = 1100000;
int main(){
  FOR(i,2,K)prime[i] = true;  
  FOR(i,2,K)if(prime[i]){
    for(int j = 2*i; j<K; j+=i)prime[j] = false;
    LL x = i*(LL)i;
    while(x <= 1000000LL*1000000LL){
      V.pb(x);
      x *= i;
    }
  }
  V.pb(1);
  sort(V.begin(), V.end());
  int T;
  scanf("%d",&T);
  FOR(CID,1,T+1)scase(CID);
}
