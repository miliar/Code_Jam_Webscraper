#include <stdio.h>
#include <string.h>
#include <memory.h>

int dp[510][20];
int flag[510][20];
char str[]="welcome to code jam";

char word[1000];
int len, no = 1;

int dfs(int pto,int ps)
{
	int i,ret=0;
	if(ps==19)return 1;
	if(pto==len)return 0;
	if(flag[pto][ps])return dp[pto][ps];
	for(i=pto;i<len;i++)if(word[i]==str[ps]){
		ret=(ret+dfs(i+1,ps+1))%10000;
	}flag[pto][ps]=1;
	return dp[pto][ps]=ret;
}

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	gets(word);
	while( t-- )
	{
		gets(word);
		len = strlen(word);
		memset(flag, 0, sizeof(flag));
		printf("Case #%d: %04d\n", no++, dfs(0, 0));
	}
	return 0;
}