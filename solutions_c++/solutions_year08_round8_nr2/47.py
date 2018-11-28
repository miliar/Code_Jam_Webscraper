#include <string>
#include <map>
#include <algorithm>
#include <vector>
using namespace std;

#define MAXC 512
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define INF 999999999

int cid = 0, N;
map<string, int> C;
vector<pair<int, int> > V[MAXC];

int solve()
{
	for (int i = 0; i < N; i++)
		sort(V[i].begin(), V[i].end());

	int result = INF;
	for (int i = 0; i < cid; i++)
		for (int j = i; j < cid; j++)
			for (int k = j; k < cid; k++)
			{
				int res = 0, ls = 1;
				int indi = 0, indj = 0, indk = 0;
				int maxi = -1, maxj = -1, maxk = -1;

				while (ls <= 10000)									
				{
					while (indi < V[i].size() && V[i][indi].first <= ls)
					{
						maxi = MAX(maxi, V[i][indi].second);
						indi++;
					}

					while (indj < V[j].size() && V[j][indj].first <= ls)
					{
						maxj = MAX(maxj, V[j][indj].second);
						indj++;
					}

					while (indk < V[k].size() && V[k][indk].first <= ls)
					{
						maxk = MAX(maxk, V[k][indk].second);
						indk++;
					}

					int maxv = MAX(maxi, MAX(maxj, maxk)) + 1;

					if (maxv <= ls)
						break;

					ls = maxv;
					res++;
				}

				if (ls <= 10000)
					res = INF;

				result = MIN(result, res);
			}

	return result;
}

void readAndSolve()
{
	int T, t;

	scanf("%d", &T);

	for (int t = 1; t <= T; t++)
	{
		for (int j = 0; j < 512; j++)
			V[j].clear();
		C.clear();
		cid = 0;

		scanf("%d", &N);

		for (int i = 0; i < N; i++)
		{
			char str[512];
			int a, b;

			scanf("%s %d %d", str, &a, &b);

			if (C.count(str) == 0)
				C[str] = cid++;

			int color = C[str];
			V[color].push_back(make_pair(a, b));
		}

		int res = solve();

		if (res < INF)
			printf("Case #%d: %d\n", t, res);
		else
			printf("Case #%d: IMPOSSIBLE\n", t);
	}
}

int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);

	readAndSolve();

	return 0;
}