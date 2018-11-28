/*#include<stdio.h>
#include<string.h>
struct search
{
	char ss[105];
}sear[105];
struct query
{
	char qq[105];
}que[1005];
int main()
{
	int ca, s, q, i, j, pos, c = 1;
	int dp[1005][105], num[105];
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &ca);
	while(ca --)
	{
		scanf("%d", &s);
		getchar();
		for(i=0; i<s; i++)
		{
			gets(sear[i].ss);
		}
		scanf("%d", &q);
		getchar();
		for(i=0; i<q; i++)
		{
			gets(que[i].qq);
		}
		if(q == 0)
		{
			printf("Case #%d: 0\n", c++);
			continue;
		}
		memset(dp, 0, sizeof(dp));
		memset(num, 0, sizeof(num));
		for(i=0; i<s; i++)
		{
			if(strcmp(que[0].qq, sear[i].ss) != 0)
			{
				dp[0][i] = 1;
			}
			else
			{
				pos = i;
			}
		}
		int leap = 0;
		for(i=1; i<q; i++)
		{
			for(j=0; j<s; j++)
			{
				if(strcmp(que[i].qq, sear[j].ss) == 0)
				{
					if(j != pos)
					{
						num[j] ++;
						if(leap == 0)
						{
							dp[i][pos] = 1;
							num[pos] ++;
							leap = 1;
						}
					}
					else if(leap == 1)
					{
						num[j] ++;
					}
				}
				else
				{
					if(leap == 1)
						dp[i][j] = 1;
				}
			}
		}
		int min = 1000000;
		for(i=0; i<s; i++)
		{
			if(num[i] < min)
			{
				min = num[i];
			}
		}
		printf("Case #%d: %d\n", c++, min);
	}
	return 0;
}*/
#include<stdio.h>
#include<string.h>
struct search
{
	char ss[105];
}sear[105];
struct query
{
	char qq[105];
}que[1005];
int main()
{
	int s, q, t, ca = 1, i, j, k, min;
	int dp[1005][105];
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &t);
	while(t --)
	{
		scanf("%d", &s);
		getchar();
		for(i=0; i<s; i++)
		{
			gets(sear[i].ss);
		}
		scanf("%d", &q);
		getchar();
		for(i=0; i<q; i++)
		{
			gets(que[i].qq);
		}
		if(q == 0)
		{
			printf("Case #%d: 0\n", ca++);
			continue;
		}
		for(i=0; i<q; i++)
		{
			for(j=0; j<s; j++)
			{
				dp[i][j] = 9999999;
			}
		}
		for(i=0; i<s; i++)
		{
			if(strcmp(sear[i].ss, que[0].qq) != 0)
			{
				dp[0][i] = 0;
			}
		}
		for(i=1; i<q; i++)
		{
			for(j=0; j<s; j++)
			{
				if(strcmp(que[i].qq , sear[j].ss) != 0)
				{
					if(dp[i-1][j] != 9999999)
					{
						dp[i][j] = dp[i-1][j];
					}
					else if(dp[i-1][j] == 9999999)
					{
						min = 999999;
						for(k=0; k<s; k++)
						{
							if(k != j)
							{
								if((dp[i-1][k] + 1) < min)
								{
									min = dp[i-1][k] + 1;
								}
							}
						}
						dp[i][j] = min;
					}
				}

			}
		}
		min = 999999;
		for(i=0; i<s; i++)
		{
			if(dp[q-1][i] < min)
			{
				min = dp[q-1][i];
			}
		}
		printf("Case #%d: %d\n", ca++, min);
	}

	return 0;
}