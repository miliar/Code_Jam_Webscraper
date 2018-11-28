#include<iostream>
using namespace std;
int i[2048],i2[20][2048],b[20][2048][20];
int main()
{
	int a,s,d,n,p,q,inf=1000000000;
int _,T;
scanf("%d",&T);
for(_=1;_<=T;_++)
{
	scanf("%d",&n);
	p=1;
	for(a=0;a<n;a++) p*=2;
	for(a=0;a<p;a++) scanf("%d",&i[a]);
	q=p/2;
	for(a=n-1;a>=0;a--)
	{
		for(s=0;s<q;s++) scanf("%d",&i2[a][s]);
		q=q/2;
	}
	for(a=0;a<p;a++)
	{
		for(s=0;s<=i[a];s++) b[n][a][s]=0;
		for(s=i[a]+1;s<=n+1;s++) b[n][a][s]=inf;
//		b[n][a][n+1]=-1;
	}
	q=p/2;
	for(a=n-1;a>=0;a--)
	{
		for(s=0;s<q;s++)
		{
			for(d=0;d<=n;d++)
			{
				b[a][s][d]=b[a+1][s*2][d]+b[a+1][s*2+1][d];
			}
			b[a][s][n+1]=inf;
			for(d=0;d<=n;d++)
			{
				b[a][s][d]=min(min(b[a][s][d]+i2[a][s],b[a][s][d+1]),inf);
//if( a==n-1 ) printf("%d ",b[a][s][d]);
			}
//if( a==n-1 ) printf("\n");
		}
		q=q/2;
	}
	printf("Case #%d: %d\n",_,b[0][0][0]);
}
	return 0;
}
