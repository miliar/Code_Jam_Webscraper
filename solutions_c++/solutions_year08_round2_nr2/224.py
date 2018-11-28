#include <cstdio>
#include <iostream>

using namespace std;


bool prime[1024];
int a[1024], len;
void get_prime()
{
	int i, j;
	memset(prime, 0, sizeof(prime));
	for (i = 2; i <= 100; i ++)
	{
		if (prime[i] == 0)
		{
			for (j = i + i; j <= 1000; j += i)
				prime[j] = 1;
		}
	}
	len = 0;
	for (i = 2; i <= 1000; i ++)
		if (prime[i] == 0)
			a[len++] = i;
}

int father[1024];

int find(int k)
{
	if (k == father[k])
		return k;
	return father[k] = find(father[k]);
}

int main()
{
	int T, t = 1;
	get_prime();
	scanf("%d", &T);
	while (T --)
	{
		int i, j, A, B, P, st, en, k;
		scanf("%d%d%d", &A, &B, &P);
		for (i = A; i <= B; i ++)
			father[i] = i;
		for (i = 0; ; i ++)
		{
			if (a[i] > B)
				break;
			if (a[i] < P)
				continue;
			for (j = A; j <= B; j ++)
			{
				for (k = j + 1; k <= B; k ++)
				{
					if (j % a[i] == 0 && k % a[i] == 0)
					{
						st = find(j);
						en = find(k);
						if (st != en)
							father[en] = st;
					}
				}
			}
		}
		bool flag[1024];
		memset(flag, 0, sizeof(flag));
		int ans = 0;
		for (i = A; i <= B; i ++)
		{
			k = find(i);
			if (flag[k] == 0)
				ans ++;
			flag[k] = 1;
		}
		printf("Case #%d: %d\n", t ++, ans);
	}
	return 0;
}