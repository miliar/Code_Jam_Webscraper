#include<iostream>
using namespace std;

const int maxp = 10 + 1;
int a[maxp][1 << maxp], b[1 << maxp], p, d[maxp][1 << maxp][maxp];
 
void init()
{
	scanf("%d", &p);
	for (int i = 0; i < (1 << p); i++)
		scanf("%d", &b[i]);
	for (int i = p - 1; i >= 0; i--)
		for (int j = 0; j < (1 << i); j++)
			scanf("%d", &a[i][j]);
}

void dp(int dep)
{
	if (dep == p - 1)
	{
		for (int i = 0; i < (1 << p - 1); i++)
		{
			d[dep][i][max(p - b[i * 2], p - b[i * 2 + 1])] = 0;
			for (int j = 0; j < p; j++)	
				d[dep][i][j + 1] = min(d[dep][i][j + 1], d[dep][i][j]);
		}
		return;
	}
	dp(dep + 1);
	for (int i = 0; i < (1 << dep); i++)
	{
		for (int j = 0; j < p; j++)
			d[dep][i][j] = min(d[dep][i][j], min(d[dep + 1][i * 2][j], d[dep + 1][i * 2][j + 1] + a[dep + 1][i * 2])
						  + min(d[dep + 1][i * 2 + 1][j], d[dep + 1][i * 2 + 1][j + 1] + a[dep + 1][i * 2 + 1]));
		for (int j = 0; j < p; j++)	
				d[dep][i][j + 1] = min(d[dep][i][j + 1], d[dep][i][j]);
	}
			
}

void solve()
{
	memset(d, 50, sizeof(d));
	dp(0);
	cout << min(d[0][0][0], d[0][0][1] + a[0][0]) << endl;
}

int main()
{
	freopen("bl.in", "r", stdin);
	freopen("b0.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		cout << "Case #" << t << ": " ; 
		init();
		solve();
	}
}