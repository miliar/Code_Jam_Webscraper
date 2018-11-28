#include <stdio.h>

int main()
{
	int t , ca;
	int a1 , a2 , b1 , b2;
	int res , ok;
	int a , b;

	freopen("C-small-attempt0.in" , "r" , stdin);
	freopen("C-small-attempt0.out" , "w" , stdout);
	scanf("%d" , &t);
	for (int ca = 1; ca <= t; ca ++)
	{
		scanf("%d %d %d %d" , &a1 , &a2 , &b1 , &b2);
		printf("Case #%d: " , ca);
		res = 0;
		for (int x = a1; x <= a2; x ++)
			for (int y = b1; y <= b2; y ++)
			{
				a = x > y ? x : y;
				b = x < y ? x : y;
				ok = 1;
				if (a == b) ok = 0;
				else
				{
					int s = 0;
					while (a % b != 0)
					{
						int r = a % b;
						if (a / b > 1) break;
						s ++;
						a = b;
						b = r;
					}
					if ((s & 1) == 1) ok = 0;
				}
				res += ok;
			}
		printf("%d\n" , res);
	}
	return 0;
}