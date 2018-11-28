#include <cstdio>
#include <cstring>
//#include <cmath>
#include <limits>
#include <algorithm>

using namespace std;

int P, Q;
int q[110];
long long mem[110][110];

long long f(int a, int b)
{
	if (mem[a][b] >= 0)
		return mem[a][b];
	else if (abs(a - b) <= 1)
		return mem[a][b] = 0;
	else if (abs(a - b) == 2)
		return mem[a][b] = abs(q[a] - q[b]) - 2;
	else
	{
		long long res = std::numeric_limits<long long>::max();
		for (int i = a + 1; i < b; ++i)
			res = min(res, f(a, i) + f(i, b));
		return mem[a][b] = res + abs(q[a] - q[b]) - 2;
	}
}

int main()
{
	int T;

	scanf("%d", &T);

	for (int t = 1; t <= T; ++t)
	{
		memset(mem, 0xff, sizeof(mem));

		scanf("%d %d", &P, &Q);

		for (int i = 1; i <= Q; ++i)
			scanf("%d", q+i);

		q[0] = 0;
		q[Q + 1] = P + 1;

		printf("Case #%d: %lld\n", t, f(0, Q + 1));
	}

	return 0;
}
