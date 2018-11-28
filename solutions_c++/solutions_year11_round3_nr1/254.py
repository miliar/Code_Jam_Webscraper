#include <iostream>
#include <string>
using namespace std;

int R, C;
string m[55];

bool tst(int x, int y)
{
	if (m[x][y] != '#') return true;
	if (x >= R - 1) return false;
	if (y >= C - 1) return false;
	if (m[x][y + 1] != '#' || m[x + 1][y + 1] != '#' || m[x + 1][y] != '#')
		return false;
	m[x][y] = '/'; m[x + 1][y] = '\\';
	m[x][y + 1] = '\\'; m[x + 1][y + 1] = '/';
	return true;
}

void solve(int cID)
{
	cin >> R >> C;
	for (int i = 0; i < R; i ++)
		cin >> m[i];

	int x = 0, y = 0;
	bool f = true;
	while (true)
	{
		if (!tst(x, y)) 
		{
			f = false;
			break;
		}
		y ++;
		if (y >= C)
		{
			y = 0;
			x ++;
		}
		if (x >= R) break;
	}

	cout << "Case #" << cID << ":\n";
	if (f) {
		for (int i = 0; i < R; i ++)
			cout << m[i] << endl;
	}
	else cout << "Impossible\n";
}

int main()
{
	int T;
	cin >> T;
	for (int t = 1; t <= T; t ++)
		solve(t);
}
