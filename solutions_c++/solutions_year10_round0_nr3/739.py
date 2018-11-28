#include <cstdio>
#include <inttypes.h>

using namespace std;

int g[1000], m[1000];
long long s[1000];

int main(int argc, char *argv[])
{
	int t;
	scanf("%d", &t);
	for (int c = 0; c < t; c++)
	{
		int r, k, n;
		scanf("%d %d %d", &r, &k, &n);
		for (int i = 0; i < n; i++)
			scanf("%d", &g[i]);
		m[0] = 0;
		s[0] = 0;
		for (int i = 0; i < n; i++)
		{
			if (i != 0)
			{
				s[i] = s[i - 1] - g[i - 1];
				m[i] = m[i - 1];
			}
			if (m[i] == i && s[i] + g[i] <= k)
			{
				s[i] += g[m[i]];
				m[i] = (m[i] + 1) % n;
			}
			for (; (m[i] != i) && ((s[i] + g[m[i]]) <= k); m[i] = (m[i] + 1) % n)
				s[i] += g[m[i]];
		}
		long long res = 0;
		int cur = 0;
		for (int i = 0; i < r; i++)
		{
			res += s[cur];
			cur = m[cur];
		}

		printf("Case #%d: %I64d\n", c + 1, res);
	}
	return 0;
}