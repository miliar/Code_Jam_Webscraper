#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>

using namespace std;

int n;
char table[100][100];
int sum[100];
int win[100];

long double owp[100];

int main()
{
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; i++)
	{
		scanf("%d\n", &n);
		for(int j =0; j < n; j++) scanf("%s", table[j]);

		for(int j =0; j < n; j++)
		{
			sum[j]=0; win[j]=0;
			for(int k=0;k<n;k++)
			{
				sum[j] += (table[j][k] != '.');
				win[j] += (table[j][k] == '1');
			}
		}
		for(int j=0;j<n;j++)
		{
			owp[j] = 0.;
			for(int k=0;k<n;k++) if(table[k][j] != '.')
			{
				int curplay = sum[k] - 1;
				int curwin = win[k] - (table[k][j] == '1');
				owp[j] += (long double)curwin/(long double)curplay;
			}
			owp[j] /= (long double)sum[j];
		}
		printf("Case #%d:\n", i);
		for(int j = 0;j <n;j++)
		{
			long double oowp = 0.;
			for(int k=0;k<n;k++) if(table[j][k] != '.') oowp += owp[k];
			oowp /= (long double)sum[j];
			printf("%.12Lf\n", (long double)(0.25 * ((long double)win[j]/sum[j]) + 0.5 * owp[j] + 0.25 * oowp));
		}
	}
	return 0;
}
