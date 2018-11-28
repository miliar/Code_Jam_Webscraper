#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <cctype>

using namespace std;
template <class T> T sqr(T a) { return a * a; }

int prime[1001];
int np[1001];
int cnt[1001];
int cnt2[1001];
int n, pc;

void precalc()
{
	memset(np, 0, sizeof(np));
	pc = 0;
	for (int i = 2; i < 1000; i++)
		if (!np[i])
		{
			prime[pc++] = i;
			for (int j = i * 2; j < 1000; j += i)
				np[j] = 1;
		}
}

int main()
{
#ifdef impetus
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	precalc();
	int testnum;
	scanf("%d", &testnum);
	for (int tc = 0; tc < testnum; tc++)
	{
		scanf("%d", &n);
		if (n == 1)
		{
			printf("Case #%d: 0\n", tc + 1);
			continue;
		}
		int mx = 1;
		int mn = 0;
		for (int i = 2; i <= n; i++)
		{
			int r = i;
			if (!np[r])
			{
				mn++;
				while (r <= n)
				{
					mx++;
					r *= i;
				}
			}
		}
		/*int mn = 0;
		memset(cnt, 0, sizeof(cnt));
		for (int i = n; i >= 2; i--)
		{
			int r = i;
			int fail = 0;
			memset(cnt2, 0, sizeof(cnt2));
			for (int j = 0; j < pc && r > 1; j++)
			{
				while (r % prime[j] == 0)
				{
					r /= prime[j];
					cnt2[j]++;
				}
				if (cnt2[j] > cnt[j])
					fail = 1;
			}
			if (fail)
			{
				mn++;
				for (int j = 0; j < pc; j++)
					cnt[j] += cnt2[j];
			}
		}*/
		printf("Case #%d: %d\n", tc + 1, mx - mn);
	}
	return 0;
}