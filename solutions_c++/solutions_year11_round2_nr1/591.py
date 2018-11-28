#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>

using namespace std;

const int maxn(105);

double ans[maxn],wp[maxn],owp[maxn],oowp[maxn];
char s[maxn];
int a[maxn][maxn],sum[maxn],win[maxn];

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int task;
	scanf("%d",&task);
	for (int cases(1);cases<=task;cases++)
	{
		int n;
		scanf("%d\n",&n);
		memset(a,0,sizeof(a));
		memset(sum,0,sizeof(sum));
		memset(win,0,sizeof(win));
		for (int i(0);i<n;i++)
		{
			gets(s);
			for (int j(0);j<n;j++)
			{
				if (s[j] == '1')
				{
					a[i][j] = 1;
					win[i]++;
				}
				else
				if (s[j] == '0')
					a[i][j] = 0;
				else
				{
					a[i][j] = -1;
					sum[i]--;
				}
				sum[i]++;
			}
			for (int i(0);i<n;i++)
			{
				wp[i] = 1.0 * win[i] / sum[i];
			}
			for (int k(0);k<n;k++)
			{
				int tot = 0;
				double sum = 0;
				for (int i(0);i<n;i++)
				if (a[i][k]!=-1)
				{
					tot = tot + 1;
					int win(0);
					int sums(0);
					for (int j(0);j<n;j++)
					if (j!=k && a[i][j] !=-1)
					{
						sums++;
						win+=a[i][j];
					}
					sum = sum + 1.0 * win / sums;
				}
				owp[k] = sum / tot;
			}
		}
		for (int i(0);i<n;i++)
		{
			double sum(0);
			int tot(0);
			for (int j(0);j<n;j++)
				if (a[i][j] != -1)
				{
					tot ++;
					sum = sum + owp[j];
				}
			oowp[i] = sum / tot;
		}
		/*for (int i(0);i<n;i++)
			cout<<owp[i]<<endl;*/
		printf("Case #%d:\n",cases);
		for (int i(0);i<n;i++)
		{
			ans[i] = 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i] + 1e-8;
			printf("%.7lf\n",ans[i]);
		}
		//for (int i(0);i<n;i+
	}
	return 0;
}
