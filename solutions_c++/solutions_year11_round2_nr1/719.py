#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
#define N 105
double wp[N],owp[N],oowp[N];
double sum[N],cnt[N];
double osum[N];

char ch[N][N];
int main()
{
	int t;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int g = 1;
	scanf("%d",&t);
	while(t--)
	{
		int n;
		scanf("%d",&n);
		int i,j;
		for( i = 0 ; i < n ; i ++)
				scanf("%s",ch[i]);
		printf("Case #%d:\n",g++);
		for( i = 0 ; i < n ; i ++)
		{
			cnt[i] = 0;
			sum[i] = 0;
			for(j = 0 ; j < n ; j ++)
			{
				if(ch[i][j] != '.')
				{
					cnt[i] ++;
					sum[i] += ch[i][j] - '0';
				}
			}
			wp[i] = sum[i] / cnt[i];
		}
		for( i = 0 ; i < n ; i ++)
		{
			osum[i] = 0;
			for(j = 0 ; j < n ; j ++)
			{			
				if(ch[i][j] != '.')
				{
					osum[i] += (sum[j] - (1-(ch[i][j] - '0')))/(cnt[j] - 1);
				}
			}
			owp[i] = osum[i] / cnt[i];
		}
		for( i = 0 ; i <  n ; i ++)
		{
			oowp[i] = 0;
			for(j = 0 ; j < n; j ++)
			{
				if(ch[i][j] != '.')
				{
					oowp[i] += owp[j];
				}
			}
			oowp[i] /= cnt[i];
		}
		for( i = 0 ; i <n ; i ++)
			printf("%.12lf\n",0.25 * wp[i]+ 0.50 * owp[i] + 0.25 * oowp[i]);
	}
	return 0;


}