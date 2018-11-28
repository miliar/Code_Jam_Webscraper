#include <stdio.h>
#include <string.h>

typedef __int64 I64d;
int main()
{
	int r , k , n;
	int a[1010];
	int check[1010] = {0};
	I64d mon[1010] = {0};
	int tu[1010] = {0};
	int cas , t , i , w , tt;
	I64d total , xunMon , s;
	int xunTu , x;

	freopen("C-large.in" , "r" , stdin);
	freopen("C-large.out" , "w" , stdout);

	scanf("%d" , &cas);
	for (t = 1; t <= cas; t ++)
	{
		scanf("%d %d %d" , &r , &k , &n);
		
		for (i = 0; i < n; i ++) {check[i] = 0; mon[i] = 0; tu[i] = 0;}
		total = 0;

		s = 0;
		for (i = 0; i < n; i ++)
		{
			scanf("%d" , &a[i]);
			s += a[i];
		}
		printf("Case #%d: " , t);
		if (s <= k)
		{
			printf("%I64d\n" , (I64d)s * (I64d)r);
			continue;
		}
		check[0] = 1;
		mon[0] = 0;
		tu[0] = 0;
		s = 0;
		w = n-1;
		i = 0;
		tt = 0;
		while (tt < r)
		{
			while (i != w)
			{
				if (s + a[i] <= k) s += a[i];
				else break;
				i ++;
				if (i == n) i = 0;
			}
			tt ++;
			total += (I64d)s;
			if (check[i] == 0)
			{
				check[i] = 1;
				mon[i] = total;
				tu[i] = tt;
				w = i - 1;
				if (w < 0) w = n-1;
				s = 0;
			}
			else
			{
				xunMon = total - mon[i];
				xunTu = tt - tu[i];
				total = mon[i];
				tt = tu[i];
				x = i;
				break;
			}
		}
		r -= tt;
		if (r > 0 && xunTu > 0)
		{
			total = total + xunMon * (I64d)(r / xunTu);
			r %= xunTu;
			i = x;
			w = i-1;
			if (w < 0) w = n-1;
			s = 0;
			while (r --)
			{
				while (i != w)
				{
					if (s + a[i] <= k) s += a[i];
					else break;
					i ++;
					if (i == n) i = 0;
				}
				total += (I64d)s;
				w = i-1;
				if (w < 0) w = n-1;
				s = 0;
			}
		}
		printf("%I64d\n" , total);
	}
	return 0;
}