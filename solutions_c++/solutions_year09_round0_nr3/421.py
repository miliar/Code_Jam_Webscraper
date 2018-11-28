// pc.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"
#include "cstdio"
#include "cstring"
#include "memory.h"

struct ty 
{
	int len;
	int loc[500];
};

ty c[27];
char ch[501];
char dic[] = {"welcome to code jam"};
int len;
int dp[19][500];

int srch(int t,int p)
{
	if (dp[t][p] >= 0)
		return dp[t][p];

	if (t == 18)
	{
		dp[t][p] = 1;
		return 1;
	}

	int ret = 0;
	int k = dic[t] - 'a';
	k = k >= 0 && k < 26 ? k : 26;
	int j = dic[t+1] - 'a';
	j = j >= 0 && j < 26 ? j : 26;

	for (int i = 0; i < c[j].len; i++)
	{
		if (c[k].loc[p] < c[j].loc[i])
		{
			ret += srch(t+1,i); 
		}
	}
	ret %= 10000;
	dp[t][p] = ret;
	return ret;
}

int main()
{
//	freopen("e:\\C-large.in","r",stdin);
//	freopen("a.txt","w",stdout);
	
	int n;
	int i,j;

	scanf("%d",&n);
	getchar();
	for (int z = 1; z <= n; z++)
	{
		printf("Case #%d: ",z);
		int ans = 0;

		gets(ch);
		//printf("%s\n",ch);
		len = strlen(ch);

		for (i = 0; i < 27; i++)
			c[i].len = 0;

		for (i = 0; i < len; i++)
		{
			j = ch[i] - 'a';
			j = j >= 0 && j < 26 ? j : 26;

			c[j].loc[c[j].len++] = i;
		}

		for (i = 0; i < 19; i++)
			for (j = 0; j < 500; j++)
				dp[i][j] = -1;

		j = 'w' - 'a';
		for (i = 0; i < c[j].len; i++)
			ans += srch(0,i);

		ans %= 10000;
		printf("%04d\n",ans);
	}
	return 0;
}

