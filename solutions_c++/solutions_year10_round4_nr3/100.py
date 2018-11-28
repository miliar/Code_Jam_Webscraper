#include <iostream>
#include <set>
#include <string>
#include <map>
#include <queue>
#include <algorithm>

using namespace std;

string name = "c";

int f[101][101];
int n;

void solve()
{
	cin >> n;
	memset(f, 0, sizeof f);
	
	for (int i = 0; i < n; i++)
	{
		int x1, y1, x2, y2;
		cin >> y1 >> x1 >> y2 >> x2;
		for (int x = x1 - 1; x < x2; x++) for (int y = y1 - 1; y < y2; y++) f[x+1][y+1] = 1;
	}
	
	int res = 0;
	bool any = true;
	while (any)
	{
		any = false;
		
		if (false)
		{
		cerr << "--------------------\n";
		for (int i = 0; i < 10; i++)
		{
			for(int j = 0; j < 10; j++)
				cerr << f[i][j];
			cerr << endl;
		}
		}
		
		for (int x = 100; x > 0; x--) for (int y = 100; y > 0; y--)
		if (true)
		{
			any |= f[x][y];
			if (f[x-1][y] == 0 && f[x][y-1] == 0) f[x][y] = 0;
			if (f[x-1][y] == 1 && f[x][y-1] == 1) f[x][y] = 1;
		}
		if (any) res++;
	}
	cout << res << endl;
}

int main()
{
	freopen((name + ".in").c_str(), "r", stdin);
	freopen((name + ".out").c_str(), "w", stdout);
	
	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; test++)
	{
		cout << "Case #" << test << ": ";
		solve();
	}
	return 0;
}