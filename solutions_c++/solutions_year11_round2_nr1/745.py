#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
int t,n,w[110],sum[110];
double wp[110],owp[110],oowp[110],rpi[110];
char s[110][110];

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&t);
	for (int tt=1;tt<=t;tt++)
	{
		scanf("%d",&n);
		for (int i=0;i<n;i++)
			scanf("%s",s[i]);
		for (int i=0;i<n;i++)
		{
			w[i]=sum[i]=0;
			for (int j=0;j<n;j++)
				if (s[i][j]!='.')
				{
					sum[i]++;
					if (s[i][j]=='1') w[i]++;
				}
			wp[i]=w[i]*1.0/sum[i];
		}
		for (int i=0;i<n;i++)
		{
			double ss=0;
			for (int j=0;j<n;j++)
				if (s[i][j]!='.')
					if (s[i][j]=='1')
						ss+=w[j]*1.0/(sum[j]-1);
					else ss+=(w[j]-1)*1.0/(sum[j]-1);
			owp[i]=ss/sum[i];
		}
		for (int i=0;i<n;i++)
		{
			double ss=0;
			for (int j=0;j<n;j++)
				if (s[i][j]!='.')
					ss+=owp[j];
			oowp[i]=ss/sum[i];
		}
		for (int i=0;i<n;i++)
			rpi[i]=0.25*wp[i]+0.50*owp[i]+0.25*oowp[i];
		printf("Case #%d:\n",tt);
		for (int i=0;i<n;i++)
			printf("%.12lf\n",rpi[i]);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}