#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <map>
#include <set>
#define LL long long
#define ldb long double
#define sqr(a) ((a) * (a))
#define nextLine() {int c = 0; while((c = getchar()) != 10 && c != EOF);}
#define addEdge(a, b) next[edges] = first[a]; first[a] = edges; end[edges] = a;
#define debug(a) cerr << #a << " = " << a << " ";
#define debugl(a) cerr << #a << " = " << a << "\n";
const ldb eps = 1e-9;
const ldb pi = fabsl(atan2(0.0, -1.0));
const LL LINF = 1ll << 60;
const ldb LDINF = 1e42;
const int INF = 0x7f7f7f7f;
using namespace std;
#define problem "a"

char a[1110][1110];
int n, m;
void Load()
{
	cin >> n >> m;
	nextLine();
	for (int i= 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			a[i][j] = getchar();
		}
		nextLine();
	}
}

void Solve(int Test)
{
	cout << "Case #" << Test << ":\n";
	int i, j;
	for (i = 0; i < n; i++)
	{
		for (j = 0; j < m; j++)
		{
			if (a[i][j] == '#')
			{
				if (i + 1 >= n || j + 1 >= m)
				{
					printf("Impossible\n");
					return;
				}
				if (a[i + 1][j] != '#' || a[i][j + 1] != '#' || a[i + 1][j + 1] != '#')
				{
					printf("Impossible\n");
					return;
				}
				a[i][j]  = a[i + 1][j + 1] = '/';
				a[i + 1][j] = a[i][j + 1] = '\\';
			}
		}
	}
	for (i = 0; i < n; i++)
	{
		for (j = 0; j < m; j++)
		{
			putchar(a[i][j]);
		}
		putchar('\n');
	}
}

int main()
{
	freopen(problem ".in", "rt", stdin);
	freopen(problem ".out", "wt", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		Load();
		Solve(i + 1);
	}
	return 0;
}

