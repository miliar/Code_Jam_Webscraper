#include<cstdio>

int xsqr(int x)
{
	return x*x;
}

int xpow(int a, int k)
{
	if (k==0) return 1;
	if (k%2==0) return xsqr(xpow(a,k/2));
	return a*xpow(a,k-1);
}

int main()
{
	freopen("in","r",stdin);
	freopen("out","w",stdout);


	int t,k,d,n;
	scanf("%d",&t);

	for (int i=0; i<t; i++)
	{
		scanf("%d%d",&n,&k);

		d=xpow(2,n);

		printf("Case #%d: ",i+1);
		if (k%d==d-1) printf("ON\n"); else printf("OFF\n");
	}

	return 0;
}