#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
using namespace std;
#define MAXN 110

int n;
char mat[MAXN][MAXN];

int win_cnt[MAXN];
int loss_cnt[MAXN];

double wp[MAXN];
double owp[MAXN];
double oowp[MAXN];

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int caseN;
	scanf("%d",&caseN);
	for (int caseI=1;caseI<=caseN;caseI++)
	{
		scanf("%d",&n);
		for (int i=0;i<n;i++)
			scanf("%s",mat[i]);
		memset(win_cnt,0,sizeof(win_cnt));
		memset(loss_cnt,0,sizeof(loss_cnt));
		for (int i=0;i<n;i++)
			for (int j=0;j<n;j++)
			{
				if (mat[i][j]=='1')
					win_cnt[i]++;
				if (mat[i][j]=='0')
					loss_cnt[i]++;
			}
		for (int i=0;i<n;i++)
			wp[i]=win_cnt[i]*1.0/(win_cnt[i]+loss_cnt[i]);
		for (int i=0;i<n;i++)
		{
			owp[i]=0;
			for (int j=0;j<n;j++)
				if (mat[i][j]!='.')
				{
					int win=win_cnt[j];
					int loss=loss_cnt[j];
					if (mat[i][j]=='1')
						loss--;
					else
						win--;
					owp[i]+=win*1.0/(win+loss);
				}
			owp[i]/=win_cnt[i]+loss_cnt[i];
		}
		for (int i=0;i<n;i++)
		{
			oowp[i]=0;
			for (int j=0;j<n;j++)
				if (mat[i][j]!='.')
					oowp[i]+=owp[j];
			oowp[i]/=win_cnt[i]+loss_cnt[i];
		}
		printf("Case #%d:\n",caseI);
		for (int i=0;i<n;i++)
			printf("%.10lf\n",0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);
	}
	return 0;
}
