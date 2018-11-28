#include<iostream>
#include<string.h>

using namespace std;

int dp[200][200];
int r[20];
int c[20];
int h,w,n;

int solve()
{
  int i,j;
  cin >> h >> w >> n;
  for (i=0; i<n; i++) {
    cin >> r[i] >> c[i];
    r[i]--;
    c[i]--;
  }
  
  memset(dp, 0, sizeof(dp));
  dp[0][0]=1;

  for (i=0; i<n; i++) dp[r[i]][c[i]]=-1;

  for (i=0; i<h; i++)
    for (j=0; j<w; j++) if (dp[i][j]>=0) {
      if (0<=i-1 && 0<=j-2 && dp[i-1][j-2]>=0) dp[i][j]+=dp[i-1][j-2];
      if (0<=i-2 && 0<=j-1 && dp[i-2][j-1]>=0) dp[i][j]+=dp[i-2][j-1];
      dp[i][j]%=10007;
    }
  
  if (dp[h-1][w-1]<0) dp[h-1][w-1]=0;
  cout << dp[h-1][w-1] << endl;


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
