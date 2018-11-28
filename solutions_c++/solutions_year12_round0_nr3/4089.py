#include <stdio.h>
#include <math.h>

int getdig(int x)
{
	int ret = 0;
	while(x > 0)
	{
		x /= 10;
		ret++;
	}
	
	return ret;
}

int recycle(int x,int n)
{
	int tmp = x % 10;
	tmp *= pow(10, (n - 1));
	x /= 10;
	return (tmp+x);
}

int check(int a, int b)
{
	int i;
	int c = b;
	int n = getdig(b);

	for( i = 1; i < n; i++)
	{
		c = recycle(c, n);
		if(a == c)
		{
			return 1;
		}
	}

	return 0;
}


int main()
{
	int n;
	int a,b;
	int i,j,k;
	int ans;
	
	scanf("%d", &n);
	for(k = 1; k <= n; k++)
	{
		scanf("%d %d", &a, &b);
		ans = 0;
		for(i = a; i <= b; i++)
		{
			for(j = i + 1; j <= b; j++)
			{
				ans += check(i, j);
			}
		}

		printf("Case #%d: %d\n", k, ans);
	}

}
