/*
Google Codejam Round 1B
Prob Rank is pure
By Phinfinity (anish)
*/
#include<cstdio>
#define MOD 100003
int main()
{
  int ans[509];
  int a[509][509];
  int i,j,n,t;
  for(i=0;i<=502;i++)
  {
    for(j=0;j<=502;j++)
    {
      a[i][j]=0;
    }
  }
  a[0][1]=1;
  for(n=2;n<=500;n++)
  {
    ans[n]=0;
    for(i=0;i<=n;i++)
      ans[n]=(ans[n]+a[0][i])%MOD;
    i=0;
    for(j=1;j<=n;j++)
    {
      a[n-j-1][n]=(a[n-j-1][n]+a[0][j])%MOD;
    }
    for(i=1;i<n;i++)
    {
      for(j=1;j<n;j++)
      {
	a[i-1][j]=(a[i-1][j]+a[i][j])%MOD;
      }
    }
  }
  scanf("%d",&t);
  for(i=1;i<=t;i++)
  {
    scanf("%d",&n);
    printf("Case #%d: %d\n",i,ans[n]);
  }
  return 0;
}