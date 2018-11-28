#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

__int64 gcd(__int64 a, __int64 b)
{
	if(a < b)
	{
		__int64 tmp = a;
		a = b;
		b = tmp;
	}
	__int64 c;
	do
	{
		c = a%b;
		a = b;
		b = c;

	}while(c > 0);

	return a;
}

int main()
{
	int ca, c;
	int i, j, n, k;

	__int64 a[11], b[11], ans;

	freopen("c:\\B-small-attempt1.in", "r", stdin);
	freopen("c:\\B-small-attempt1.out", "w+", stdout);

	scanf("%d", &ca);
	for(c = 1; c <= ca; c++)
	{
		printf("Case #%d: ", c);
		scanf("%d", &n);
		for(i = 0;i < n; i++) scanf("%I64d", &a[i]);

		sort(a, a+n);
		k = 1;
		for(i = 1;i < n; i++)
		{
			for(j = i;j < n; j++)
			{
				if(a[j] != a[i-1])
					break;
			}
			a[i] = a[j];
			i = j;
			k++;
		}

		n = k;

		if(n == 1)
		{
			printf("0\n");
			continue;
		}


		for(i = n-1;i >= 1; i--)
		{
			b[i] = a[i] - a[i-1];
		}
		if(n > 2) 
		{
			ans = gcd(b[n-1], b[n-2]);
			for(i = 1;i < n-2; i++)
			{
				ans = gcd(ans, b[i]);
			}
		}
		else ans = b[1];

		if(a[0]%ans != 0)
			printf("%I64d\n", ans - (a[0]%ans));
		else 
			printf("0\n");
	}
	return 0;
}