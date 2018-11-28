#include<cstdio>
int main()
{
	int st[100][100],no[100][100],dp[100][100],a[100][100];
	int t,r,c,i,j,ca=0,fl;
	char ch,str[100];
	scanf("%d%c",&t,&ch);
	while(t--)
	{
		ca++;
		scanf("%d %d%c",&r,&c,&ch);
		for (i=1;i<=r;i++)
		{
			no[i][0] = 0;
			dp[i][0] = 1;
			scanf("%s",str);
			for (j=0;str[j]!=0;j++)
			{
				if (str[j]=='.')
					st[i][j+1] = 0;
				else
					st[i][j+1] = 1;
			}
		}
/*		for (i=1;i<=r;i++)
		{
			for (j=1;j<=c;j++)
			{
				if (st[i][j]==1)
				{
					no[i][j] = no[i][j-1] + no[i-1][j] - no[i-1][j-1] + 1;
				}
			}
		}*/
		fl = 0;
		for (i=1;i<=r;i++)
		{
			for (j=1;j<=c;j++)
			{
				if (st[i][j]==1)
				{
					if (st[i][j+1]==1 && st[i+1][j]==1 && st[i+1][j+1]==1)
					{
						st[i][j] = 2;
						st[i][j+1] = -2;
						st[i+1][j] = 3;
						st[i+1][j+1] = -3;
					}
					else
					{
						fl = 1;
						break;
					}
				}
			}
			if (fl==1)
				break;
		}
		if (fl==1)
		{
			printf("Case #%d:\n",ca);
			printf("Impossible\n");
			continue;
		}
		else
		{
			printf("Case #%d:\n",ca);
			for (i=1;i<=r;i++)
			{
				for (j=1;j<=c;j++)
				{
					if (st[i][j]==0)
						printf(".");
					else if (st[i][j]==2)
						printf("/");
					else if (st[i][j]==-2)
						printf("\\");
					else if (st[i][j]==3)
						printf("\\");
					else
						printf("/");
				}
				printf("\n");
			}
		}
	}
	return 0;
}
