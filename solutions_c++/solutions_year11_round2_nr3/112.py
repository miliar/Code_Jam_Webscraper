#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cassert>
#include <vector>

using namespace std;

const int MAX = 2048;
bool has[MAX][MAX];

int N, U[MAX], V[MAX];

vector<vector<int> > R;
vector<vector<int> > FR;

bool vst[MAX];

void dfs(int s, int u, vector<int> vt)
{
	vst[u] = true;
	if (vt.size() > 2 && has[u][s] == true)
	{
		R.push_back(vt);
	}
	else
	{
		for (int v = 1; v <= N; v++) if (!vst[v])
		{
			if (has[u][v])
			{
				vt.push_back(v);
				dfs(s, v, vt);
				vt.pop_back();
			}
		}
	}
	vst[u] = false;
}

bool cmp(const vector<int> &p, const vector<int> &q)
{
	return p.size() < q.size();
}

bool contain(const vector<int> &p, const vector<int> &q)
{
	int i = 0, j = 0;
	int n = p.size(), m = q.size();
	while (i < n && j < m)
	{
		if (p[i] == q[j])
		{
			i++;
			j++;
		}
		else
		{
			i++;
		}
	}
	return j == m;
}

int t_case, color[MAX];

int MAXC, res, res_color[MAX];

void dfs1(int p, int c)
{
	if (p > N)
	{
		if (c <= res) return;
		for (int i = 0; i < FR.size(); i++)
		{
			int v = 0;
			for (int j = 0; j < FR[i].size(); j++)
			{
				v |= (1<<(color[FR[i][j]]-1));
			}
			if (v != (1<<c)-1) return;
		}
		if (c > res)
		{
			res = c;
			for (int i = 1; i <= N; i++)
				res_color[i] = color[i];
		}
		return;
	}

	for (int i = 1; i <= c + 1; i++)
	{
		color[p] = i;
		if (i <= c)
			dfs1(p + 1, c);
		else
			dfs1(p + 1, c + 1);
	}		
}

int main()
{
	freopen("f:\\C-small-attempt0.in", "r", stdin);
	freopen("f:\\C-small-attempt0.out", "w", stdout);

	int T, M;
	scanf("%d", &T);
	for (t_case = 1; t_case <= T; t_case++)
	{
		memset(has, 0, sizeof(has));

		scanf("%d %d", &N, &M);
		for (int i = 0; i < M; i++)
			scanf("%d", &U[i]);
		for (int i = 0; i < M; i++)
		{
			scanf("%d", &V[i]);
			has[U[i]][V[i]] = has[V[i]][U[i]] = true;
		}
		for (int i = 0; i < N; i++)
			has[i+1][(i+1)%N+1] = true;
		R.clear(); FR.clear();
		for (int i = 1; i <= N; i++)
		{
			vector<int> v;
			v.push_back(i);
			dfs(i, i, v);
		}
		for (int i = 0; i < R.size(); i++)
			sort(R[i].begin(), R[i].end());
		sort(R.begin(), R.end(), cmp);
		bool del[MAX];
		memset(del, 0, sizeof(del));
		for (int i = 0; i < R.size(); i++)
		{
			for (int j = i + 1; j < R.size(); j++)
			{
				if (contain(R[j], R[i]))
					del[j] = true;
			}
		}
		for (int i = 0; i < R.size(); i++) if (!del[i])
		{
			FR.push_back(R[i]);
		}
		MAXC = N;
		if (!FR.empty())
			MAXC = FR[0].size();

		res = 1;
		for (int i = 1; i <= N; i++)
			res_color[i] = 1;
		dfs1(1, 1);
		printf("Case #%d: %d\n", t_case, res);
		for (int i = 1; i <= N; i++)
		{
			printf("%d", res_color[i]);
			if (i < N) putchar(' ');
			else putchar('\n');
		}
	}
	return 0;
}
