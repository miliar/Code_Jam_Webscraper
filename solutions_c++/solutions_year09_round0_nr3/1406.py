#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;

#define FR(i,a,b) for(int i=(a);i<(b);++i)
#define FOR(i,n) FR(i,0,n)
#define CLR(x,a) memset(x,a,sizeof(x))
#define setmin(a,b) a = min(a,b)

const int MOD = 10000;
const char *s = "welcome to code jam";
const int len = 19;

char buf[512];
int dp[501];

int cas=0;
void doit() {
  scanf("%[^\n] ",buf);

  CLR(dp,0);
  int L = strlen(buf);
  dp[L] = 1;

  for (int i = len-1; i >= 0; --i) {
    int tot = 0;
    for (int j = L; j >= 0; --j) {
      int oldtot = tot;
      tot = (tot+dp[j])%MOD;

      dp[j] = oldtot * (s[i] == buf[j]);
    }
  }

  int ans = 0;
  FOR(i,L+1) {
    ans = (ans+dp[i])%MOD;
  }

  printf("Case #%d: %04d\n", ++cas, ans);
}

int N;
int main() {
  scanf("%d ",&N);
  FOR(i,N) doit();
}
