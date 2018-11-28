#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <bitset>
#include <list>
#include <algorithm>
#include <cmath>

#include <cstdlib>
#include <ctime>

using namespace std;

typedef long long LL;

#define ALL(x) (x).begin(), (x).end()
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); ++i)
#define FORI(it, v) for(__typeof((v).begin()) it = (v).begin(); it != (v).end(); ++it)
#define pb push_back
#define mp make_pair

#define MAXN 10005

int N;

int type[MAXN], change[MAXN];
int value[MAXN];

int bst[MAXN][2];

inline void dfs(int k)
{
	if (k + k > N)
	{
		bst[k][value[k]] = 0;
		bst[k][!value[k]] = 0x3f3f3f3f;
		return;
	}

	dfs(k + k);
	dfs(k + k + 1);

	if (type[k] == 1)	//AND
	{
		bst[k][1] = min(0x3f3f3f3f, bst[k + k][1] + bst[k + k + 1][1]);
		bst[k][0] = 0x3f3f3f3f;
		FOR(a, 0, 2) FOR(b, 0, 2)
			if (a != 1 || b != 1)
				bst[k][0] = min(bst[k][0], bst[k + k][a] + bst[k + k + 1][b]);
	}
	else			//OR
	{
		bst[k][0] = min(0x3f3f3f3f, bst[k + k][0] + bst[k + k + 1][0]);
		bst[k][1] = 0x3f3f3f3f;
		FOR(a, 0, 2) FOR(b, 0, 2)
			if (a != 0 || b != 0)
				bst[k][1] = min(bst[k][1], bst[k + k][a] + bst[k + k + 1][b]);
	}

	if (change[k])
	{
		int newbst[2] = {bst[k][0], bst[k][1]};

		if (type[k] == 0)
		{
			newbst[1] = min(0x3f3f3f3f, bst[k + k][1] + bst[k + k + 1][1]);
			newbst[0] = 0x3f3f3f3f;
			FOR(a, 0, 2) FOR(b, 0, 2)
				if (a != 1 || b != 1)
					newbst[0] = min(newbst[0], bst[k + k][a] + bst[k + k + 1][b]);
		}
		else
		{
			newbst[0] = min(0x3f3f3f3f, bst[k + k][0] + bst[k + k + 1][0]);
			newbst[1] = 0x3f3f3f3f;
			FOR(a, 0, 2) FOR(b, 0, 2)
				if (a != 0 || b != 0)
					newbst[1] = min(newbst[1], bst[k + k][a] + bst[k + k + 1][b]);
		}

		bst[k][0] = min(bst[k][0], newbst[0] + 1);
		bst[k][1] = min(bst[k][1], newbst[1] + 1);
	}
}

int main()
{
//	freopen("A.in", "rt", stdin);
//	freopen("A.out", "wt", stdout);

	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		int V;
		scanf("%d %d", &N, &V);
		for (int i = 1; i <= (N - 1) / 2; i++)
			scanf("%d %d", type + i, change + i);
		for (int i = (N - 1) / 2 + 1; i <= N; i++)
			scanf("%d", value + i);

		dfs(1);
		if (bst[1][V] == 0x3f3f3f3f)
			printf("Case #%d: IMPOSSIBLE\n", t);
		else
			printf("Case #%d: %d\n", t, bst[1][V]);

	}

	return 0;
}


