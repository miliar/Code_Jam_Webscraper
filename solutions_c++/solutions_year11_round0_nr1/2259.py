#include <algorithm>
#include <cstdio>

using namespace std;

void solve()
{
	int N, task[100][2], p1 = 1, p2 = 1;

	scanf("%d", &N);
	for (int i = 0; i < N; ++i)
	{
		char st[2];
		int p;
		scanf("%s%d", &st[0], &p);

		if (st[0] == 'B') task[i][0] = 1; else task[i][0] = 2;
		task[i][1] = p;
	}

	int cur = 0, t = 0;

	while (cur < N)
	{
		++t;

		bool mv1 = false;
		for (int k = cur; k < N; ++k)
			if (task[k][0] == 1) {
				if (p1 != task[k][1]) { if (p1 > task[k][1]) --p1; else ++p1; mv1 = true; }
				break;
			}

		bool mv2 = false;
		for (int k = cur; k < N; ++k)
			if (task[k][0] == 2) {
				if (p2 != task[k][1]) { if (p2 > task[k][1]) --p2; else ++p2; mv2 = true; }
				break;
			}

		if (task[cur][0] == 1)
		{
			if (!mv1 && p1 == task[cur][1]) ++cur;
		}
		else
		{
			if (!mv2 && p2 == task[cur][1]) ++cur;
		}
	}

	printf("%d\n", t);
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	scanf("%d", &T);

	for (int t = 1; t <= T; ++t)
	{
		printf("Case #%d: ", t);
		solve();
	}

    return 0;
}
