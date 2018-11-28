#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <string>

#define pb push_back
#define mp make_pair
#define sz(v) ((int)(v).size())
#define all(v) (v).begin(),(v).end()

using namespace std;

typedef pair<int, int> ii;
typedef long long int64;
typedef vector<int> vi;

const int maxn = 110;

int n, m;
int a[maxn][maxn];

char res[maxn][maxn];
char cur = 'a';

const int dx[] = {-1, 0, 0, 1};
const int dy[] = {0, -1, 1, 0};

bool good(int x, int y)
{
	return x >= 0 && x < n && y >= 0 && y < m;
}

char dfs(int i, int j)
{
	if (res[i][j] != -1) return res[i][j];
	int mm = a[i][j], md = -1;
	for (int dir = 0; dir < 4; dir++)
	{
		int x = i + dx[dir], y = j + dy[dir];
		if (!good(x, y)) continue;
		if (a[x][y] < mm)
			mm = a[x][y], md = dir;
	}
	if (md == -1)
	{
		res[i][j] = cur++;
		return res[i][j];
	}
	int dir = md;
	int x = i + dx[dir], y = j + dy[dir];
	return res[i][j] = dfs(x, y);
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tc;
	cin >> tc;
	for (int it = 0; it < tc; it++)
	{
		cin >> n >> m;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
				cin >> a[i][j];
		memset(res, -1, sizeof(res));
		cur = 'a';
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
				if (res[i][j] == -1)
					dfs(i, j);
		printf("Case #%d:\n", it + 1);
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < m; j++)
			{
				printf("%c ", res[i][j]);
			}
			printf("\n");
		}
	}
	return 0;
}
