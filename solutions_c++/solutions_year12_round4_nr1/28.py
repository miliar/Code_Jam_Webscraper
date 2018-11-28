/* Writen by Filip Hlasek 2012 */
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <cmath>
#include <cstring>

#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
#define REP(i,b) for(int i=0;i<b;i++)

using namespace std;

#define MAXN 11111
int d[MAXN], l[MAXN], N, dp[MAXN];

int main(int argc, char *argv[]){
  int T;
  scanf("%d",&T); 
  REP(t,T){
    printf("Case #%d: ", t+1);
    scanf("%d",&N);
    REP(i,N) scanf("%d%d",d+i,l+i);
    scanf("%d",d+N);
    l[N] = 1;
    REP(i,N+1) dp[i] = 0;
    dp[0] = d[0];
    REP(i,N) for(int j = i + 1; j <= N; j++){
      if(d[j] > d[i] + dp[i]) break;
      dp[j] = max(dp[j], min(l[j], d[j] - d[i]));
    }
    if(dp[N]) printf("YES\n");
    else printf("NO\n");
  }
  return 0;
}
