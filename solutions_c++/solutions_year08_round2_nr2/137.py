#include <iostream>
using namespace std;
const int MAX = 1005;

int a, b, p;
int cnt, prime[MAX];
bool flag[MAX];

void pro()
{
	cnt = 0;
	int i, j;
	memset(flag, false, sizeof(flag));
	for (i = 2; i < MAX; ++ i)
		if (!flag[i])
		{
			prime[cnt++] = i;
			for (j = i*i; j < MAX; j+=i)
				flag[j] = true;
		}
}

int main (void)
{
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);
	pro();
	int Case = 1, T;
	scanf("%d", &T);
	while (T--)
	{
		scanf("%d %d %d", &a, &b, &p);
		int ans = b-a+1;
		int i, j, k;
		for (i = 0; i < cnt; ++ i)
			if (prime[i] >= p)
				break;
		memset(flag, false, sizeof(flag));
		for (i; i < cnt; ++ i)
		{
			bool first = true;
			k = a/prime[i];
			if (a % prime[i]) k ++;
			k *= prime[i];
			for (j = k; j <= b; j += prime[i])
			{
				if (j == k) ans ++;
				if (flag[j] && first)
				{
					ans --;
					first = false;
				}
				else if (!flag[j])
				{
					ans --;
					flag[j] = true;
				}
			}
		}

		printf("Case #%d: %d\n", Case++, ans);
	}
	return 0;
}