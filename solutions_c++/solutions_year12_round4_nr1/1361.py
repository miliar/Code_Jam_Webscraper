#include <iostream>
#include <math.h>

using namespace std;

int n;
int d[10000];
int l[10000];
int dd;
bool m[10000][10000];

bool solve(int x, int y)
{
	if (m[x][y])
		return false;
	int cur_len = min(d[y] - d[x], l[y]);
	if (d[y] + cur_len >= dd)
		return true;
	int i = y;
	while (i < n - 1)
	{
		i++;
		if (d[i] - d[y] > cur_len)
			break;
		if (solve(y, i))
			return true;
	}
	m[x][y] = true;
	return false;
}

void solve()
{
	cin >> n;
	for (int i = 0; i < n; i++)
		cin >> d[i] >> l [i];
	cin >> dd;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			m[i][j] = false;
	
	int cur_len = d[0];
	if (d[0] + cur_len >= dd)
	{
		cout << "YES" << endl;
		return;
	}
	int i = 0;
	while (i < n - 1)
	{
		i++;
		if (d[i] - d[0] > cur_len)
			break;
		if (solve(0, i))
		{
			cout << "YES" << endl;
			return;
		}
	}
	cout << "NO" << endl;
}

int main()
{
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		cout << "Case #" << i + 1 << ": ";
		solve();
	}

	return 0;
}

