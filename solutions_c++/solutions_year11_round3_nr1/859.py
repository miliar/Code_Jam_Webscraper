#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <string>
#include <cmath>
using namespace std;

const double PI = 3.1415926535897932384626433832795;

char buf[10000];
char a[1000][1000];

void solve()
{
	gets(buf);
	int n, m;
	sscanf(buf, "%d%d", &n, &m);
	for(int i = 0; i < n; ++i)
		gets(a[i]);

	if (n == 1 || m == 1)
		for(int i = 0; i < n; ++i)
			for(int j = 0; j < m; ++j)
				if (a[i][j] == '#')
				{
					cout << "\nImpossible\n";
					return;
				}

	for(int i = 0; i < n - 1; ++i)
		for(int j = 0; j < m; ++j) {
			if (a[i][j] == '#') {
				if (a[i + 1][j] == '#' && a[i][j + 1] == '#' && a[i + 1][j + 1] == '#') {
					a[i][j] = '/';
					a[i + 1][j + 1] = '/';
					a[i + 1][j] = '\\';
					a[i][j + 1] = '\\';
				}
				else
				{
					cout << "\nImpossible\n";
					return;
				}
			}
		}
	for(int i = 0; i < n; ++i) {
		cout << '\n';
		for(int j = 0; j < m; ++j)
			cout << a[i][j];
	}
	cout << "\n";
}

int main()
{
	freopen("in.txt", "rt", stdin);
	freopen("out.txt", "wt", stdout);
	int t;
	gets(buf);
	t = atoi(buf);
	for(int i = 0; i < t; ++i) {
		printf("Case #%d: ", i + 1);
		solve();
	}
	return (0);
}
