#include<iostream>
#include<string.h>

using namespace std;

int v[200000];
int g[200000];
int c[200000];

int dp[200000][2];
int n,m;

int process(int x, int d)
{
  int i,j,k;
  for (i=0; i<=1; i++) if (dp[x*2][i]>=0)
    for (j=0; j<=1; j++) if (dp[x*2+1][j]>=0) {
      if (g[x]) k=i&&j;
      else k=i||j;
      if (dp[x][k]<0 || dp[x][k]>dp[x*2][i]+dp[x*2+1][j])
	dp[x][k]=dp[x*2][i]+dp[x*2+1][j]+d;
    }

  return 0;
}

int solve()
{
  int i;

  cin >> n >> m;
  memset(v, 0, sizeof(v));
  memset(g, 0, sizeof(g));
  memset(c, 0, sizeof(c));
  memset(dp, 0xff, sizeof(dp));
  for (i=1; i<=(n-1)/2; i++) cin >> g[i] >> c[i];

  for (i=(n-1)/2+1; i<=n; i++) {
    cin >> v[i];
    dp[i][v[i]]=0;
  }
  
  for (i=(n-1)/2; i>=1; i--) {
    process(i, 0);
    if (c[i]) {
      g[i]=1-g[i];
      process(i, 1);
    }
    
  }

  if (dp[1][m]<0) cout << "IMPOSSIBLE" <<endl;
  else cout << dp[1][m] << endl;

  return 0;
}

main()
{
  int t, c=0;
  cin >> t;
  while (t--) {
    cout << "Case #" << ++c << ": ";
    solve();
  }
  return 0;
}
