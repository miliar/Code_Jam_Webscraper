#include <iostream>


using namespace std;


char s[146][146];
double owp[146], oowp[146], wp[146];
int wins[146], sum[146];


int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d", &t);
	for(int _ = 0; _ < t; _++)
	{
		int n;
		scanf("%d", &n);
		gets(s[0]);
		for(int i = 0; i < n; i++)
			gets(s[i]);
		for(int i = 0; i < n; i++)
		{
			sum[i] = 0;
			wins[i] = 0;
			for(int j = 0; j < n; j++)
				if(s[i][j] != '.')
				{
					sum[i]++;
					wins[i] += s[i][j] - '0';
				}
			wp[i] = (double)wins[i] / (double)sum[i];
		}
		for(int i = 0; i < n; i++)
		{
			double wpsum = 0;
			for(int j = 0; j < n; j++)
				if(s[i][j] != '.')
				{
					wpsum += (double)(wins[j] - s[j][i] + '0') / (double)(sum[j] - 1);
				}
			owp[i] = wpsum / (double)sum[i];
		}
		for(int i = 0; i < n; i++)
		{
			oowp[i] = 0;
			for(int j = 0; j < n; j++)
				if(s[i][j] != '.')
					oowp[i] += owp[j];
			oowp[i] /= (double)sum[i];
		}
		printf("Case #%d:\n", _ + 1);
		for(int i = 0; i < n; i++)
		{
			double ans = 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
			printf("%.9lf\n", ans);
		}
	}
}