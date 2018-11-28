#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <queue>

using namespace std;

int main()
{
	freopen("f:\\C-small-attempt0.in", "r", stdin);
	freopen("f:\\C-small-attempt0.out", "w", stdout);

	int T, N, v;
	scanf("%d", &T);
	for (int t_case = 1; t_case <= T; t_case++)
	{
		int xor = 0, sum = 0, minv = (1<<30);
		scanf("%d", &N);
		for (int i = 0; i < N; i++)
		{
			scanf("%d", &v);
			xor ^= v; sum += v;
			if (minv > v) minv = v;
		}
		if (xor != 0)
		{
			printf("Case #%d: NO\n", t_case);
		}
		else
		{
			printf("Case #%d: %d\n", t_case, sum - minv);
		}
	}
	return 0;
}
