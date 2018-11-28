#include <cstdio>
#include <vector>
using namespace std;

#define FOR(i,a,b) for(int i=(a); i<(int)(b); ++i)

int di[] = {-1, 0, 0, 1};
int dj[] = {0, -1, 1, 0};

int dfs(vector< vector<int> > &a, vector< vector<int> > &res, int i, int j, int c)
{
	if (res[i][j] != -1) return res[i][j];
	res[i][j] = c;
	int mnAlt = a[i][j];
	FOR(d,0,4)
	{
		int ii = i+di[d];
		int jj = j+dj[d];
		if (ii < 0 || ii >= res.size()) continue;
		if (jj < 0 || jj >= res[0].size()) continue;
		mnAlt = min(mnAlt, a[ii][jj]);
	}

	if (mnAlt < a[i][j])
	FOR(d,0,4)
	{
		int ii = i+di[d];
		int jj = j+dj[d];
		if (ii < 0 || ii >= res.size()) continue;
		if (jj < 0 || jj >= res[0].size()) continue;
		if (mnAlt == a[ii][jj])
		{
			return res[i][j] = dfs(a, res, ii, jj, c);
		}
	}

	return res[i][j] = c;
}

vector< vector<int> > comps(vector< vector<int> > &a)
{
	int n = a.size(), m = a[0].size();
	vector< vector<int> > res(n, vector<int>(m, -1));
	int c = 0;
	FOR(i,0,n) FOR(j,0,m)
		if (res[i][j] == -1)
		{
			int tt = dfs(a, res, i, j, c);
			c += (tt == c);
		}
	return res;
}

int main()
{
	int T;
	freopen("B-large.in", "rt", stdin);
	freopen("B-large.out", "wt", stdout);
	scanf("%d", &T);
	FOR(cas,1,T+1)
	{
		int H, W;
		scanf("%d%d", &H, &W);
		vector< vector<int> > a(H, vector<int>(W) );
		FOR(i,0,H) FOR(j,0,W)
			scanf("%d", &a[i][j]);

		vector< vector<int> > b = comps(a);

		int alp = 'a';
		vector<int> mp(256, -1);

		printf("Case #%d:\n", cas);
		fprintf(stderr, "Case #%d:\n", cas);

		FOR(i,0,H) FOR(j,0,W)
		{
			if (mp[b[i][j]] == -1)
				mp[b[i][j]] = alp++;
			printf("%c%c", mp[b[i][j]], j+1 < W ? ' ' : '\n');
		}
	}
	return 0;
}
