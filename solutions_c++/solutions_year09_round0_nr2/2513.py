#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <vector>
#include <utility>

#define forn(i, n) for(int i = 0; i < int(n); i++)
#define ft first
#define sc second
#define mp make_pair
#define pb push_back
#define NMAX 200
#define INF (INT_MAX / 2)

using namespace std;

typedef pair<int, int> pt;

int dx[] = { -1, 0, 0, 1 };
int dy[] = { 0, -1, 1, 0};

char cur;
int n, m;
int a[NMAX][NMAX], ans[NMAX][NMAX];
vector<pt> g[NMAX][NMAX];

void dfs(int i, int j)
{
	ans[i][j] = cur;

	forn(idx, g[i][j].size())
	{
		int x = g[i][j][idx].ft, y = g[i][j][idx].sc;
		if(!ans[x][y])
			dfs(x, y);
	}
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	cin >> T;

	forn(test, T)
	{
		cur = 'a';
		memset(ans, 0, sizeof(ans));

		cin >> n >> m;
		forn(i, n)
			forn(j, m)
				scanf("%d", &a[i][j]);

		forn(i, n)
			forn(j, m)
			{
				int minv = INF, mink = -1;
				forn(k, 4)
				{
					int xx = i + dx[k], yy = j + dy[k];
					if(0 <= xx && xx < n && 0 <= yy && yy < m &&
						minv > a[xx][yy] && a[xx][yy] < a[i][j])
						minv = a[xx][yy], mink = k;
				}

				if(mink != -1)
				{
					int xx = i + dx[mink], yy = j + dy[mink];
					g[i][j].pb(mp(xx, yy));
					g[xx][yy].pb(mp(i, j));
				}
			}

		forn(i, n)
			forn(j, m)
				if(!ans[i][j])
					dfs(i, j), cur++;

		printf("Case #%d:\n", test + 1);
		forn(i, n)
		{
			forn(j, m)
				printf("%c ", ans[i][j]), g[i][j].clear();
			printf("\n");
		}
	}

	return 0;
}