#include<iostream>
#include<stdio.h>
using namespace std;
char s[111][111];
double wp[111],owp[111],oowp[111],cnt[111];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t,n;
	scanf("%d",&t);
	for(int tt = 0; tt < t; tt++)
	{
		scanf("%d",&n);
		for(int i = 0; i < n; i++)
			scanf("%s",&s[i]);
		for(int i = 0; i < n; i++)
		{
			cnt[i] = 0.0;
			for(int j = 0; j < n; j++)
				if (s[i][j] != '.')
					cnt[i]++;
		}
		for(int i = 0; i < n; i++)
		{
			wp[i] = 0.0;
			for(int j = 0; j < n; j++)
				if (s[i][j] == '1') wp[i] = wp[i] + 1.0;
		}
		for(int i = 0; i < n; i++)
		{
			owp[i] = 0.0;
			for(int j = 0; j < n; j++)
			{
				if (s[i][j] == '.') continue;
				if (s[i][j] == '0') owp[i] = owp[i] + (wp[j] - 1.0) / (cnt[j] - 1.0); else owp[i] = owp[i] + wp[j] / (cnt[j] - 1.0);
			}
			owp[i] = owp[i] / cnt[i];
		}
		for(int i = 0; i < n; i++)
		{
			oowp[i] = 0.0;
			for(int j = 0; j < n; j++)
			{
				if (s[i][j] == '.') continue;
				oowp[i] = oowp[i] + owp[j];
			}
			oowp[i] = oowp[i] / cnt[i];
		}
		printf("Case #%d:\n",tt + 1);
		for(int i = 0; i < n; i++)
			printf("%.9lf\n",0.25 * wp[i] / cnt[i] + 0.5 * owp[i] + 0.25 * oowp[i]);
			                 
	}
	return 0;
}
