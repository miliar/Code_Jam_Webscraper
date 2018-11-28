#include <iostream>
using namespace std;

const int N = 105;
bool g[N][N];

int check()
{
	for (int i = 1; i < N; i++)
		for (int j = 1; j < N; j++)
			if (g[i][j]) return true;
	return false;
}

void calc()
{
	for (int i = N-1; i >= 1; i--)
		for (int j = N-1; j >= 1; j--)
			if (g[i][j])
			{
				if (!g[i-1][j] && !g[i][j-1])
					g[i][j] = false;
			}
			else
			{
				if (g[i-1][j] && g[i][j-1])
					g[i][j] = true;
			}
}
void print()
{
	for (int i = 1; i <= 5; i++)
	{
		for (int j = 1; j <= 5; j++)
			if (g[i][j])
				cout << 1;
			else
				cout << 0;
		cout << endl;
	}
	cout << endl;
}
void work()
{
	int r;
	cin >> r;
	memset(g, false, sizeof(g));
	for (int i = 1; i <= r; i++)
	{
		int x1, y1, x2, y2;
		cin >> x1 >> y1 >> x2 >> y2;
		for (int x = min(x1, x2); x <= max(x1, x2); x++)
			for (int y = min(y1, y2); y <= max(y1, y2); y++)
				g[x][y] = true;
	}
//	print();
	int cnt = 0;
	while (check())
	{
		cnt++;
		calc();
//		print();
	}
	cout << cnt << endl;
}

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out","w", stdout);
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		cout << "Case #" << t << ": ";
		work();
	}
}