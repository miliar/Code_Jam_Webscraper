
#include <algorithm>
#include <cstdio>
#include <cstring>

using namespace std;

const int MAXN = 10000;

int d[MAXN], l[MAXN];
int D;

int dp[MAXN];

int main()
{
  int T;
  scanf("%d", &T);

  for (int case_id = 1; case_id <= T; case_id++)
  {
    int N;
    scanf("%d", &N);
    for (int i = 0; i < N; i++)
      scanf("%d %d", &d[i], &l[i]);
    scanf("%d", &D);

    memset(dp, 0, sizeof(dp));
    
    dp[0] = d[0];
    for (int i = 0; i < N-1; i++)
    {
      for (int j = i+1; j < N && d[j]-d[i] <= dp[i]; j++)
      {
	dp[j] = min(l[j], max(dp[j], d[j]-d[i]));
      }
    }

    bool ok = false;
    for (int i = 0; i < N; i++)
    {
      if (d[i] + dp[i] >= D)
      {
	ok = true;
	break;
      }
    }

    printf("Case #%d: %s\n", case_id, ok ? "YES" : "NO");
  }
}
