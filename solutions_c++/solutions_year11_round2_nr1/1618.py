#include <stdio.h>
#define maxx 110

char map[maxx][maxx];
double ans[maxx][4],b[maxx][2];

int n;

void solve()
{
	int i,j;
	int count;
	for(i=0;i<n;i++)
	{
		b[i][0] = b[i][1] = 0;
		ans[i][0] = 0;
		count = 0;
		for(j=0;j<n;j++)
		{
			if(map[i][j] != '.')
			{
				count++;
				b[i][0]++;
				if(map[i][j] == '1')
				{
					ans[i][0] += 1;
					b[i][1]++;
				}
			}
		}
		ans[i][0] /= b[i][0];
	}
	for(i=0;i<n;i++)
	{
		ans[i][1] = 0;
		count = 0;
		for(j=0;j<n;j++)
		{
			if(map[i][j] != '.')
			{
				count++;
				if(map[i][j] == '1')
				{
					ans[i][1] += b[j][1] / (b[j][0] - 1);
				}
				else
				{
					ans[i][1] += (b[j][1] -1) / (b[j][0] - 1);
				}
			}
		}
		ans[i][1] /= count;
	}

		for(i=0;i<n;i++)
		{
			ans[i][2] = 0;
			count = 0;
			for(j=0;j<n;j++)
			{
				if(map[i][j] != '.')
				{
					count++;
					ans[i][2] += ans[j][1];
				}
			}
			ans[i][2] /= count;
		}


	for(i=0;i<n;i++)
	{
		ans[i][3] = 0.25 * ans[i][0] + 0.5 * ans[i][1] + 0.25 * ans[i][2];
	}


}

int main ()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	int T,cas,i,k;
	scanf("%d",&T);
	for(cas=1;cas<=T;cas++)
	{
		scanf("%d",&n);
		gets(map[0]);
		for(i=0;i<n;i++) gets(map[i]);
		solve();
		printf("Case #%d:\n",cas);

		for(i=0;i<n;i++)printf("%.7lf\n",ans[i][3]);

	}


}

        