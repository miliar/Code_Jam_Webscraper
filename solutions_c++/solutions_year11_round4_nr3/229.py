#include <stdio.h>
#include <string.h>

typedef __int64 i64d;

int p[80000];
int num;
int b[1000001] = {0};

int main()
{
	int cas;
	freopen("C-large.in" , "r" , stdin);
	freopen("C-large.out" , "w" , stdout);
	scanf("%d" , &cas);
	for (int i = 2; i * i <= 1000000; i ++)
	{
		for (int k = i * i; k <= 1000000; k += i)
			b[k] = 1;
	}
	num = 0;
	for (int i = 2; i <= 1000000; i ++)
		if (b[i] == 0) p[num++] = i;
	
	for (int ca = 1; ca <= cas; ca ++)
	{
		i64d n;
		scanf("%I64d" , &n);
		if (n == 1) {printf("Case #%d: 0\n" , ca); continue;}
		int res = 1;
		for (int i = 0; i < num; i ++)
		{
			if (p[i] * 2 > n) break;
			i64d k = p[i];
			while (k <= n/(i64d)p[i])
			{
				k *= (i64d)p[i];
				res ++;
			}
		}
		printf("Case #%d: %d\n" , ca , res);
	}
	return 0;
}