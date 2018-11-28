#include <cstdio>
int T,I,i,j,n,a[100],b[100];
double wp[100],owp[100],oowp[100];
char s[111][111];
int main()
{
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d",&T);
	for(I=1;I<=T;I++)
	{
		scanf("%d\n",&n);
		for(i=0;i<n;i++)
			wp[i]=owp[i]=oowp[i]=a[i]=b[i]=0;
		for(i=0;i<n;i++)
		{
			gets(s[i]);
			for(j=0;j<n;j++)
				if(s[i][j]=='1')
				{
					a[i]++;
					b[i]++;
				} else
				if(s[i][j]=='0')
					b[i]++;
			wp[i]=1.0*a[i]/b[i];
		}
		for(i=0;i<n;i++)
			for(j=0;j<n;j++)
				if(s[i][j]!='.')
					owp[i]+=1.0*(a[j]-(49-s[i][j]))/(b[j]-1)/b[i];
		for(i=0;i<n;i++)
			for(j=0;j<n;j++)
				if(s[i][j]!='.')
					oowp[i]+=owp[j]/b[i];
		printf("Case #%d:\n",I);
		for(i=0;i<n;i++)
			printf("%.10lf\n",0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);
//			printf("%.6lf %.6lf %.6lf %.6lf %d %d\n",0.25*wp[i]+0.5*owp[i]+0.25*oowp[i],wp[i],owp[i],oowp[i],a[i],b[i]);
	}
	return 0;
}