#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

void go()
{
	int n, m;
	scanf("%d%d", &n, &m);
	vector<vector<pair<int, int>>> p(m);
	for (int i = 0; i < m; ++i)
	{
		int t; scanf("%d", &t);
		int a, b;
		for (int j = 0; j < t; ++j) {
			scanf("%d%d", &a, &b);
			p[i].push_back(make_pair(a - 1, b));
		}		
	}
	int best = -1, bestc;
	for (int i = 0; i < 1 << n; ++i)
	{
		int ct = 0;
		for (int j = 1; j <= i; j <<= 1) if (j & i) ++ct;
		if (best != -1 && ct >= bestc) continue;
		bool ok = true;
		for (int j = 0; j < m && ok; ++j)
		{
			bool s = false;
			for (int k = 0; k < p[j].size() && !s; ++k)
				s = ((i >> p[j][k].first) & 1) == p[j][k].second;
			ok = s;
		}
		if (ok) best = i, bestc = ct;
	}
	if (best == -1) printf("IMPOSSIBLE\n");
	else {
		for (int i = 0; i < n; ++i)
			printf("%d ", (best >> i) & 1);
		printf("\n");
	}
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int C;
	scanf("%d", &C);
	for (int i = 0; i < C; ++i)
	{
		printf("Case #%d: ", i  +1);
		go();
	}
}