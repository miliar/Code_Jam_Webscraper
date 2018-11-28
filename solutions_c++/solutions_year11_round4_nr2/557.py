#include<cstdio>
#include<algorithm>

using namespace std;

#define MX 600

int tt;
int r,c,d;

long long D[MX][MX];
long long sumA[MX][MX];
long long sumB[MX][MX];
long long sum[MX][MX];

long double Abs(long double x)
{
	if (x<0) return -x;
	return x;
}

long double zrac(int i,int j,int k)
{
	long double ans=0;
	ans+=sum[i+k-1][j+k-1];
	if (i) ans-=sum[i-1][j+k-1];
	if (j) ans-=sum[i+k-1][j-1];
	if (i&&j) ans+=sum[i-1][j-1];
	return ans;
}
long double zracA(int i,int j,int k)
{
	long double ans=0;
	ans+=sumA[i+k-1][j+k-1];
	if (i) ans-=sumA[i-1][j+k-1];
	if (j) ans-=sumA[i+k-1][j-1];
	if (i&&j) ans+=sumA[i-1][j-1];
	return ans;
}
long double zracB(int i,int j,int k)
{
	long double ans=0;
	ans+=sumB[i+k-1][j+k-1];
	if (i) ans-=sumB[i-1][j+k-1];
	if (j) ans-=sumB[i+k-1][j-1];
	if (i&&j) ans+=sumB[i-1][j-1];
	return ans;
}

int main()
{
	scanf("%d",&tt);
	for(int t=1;t<=tt;++t)
	{
		scanf("%d%d%d",&r,&c,&d);
		for(int i=0;i<r;++i)
		{
			for(int j=0;j<c;++j)
			{
				int w;
				scanf("%1d",&w);
				D[i][j]=d+w;
			}
		}
		for(int i=0;i<r;++i)
		{
			for(int j=0;j<c;++j)
			{
				if (i==0)
				{
					if (j==0)
					{
						sumA[i][j]=0;
						sumB[i][j]=0;
						sum[i][j]=D[i][j];
					}
					else
					{
						sumA[i][j]=sumA[i][j-1];
						sumA[i][j]+=D[i][j]*i;
						sumB[i][j]=sumB[i][j-1];
						sumB[i][j]+=D[i][j]*j;
						sum[i][j]=sum[i][j-1];
						sum[i][j]+=D[i][j];
					}
				}
				else if (j==0)
				{
					sumA[i][j]=sumA[i-1][j];
					sumA[i][j]+=D[i][j]*i;
					sumB[i][j]=sumB[i-1][j];
					sumB[i][j]+=D[i][j]*j;
					sum[i][j]=sum[i-1][j];
					sum[i][j]+=D[i][j];
				}
				else
				{
					sumA[i][j]=sumA[i-1][j]+sumA[i][j-1]-sumA[i-1][j-1];
					sumA[i][j]+=D[i][j]*i;
					sumB[i][j]=sumB[i-1][j]+sumB[i][j-1]-sumB[i-1][j-1];
					sumB[i][j]+=D[i][j]*j;
					sum[i][j]=sum[i-1][j]+sum[i][j-1]-sum[i-1][j-1];
					sum[i][j]+=D[i][j];
				}
			}
		}
		//printf("%d %d %d\n",r,c,d);
		int ans=0;
		for(int i=0;i<r;++i)
			for(int j=0;j<c;++j)
				for(int k=3;i+k<=r&&j+k<=c;++k)
				{
					//printf("%d %d %d\n",i,j,k);
					long double suma=0,sum2=0;
					long double s1=zracA(i,j,k)-(i+(k-1)/(long double)2)*zrac(i,j,k);
					s1+=D[i][j]*(k-1)/(long double)2;
					s1+=D[i][j+k-1]*(k-1)/(long double)2;
					s1-=D[i+k-1][j]*(k-1)/(long double)2;
					s1-=D[i+k-1][j+k-1]*(k-1)/(long double)2;
					long double s2=zracB(i,j,k)-(j+(k-1)/(long double)2)*zrac(i,j,k);
					s2+=D[i][j]*(k-1)/(long double)2;
					s2-=D[i][j+k-1]*(k-1)/(long double)2;
					s2+=D[i+k-1][j]*(k-1)/(long double)2;
					s2-=D[i+k-1][j+k-1]*(k-1)/(long double)2;
					//printf("%lf %lf\n",suma,sum2);
					//printf("%lf %lf\n",s1,s2);
					suma=s1;
					sum2=s2;
					long double EPS=1e-11;
					if (Abs(suma)<EPS&&Abs(sum2)<EPS)
					{
						//printf("%d\n",k);
						if (k>ans) ans=k;
					}
				}
		printf("Case #%d: ",t);
		if (ans>=3) printf("%d\n",ans);
		else puts("IMPOSSIBLE");
	}
	return 0;
}
