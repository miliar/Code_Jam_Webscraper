#include <iostream>
using namespace std;
const int MaxN=10000;
int test,t, r, k, n, next[MaxN];
long long g[MaxN], tot[MaxN];
long long ans;
void inputint()
{
	scanf ("%d%d%d", &r, &k, &n);
	for (int i = 0; i < n; i++)
		scanf("%d", &g[i]);
}
void work()
{
    long long cur;
    int i, endMark;
	for(i = 0; i < n; i++)
	{
		tot[i] = 0;
		endMark = 0;
		for(int j = i; j < n; j++)
			if (tot[i] + g[j] <= k)
				tot[i] += g[j];
			else
			{
				next[i] = j;
				endMark = 1;
				break;
			}
		if (!endMark)
			for ( int j = 0; j < i; j++)
				if (tot[i] + g[j] <= k)
					tot[i] += g[j];
				else
				{
					next[i] = j;
					endMark = 1;
					break;
				}

		if (!endMark)
			next[i] = i;
	}

	ans = 0;   
	cur = 0;
	for (int i = 0; i < r; i++)
	{
		ans += tot[cur];
		cur = next[cur];
	}
	printf ( "Case #%d: %lld\n", test + 1, ans);
}
int main()
{
	freopen("theme.in", "r", stdin);
	freopen("theme.out", "w", stdout);
	scanf ("%d", &t);
	for (test = 0; test < t; test++)
	{
		inputint();
		work();
	}
}
