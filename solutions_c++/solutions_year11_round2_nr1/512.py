#include <stdio.h>

char q[100][101];
int p[100];
int t[100];
double wp[100];
double owp[100];
double oowp[100];

int main()
{
	long long n,i,j,ca=0,k,nn,in;
	scanf("%lld",&nn);
//	printf("%lld\n",nn);
	for (in=0;in<nn;++in)
	{
		scanf("%lld",&n);
//		printf("%lld\n",n);
		for (i=0;i<n;++i) { scanf("%s",q[i]);}
		for (i=0;i<n;++i)
		{
			p[i]=t[i]=0;
			for (j=0;j<n;++j)
			{
				if (q[i][j]=='1') { ++p[i]; ++t[i]; }
				if (q[i][j]=='0') ++t[i];
			}
			if (t[i]==0) ++t[i];
			wp[i]=p[i]/(double)t[i];
		}
		for (i=0;i<n;++i)
		{
			k=0;
			owp[i]=0.0;
			for (j=0;j<n;++j)
			{
				if (q[i][j]!='.') 
				{
					if (q[i][j]=='1') owp[i]+=p[j]/(double)(t[j]-1); else owp[i]+=(p[j]-1)/(double)(t[j]-1);
					++k;
				}
			}
			owp[i]/=k;
		}
		for (i=0;i<n;++i)
		{
			k=0;
			oowp[i]=0.0;
			for (j=0;j<n;++j)
			{
				if (q[i][j]!='.') 
				{
					oowp[i]+=owp[j];
					++k;
				}
			}
			oowp[i]/=k;
		}
		printf("Case #%lld:\n",++ca);
		for (i=0;i<n;++i) printf("%.12lf\n",0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]);
	}
	return 0;
}
