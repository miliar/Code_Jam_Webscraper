#include<iostream>
using namespace std;

const int maxl = 101;
bool mark[maxl][maxl], tmark[maxl][maxl];

void init()
{
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		int x1, y1, x2, y2;
		scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
		for (int x = x1; x <= x2; x++)
			for (int y = y1; y <= y2; y++)
				mark[x][y] = true;
	}
}

void solve()
{
	int ans = 0;
	for (;;)
	{
		bool flag = true;
		for (int i = 1; i < maxl; i++)
			for (int j = 1; j < maxl; j++)
			{
				tmark[i][j] = mark[i][j];
				if (mark[i][j] && !mark[i - 1][j] && !mark[i][j - 1]) tmark[i][j] = false;
				if (!mark[i][j] && mark[i - 1][j] && mark[i][j - 1]) tmark[i][j] = true;
				if (mark[i][j]) flag = false;				
			}
		if (flag) break;
		ans++;
		memmove(mark, tmark, sizeof(mark));
	}
	cout << ans << endl;
}

int main()
{
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		cout << "Case #" << t << ": " ;
		init();
		solve();
	}
}