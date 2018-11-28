#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

char str1[600], str2[21] = {"welcome to code jam"};
int len1, len2 = 19;
int dp[600][20];

int solve(int pos1, int pos2)
{
	if(dp[pos1][pos2]) return dp[pos1][pos2];
	if(!str2[pos2]) return 1;
	if(!str1[pos1]) return 0;
	if(str1[pos1]==str2[pos2])
		dp[pos1][pos2] += solve(pos1+1,pos2+1) + solve(pos1+1,pos2);
	else dp[pos1][pos2] += solve(pos1+1,pos2);
	return dp[pos1][pos2];
}

int main()
{
	int t, x, res;
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	scanf("%d",&t);
	getchar();
	for(x=1;x<=t;x++)
	{
		gets(str1);
		len1 = strlen(str1);
		memset(dp,0,sizeof(dp));
		res = solve(0,0);
		printf("Case #%d: %04d\n",x,res);
	}
	return 0;
}
