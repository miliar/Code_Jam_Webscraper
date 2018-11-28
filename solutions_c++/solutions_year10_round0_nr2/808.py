#include <stdio.h>

#define N 1001
__int64 a[N];
__int64 n;
__int64 ab[N*N];
__int64 p;
__int64 d;
__int64 m;


#define ABS(a) ((a)>0?(a):-(a))

__int64 GCD(__int64 a, __int64 b)  
{  
	__int64 gcd;  
	if (a < b)  
	{  
		gcd = GCD(b, a);  
	}  
	else  
	{
		while (b != 0)  
		{  
			__int64 t = a % b;  
			a = b;  
			b = t;  
		}  
		gcd = a;  
	}  
	return gcd;  
}  

int main()
{
	__int64 t, i, j, k;

	//freopen("test.in", "r", stdin);
	freopen("B-small-attempt0.in.txt", "r", stdin);
	freopen("B-small-attempt0.out.txt", "w", stdout);

	scanf("%I64d", &t);
	for(i = 0; i < t; i++)
	{
		if(scanf("%d", &n) == EOF) break;
		for(j = 0; j < n; j++)
		{
			scanf("%I64d", a + j);
			//printf("%I64d\n", a[j]);
		}
		p = 0;
		for(j = 0; j < n; j++)
		{
			for(k = j + 1; k < n; k++)
			{
				ab[p] = a[j] - a[k];
				ab[p] = ABS(ab[p]);
				p++;
			}
		}
		if(p == 1) {
			d = ab[0];
		} else {
			d = GCD(ab[0], ab[1]);
			for(j = 2; j < p; j++)
			{
				d = GCD(d, ab[j]);
			}
		}
		m = (d - (a[0] % d)) % d;
		printf("Case #%I64d: %I64d\n", i + 1, m);

	}
	return 0;
}
