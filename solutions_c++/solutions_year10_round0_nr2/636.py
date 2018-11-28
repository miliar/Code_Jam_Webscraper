#include <stdio.h>

int gcd(int a,int b)
{
	if(a<0)
		a=-a;
	if(b<0)
		b=-b;
	int r;
	while(a && b)
	{
		r=a%b;
		a=b;
		b=r;
	}
	return a+b;
}

int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int T,t,a[10],n,i,j,r;
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)
			scanf("%d",&a[i]);
		r=0;
		for(i=0;i<n;i++)
			for(j=i+1;j<n;j++)
				r=gcd(r,a[i]-a[j]);
		printf("Case #%d: %d\n",t,(r-a[0]%r)%r);
	}
	return 0;
}