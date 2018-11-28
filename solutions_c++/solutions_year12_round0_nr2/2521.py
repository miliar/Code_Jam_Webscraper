#include <cstdio>

int test(int x, int p)
{
	int d = x/3-1;
	if (d<0)
		d = 0;
	for (int i = d; i<d+4; ++i)
		 for (int j=i; j<=i+1; ++j)
			for (int k=j; k<=i+1; ++k)
				if (i+j+k == x && k >= p)
				{
				//	printf("i=%d j=%d k=%d\n",i,j,k);
					return 1;
				}
	d = x/3-2;
	if (d<0)
		d = 0;
	for (int i = d; i<d+5; ++i)
		for (int j = i; j<=i+2; ++j)
			for (int k = j; k<=i+2; ++k)
				if (i+j+k == x && k >= p)
				{
				//	printf("i=%d j=%d k=%d\n",i,j,k);
					return 2;
				}
	return 0;
}

void solve()
{
	int n,s,p;
	int r = 0;
	scanf("%d%d%d",&n,&s,&p);
	for (int i=0; i<n; ++i)
	{
		int x;
		scanf("%d",&x);
		int ret = test(x,p);
		//printf("x=%d p=%d ret=%d\n",x,p,ret);
		if (ret == 1)
			++r;
		if (ret > 1 && s > 0)
			++r,--s;
	}
	printf("%d\n",r);
}

int main()
{
	int t;
	scanf("%d",&t);
	for (int i = 1; i<=t; ++i)
	{
		printf("Case #%d: ",i);
		solve();
	}
	return 0;
}