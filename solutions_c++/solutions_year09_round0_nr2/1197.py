#include <iostream>
#include <algorithm>
#include <cmath>
#include <cassert>
#include <vector>
#include <set>
#include <string>
#define ldb long double
#define LL long long
#define sqr(a) (a) * (a)
#define nextLine() {int c = 0; while((c = getchar()) != 10 && c != EOF);}
const ldb LDINF = 9128739847123.00;
const ldb eps = 1e-9;
const int INF = 2147483647 / 2;
using namespace std;

const int dx[4] = {-1, 0, 0, 1};
const int dy[4] = {0, -1, 1, 0};
int n, m;
int was[110][110];
int a[110][110];
int d[110][110];

void Load()
{
	cin >> n >> m;
	int i;
	int j;
	for (i = 0; i <= n + 1; i++)
	{
		for (j = 0; j <= m + 1; j++)
		{
			a[i][j] = INF;
		}
	}
	for (i = 1; i <= n; i++)
	{
		for (j = 1; j <= m; j++)
		{
         	cin >> a[i][j];
        }
	}
}
int last;

void dfs(int i, int j)
{
	was[i][j] = 1;
	int k;
	int mn = INF;
	for (k = 0; k < 4; k++)
	{
		mn = min(mn, a[i + dx[k]][j + dy[k]]);
	}
	if (mn >= a[i][j]) return;
	for (k = 0; k < 4; k++)
	{
		if (a[i + dx[k]][j + dy[k]] == mn)
		{
			if (was[i + dx[k]][j + dy[k]] == 0)
			{
				d[i + dx[k]][j + dy[k]] = last;
				dfs(i + dx[k], j + dy[k]);
			}
			d[i][j] = min(d[i][j], d[i + dx[k]][j + dy[k]]);
			break;
		}
	}

}
void Solve(int Test)
{
	int i;
	int j;
	for (i = 1; i <= n; i++)
	{
		for (j =1; j <= m; j++)
		{
			was[i][j] = 0;
		}	
	}
	last = 0;
	for (i = 1; i <= n; i++)
	{
		for (j =1; j <= m; j++)
		{
			if (was[i][j] == 0)
			{
				d[i][j] = last;
				dfs(i, j);
				if (d[i][j] == last)
				{
					last++;
				}
			}
		}	
	}
	cout << "Case #" << Test << ":\n";
	for (i = 1; i <= n; i++)
	{
		for (j = 1; j <= m; j++)
		{
			cout << (char)('a' + d[i][j]) << " ";
		}
		cout << "\n";
	}
}


#define file "b"
int main()
{
	freopen(file".in", "rt", stdin);
	freopen(file".out", "wt", stdout);
	int T;
	cin >> T;
	int i;
	for (i = 1; i <= T; i++)
	{
		Load();
		Solve(i);
	}
	return 0;
}