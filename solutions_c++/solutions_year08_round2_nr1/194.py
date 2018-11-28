#include<cstdio>
const long long mn=105;
long long T,n,A,B,C,D,X0,Y0,M,X,Y;
long long x[mn],y[mn];
int main()
{
	freopen("A-small-attempt1.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%I64d",&T);
	for(long long tn=1;tn<=T;tn++)
	{
		scanf("%I64d%I64d%I64d%I64d%I64d%I64d%I64d%I64d",&n,&A,&B,&C,&D,&X0,&Y0,&M);
		X=X0,Y=Y0;
		x[0]=X,y[0]=Y;
		for(long long i=1;i<=n-1;i++)
		{
			X = (A * X + B)%M;
			Y = (C * Y + D)%M;
			x[i]=X,y[i]=Y;
		}
		long long cnt=0;
		for(long long i=0;i<n;i++)
			for(long long j=i+1;j<n;j++)
				for(long long k=j+1;k<n;k++)
					if((x[i]+x[j]+x[k])%3==0&&(y[i]+y[j]+y[k])%3==0)cnt++;
		printf("Case #%I64d: %I64d\n",tn,cnt);
	}
	return 0;
}
