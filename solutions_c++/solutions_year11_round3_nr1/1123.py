#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
using namespace std;
const int maxn = 100;
#define forn(i, n) for (int i = 0; i < n; i++)

char s[maxn][maxn];

void solve();

int main()
{
	freopen("input.txt","r", stdin);
	freopen("output.txt", "w", stdout);
	
	int t;
	cin >> t;
	forn(i, t)
	{
		cout << "Case #" << i+1 << ":\n";
		solve();
	}
};
void solve()
{
	int n, m;
	cin >> n >> m;
	int c=0;
	forn(i, n) 
	{
		cin >> s[i];
		c += count(s[i], s[i]+m, '#');
	}
	forn(i, n-1) forn(j, m-1)
	{
		if (s[i][j] == '#' && s[i+1][j] == '#' && s[i][j+1] == '#' && s[i+1][j+1] == '#')
		{
			c -= 4;
			s[i][j] = s[i+1][j+1] = '/';
			s[i+1][j] = s[i][j+1] = '\\';
		}
	}
	if (c)
		cout << "Impossible\n";
	else forn(i, n) cout << s[i] << endl;
};
