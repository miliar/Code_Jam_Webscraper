#include<algorithm>
#include<cstdio>
#include<vector>
#include<cmath>
#include<cstring>
#define INF 2000000000
#define REP(i,n) for(int i = 0; i < (n); i++)
#define FOR(i, a, b) for(int i = (a); i < (b); i++)
#define FORD(i, a, b) for(int i = (a); i >= (b); i--)
#define PI pair<int, int>
#define ST first
#define ND second
#define CLR(a, b) memset(a, b, sizeof(a))
#ifdef DEBUG
  #define DBG printf
#else
  #define DBG 
#endif
using namespace std;

int A, B;

int main(){
  int n, t, s, p, x;
  scanf("%d",&t);
  int casenum = 0;
  while(t--){
    casenum ++;
    A = 0; B = 0;
    scanf("%d %d %d",&n, &s, &p);
    REP(i, n){
      scanf("%d",&x);
      if( x == 0){
        if(p == 0)A++;
        continue;
      }
      if( x >= 3*p - 2) A++;
      else if ( x >= 3*p - 4 ) B++;
    }
    printf("Case #%d: %d\n",casenum, A + min(B, s));
  }
  return 0;
}
