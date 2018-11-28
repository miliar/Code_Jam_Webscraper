#include <cstdio>
int main()
{
	char a[105][105];
	int n,t,i,k,j;
	double owp[105],oowp,rpi,p[105],w[105];
	
	freopen("rpi.in","r",stdin);
	freopen("rpi.out","w",stdout);
	scanf("%d",&t);
	for (k=1;k<=t;++k)
	{
		scanf("%d\n",&n);
		for (i=1;i<=n;++i)
			{scanf("%s",a[i]);w[i]=p[i]=0;}
		for (i=1;i<=n;++i)
			for (j=0;j<n;++j)
				if (a[i][j]=='0')
					++p[i]; else
						if (a[i][j]=='1')
							++p[i],++w[i];
		for (i=1;i<=n;++i)
		if (p[i]!=0)	
		{
			double sum=0,nr=0;
			for (j=0;j<n;++j)
				if (a[i][j]=='0')
					++nr,sum+=(w[j+1]-1)/(p[j+1]-1); else
						if (a[i][j]=='1')
						++nr,sum+=w[j+1]/(p[j+1]-1);
			owp[i]=sum/nr;
		}
		printf("Case #%d:\n",k);
		for (i=1;i<=n;++i)
		if (p[i]!=0)	
		{
			double oowp=0;
			for (j=0;j<n;++j)
				if ((a[i][j]=='0') || (a[i][j]=='1'))
					oowp+=owp[j+1];
			oowp=(oowp/p[i])/4;
			oowp+=(w[i]/p[i]/4)+(owp[i]/2);
			printf("%lf\n",oowp);
		} else
			printf("0\n");
		
		
			
		
	}
return 0;
}
		