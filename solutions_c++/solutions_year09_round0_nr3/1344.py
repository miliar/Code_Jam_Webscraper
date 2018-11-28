#include<string.h>
#include<stdio.h>

char s[504];

int dp[504][20];

void trans(int i)
{
	int j;
	for(j=0;j<=18;j++)
		dp[i][j] = dp[i-1][j];
	if(s[i] == 'w')
		dp[i][0]++;
	if(s[i] == 'e')
		dp[i][1] += dp[i-1][0];
	if(s[i] == 'l')
		dp[i][2] += dp[i-1][1];
	if(s[i] == 'c')
		dp[i][3] += dp[i-1][2];
	if(s[i] == 'o')
		dp[i][4] += dp[i-1][3];
	if(s[i] == 'm')
		dp[i][5] += dp[i-1][4];
	if(s[i] == 'e')
		dp[i][6] += dp[i-1][5];
	if(s[i] == ' ')
		dp[i][7] += dp[i-1][6];
	if(s[i] == 't')
		dp[i][8] += dp[i-1][7];
	if(s[i] == 'o')
		dp[i][9] += dp[i-1][8];
	if(s[i] == ' ')
		dp[i][10] += dp[i-1][9];
	if(s[i] == 'c')
		dp[i][11] += dp[i-1][10];
	if(s[i] == 'o')
		dp[i][12] += dp[i-1][11];
	if(s[i] == 'd')
		dp[i][13] += dp[i-1][12];
	if(s[i] == 'e')
		dp[i][14] += dp[i-1][13];
	if(s[i] == ' ')
		dp[i][15] += dp[i-1][14];
	if(s[i] == 'j')
		dp[i][16] += dp[i-1][15];
	if(s[i] == 'a')
		dp[i][17] += dp[i-1][16];
	if(s[i] == 'm')
		dp[i][18] += dp[i-1][17];
	for(j=0;j<=18;j++)
		dp[i][j] = dp[i][j] %10000;
}

int main(void)
{
	freopen("E:\\C-small.in","r",stdin);
	freopen("E:\\C-small.txt","w",stdout);
	int n;
	scanf("%d",&n);
	getchar();
	int i;
	for(i=1;i<=n;i++)
	{
		memset(dp,0,sizeof(dp));
		gets(s);
		int j;
		int len = strlen(s);
		if(s[0] == 'w')
			dp[0][0] = 1;
		for(j=1;j<len;j++)
		{
			trans(j);
		}
		printf("Case #%d: %04d\n",i,dp[len-1][18]);
	}
	return 0;
}
				
