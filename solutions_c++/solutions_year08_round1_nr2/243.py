#include <cstdio>
#include <vector>

using namespace std;

int C, N, M, T, X, Y;
vector<vector<pair<int,int>>> vv;

void solve(int id)
{
	bool md = false;
	vector<int> aux(N, 0);
	vector<int> tt;

	do
	{
		tt.clear();
	for (size_t i = 0;i < vv.size();++i)
	{
		if (vv[i].size() == 1 && vv[i][0].second == 1)
		{
			tt.push_back(vv[i][0].first);
			aux[tt.back() - 1] = 1;
			vv[i].clear();
		}
	}

	for (size_t i = 0;i < vv.size() && !md;++i)
		for (size_t j = 0;j < vv[i].size() && !md;++j)
			for (size_t k = 0;k < tt.size() && !md;++k)
			{
				if (vv[i][j].first == tt[k])
				{
					if (vv[i][j].second == 1) vv[i].clear();
					else 
					{
						vv[i].erase(vv[i].begin() + j);
						--j;
						if (vv[i].empty()) md = true;
					}
					break;
				}
			}
	} while (!tt.empty() && !md);

	printf("Case #%d:", id);
	if (md) printf(" IMPOSSIBLE\n");
	else
	{
		for (int i = 0;i < N;++i)
			printf(" %d", aux[i]);
		printf("\n");
	}
}

int main()
{
	/*freopen("B-small.in", "r", stdin);
	freopen("B-small.txt", "w", stdout);*/

	freopen("B-large.in", "r", stdin);
	freopen("B-large.txt", "w", stdout);

	vector<pair<int,int>> vt;
	scanf("%d", &C);
	for (int i = 0;i < C;++i)
	{
		//for (size_t j = 0;j < vv.size()) vv[j].clear();
		vv.clear();

		scanf("%d", &N);
		scanf("%d", &M);
		for (int j = 0;j < M;++j)
		{
			vt.clear();
			scanf("%d", &T);
			for (int k = 0;k < T;++k)
			{
				scanf("%d %d", &X, &Y);
				vt.push_back(make_pair(X, Y));
			}
			vv.push_back(vt);
		}
		solve(i + 1);
	}
	return 0;
}