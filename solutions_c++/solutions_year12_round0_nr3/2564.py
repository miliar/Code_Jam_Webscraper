#include <cstdio>
#include <cstring>

int rotate(int a,int z)
{
	int d = (a/z);
	int r = (a%z);
	return r*10+d;
}

void solve()
{
	int A, B;
	scanf("%d%d",&A,&B);
	int r = 0;
	for (int i=A; i<=B; ++i)
	{
		int z = 10;
		while (z <= i)
			 z *= 10;
		z /= 10;
		for (int j=rotate(i,z); j!=i; j=rotate(j,z))
		{
			r += (i<j && j<=B?1:0);
		}
	}
	printf("%d\n",r);
}

int main()
{
	int t;
	scanf("%d",&t);
	for (int i=1; i<=t; ++i)
	{
		printf("Case #%d: ",i);
		solve();
	}
	return 0;
}