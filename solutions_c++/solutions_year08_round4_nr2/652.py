#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;


struct s { int x; int y; int p; bool operator <(const s & o) const { return p < o.p; }; };

int main()
{
	int C;
	scanf("%d", & C);
	for (int Case = 0; Case < C; Case++)
	{
		int N, M, A;
		scanf("%d%d%d", & N, & M, & A);

		int T = (N + 1) * (M + 1);
		vector<s> a(T);
		{
		for (int i = 0; i <= N; i++) for (int j = 0; j <= M; j++)
		{
			s & n = a[i * (M + 1) + j];
			n.x = i;
			n.y = j;
			n.p = i * j;
		}}

		sort(a.begin(), a.end());

		int i = 0, j = 0;
		while (i < T && j < T)
		{
			if (a[i].p - a[j].p == A)
				break;
			if (a[i].p - a[j].p > A)
				j++;
			else
				i++;
		}
		if (i < T && j < T)
			printf("Case #%d: %d %d %d %d %d %d\n", Case + 1, 0, 0, a[i].x, a[j].y, a[j].x, a[i].y);
		else
			printf("Case #%d: IMPOSSIBLE\n", Case + 1);
	}
	return 0;
}
