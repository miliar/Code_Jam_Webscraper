#include <iostream>
#include <sstream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <queue>
#include <set>
#include <vector>
#include <map>
#include <algorithm>

typedef long long ll;
using namespace std;

const int LIM = 10000;
int dp[LIM+2];

int main()
{
  freopen("B.in", "r", stdin);
  freopen("B.out", "w", stdout);
  
	int n_cases; cin >> n_cases;
	for (int tcase = 1; tcase <= n_cases; tcase++)
	{
    ll L; int N; cin >> L >> N;
    int a[111];
    for (int i = 0; i < N; i++)
      cin >> a[i];
    sort(a, a+N);
      
    memset(dp, 0x7f, sizeof dp);
    dp[0] = 0;
    int mx = min(LIM*1LL, L);
    ll best = LLONG_MAX;
    
    for (int i = 0; i <= mx; i++)
      if (dp[i] <= LIM)
      {
        for (int j = 0; j < N && i+a[j] <= LIM; j++)
          if (dp[i]+1 < dp[i+a[j]])
            dp[i+a[j]] = dp[i]+1;
            
          for (int j = N-1; j >= 0; j--) {
            if ((L-i)%a[j] == 0)
            {
              best = min(best, dp[i] + (L-i)/a[j]);
              break;
            }
          }
      }
	
		printf("Case #%d: ", tcase);
		if (best == LLONG_MAX)
      puts("IMPOSSIBLE");
    else
      printf("%lld\n", best);
	}

	return 0;
}