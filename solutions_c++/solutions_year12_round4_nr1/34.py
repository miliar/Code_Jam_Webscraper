#include<cstdio>
#include<cstring>
#include<algorithm>

using namespace std;

typedef long long Int;

int dp[10050][10050];

int N;
Int a[10050], b[10050], D;

inline bool ok(int i, int j, int k)
{
  return min(a[i] + (a[j]-a[i])*2, a[j]+b[j]) >= a[k];
}

int main()
{
  int T;
  scanf("%d", &T);
  
  for(int CN=1; CN<=T; ++CN) {
    scanf("%d", &N);
    for(int i=1; i<=N; ++i)
      scanf("%lld%lld", &a[i], &b[i]);
    scanf("%lld", &D);
    
    a[0] = b[0] = 0;
    memset(dp, 0, sizeof(dp));
    dp[0][1] = 1;
    bool res = false;
    int cnt = 0;
    for(int i=0; i<=N; ++i) {
      if(i > 0)
        for(int j=1; j<=N; ++j)
          dp[i][j] += dp[i][j-1];
      for(int j=i+1; j<=N; ++j) {
        if(!dp[i][j]) continue;
        if(min(a[i] + (a[j]-a[i])*2, a[j]+b[j]) >= D) res = true;
        int lo = j+1, hi = N+1;
        if(!ok(i, j, j+1)) continue;
        while(hi-lo>1) {
          cnt++;
          int mid = (hi+lo)/2;
          if(ok(i, j, mid)) lo = mid;
          else hi = mid;
          if(cnt % 100000000 == 0) fprintf(stderr, "hoge\n");
        }
        dp[j][j+1]++;
        dp[j][lo+1]--;
      }
    }
    
    fprintf(stderr, "Case #%d\n", CN);
    printf("Case #%d: ", CN);
    puts(res ? "YES" : "NO");
  }
  
  return 0;
}
