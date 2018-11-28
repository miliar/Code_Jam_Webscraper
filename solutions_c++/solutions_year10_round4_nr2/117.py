#include <iostream>
#include <cmath>
using namespace std;

typedef long long ll;

int P;
int M[5000];
int cost[5000];
ll dp[3000][20];

long long go(int node, int misses)
{
  ll& ans = dp[node][misses];
  if (ans != -1) return ans;
  
  if (node >= (1<<P)) return 0;
  
  //miss me?
  ans = LLONG_MAX;
  if (misses+1 <= M[node])
    ans = min(ans, go(node*2, misses+1) + go(node*2+1, misses+1));
  ans = min(ans, cost[node] + go(node*2, misses) + go(node*2+1, misses));
  return ans;
}

int main()
{
  freopen("B.in", "r", stdin);
  freopen("B.out", "w", stdout);
  
	int T; cin >> T;
	for (int tcase = 0; tcase < T; tcase++)
	{
    cin >> P;
    for (int i = 0; i < (1<<P); i++)
      cin >> M[i+(1<<P)];
    
    int idx = (1<<P);
    for (int i = 0; i < P; i++)
    {
      idx >>= 1;
      for (int j = 0; j < idx; j++)
        cin >> cost[idx+j];
    }
    
    for (int i = (1<<P)-1; i >= 0; i--)
      M[i] = min(M[i*2], M[i*2+1]);
    
    memset(dp, -1, sizeof dp);
    printf("Case #%d: %lld\n", tcase+1, go(1, 0));
	}
	
	return 0;
}
