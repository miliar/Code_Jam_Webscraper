#include <stdio.h>

int gcd(int a , int b)
{
	int z;
	if (b == 0) return a;
	while ((a % b) > 0) {
		z = a;
		a = b;
		b = z % b;
	}
	return b;
}

int main()
{
	int c , n , t , k , res;
	int a[10];
	int b[10];

	freopen("B-small-attempt1.in" , "r" , stdin);
	freopen("B-small-attempt1.out" , "w" , stdout);

	scanf("%d" , &c);
	for (t = 1; t <= c; t ++)
	{
		scanf("%d" , &n);
		for (int i = 0; i < n; i ++) scanf("%d" , &a[i]);
		printf("Case #%d: " , t);
		if (n == 2)
		{
			k = a[0] - a[1];
			if (k < 0) k = -k;
			if (k == 0) res = 0;
			else
			{
				res = a[0] % k;
				res = (k - res) % k;
			}
		}
		else if (n == 3)
		{
			int x = a[0] - a[1];
			int y = a[0] - a[2];
			int z = a[1] - a[2];
			if (x < 0) x = -x;
			if (y < 0) y = -y;
			if (z < 0) z = -z;
			int xx = gcd(x , y);
			int k = gcd(xx , z);
			if (k == 0)
			{
				res = 0;
			}
			else
			{
				res = a[0] % k;
				res = (k - res) % k;
			}
		}
		printf("%d\n" , res);
	}
	return 0;
}