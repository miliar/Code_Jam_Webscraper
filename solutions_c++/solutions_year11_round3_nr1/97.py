#include <cstdio>
#include <cstdlib>
#include <ctype.h>
#include <cstring>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>

#define For(i, n) for (int i = 0; i < n; i ++)
#define foreach(x, i) for (__typeof(x.begin()) i; i != x.end(); i ++)

using namespace std;

int n, m;
char a[100][100];
bool posible()
{
	for (int i = 0; i < n; i ++)
		for (int j = 0; j < m; j ++)
			if (a[i][j] == '#')
			{
				if (i == n - 1 || j == m - 1)
					return false;
				if (a[i + 1][j] != '#' || a[i][j + 1] != '#' || 
						a[i + 1][j + 1] != '#')
					return false;
				a[i][j] = '/';
				a[i][j + 1] = '\\';
				a[i + 1][j] = '\\';
				a[i + 1][j + 1] = '/';
			}
	return true;
}

void print()
{
	For (i, n)
		puts(a[i]);
}

void solve()
{
	scanf("%d%d", &n, &m);
	for (int i = 0; i < n; i ++)
		scanf("%s", a[i]);
	if (posible())
		print();
	else puts("Impossible");

}

int main()
{
	int t; scanf("%d", &t);
	For (i, t) printf("Case #%d:\n", i + 1), solve();
	return 0;
}

