#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <cstdio>



using namespace std;

int h, w, r;
int x[12], y[12];


int a[120][121];
int dp[120][121];

void Load()
{
	cin >> h >> w >> r;
	memset(a, 0, sizeof(a));
	memset(dp, 0, sizeof(dp));
	int i;
	for (i = 0; i < r; i++)
	{
		cin >> x[i] >> y[i];
		a[x[i]][y[i]] = 1;
	}
}

void Solve()
{
	
	dp[h][w] = 1;

	int i, j;
	for (i = h; i > 0; i--)
	{
		for (j = w; j > 0; j--)
		{
			if (i == h && j == w) continue;
			if (a[i][j] == 1) dp[i][j] = 0;
			else 
				dp[i][j] = (dp[i+1][j+2] + dp[i+2][j+1]) % 10007;	
		}
	}
	cout << dp[1][1];
}


int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int nt, tt;

	cin >> nt;

	for (tt = 1; tt <= nt; tt++)
	{
    	Load();
    	cout << "Case #" << tt << ": ";
    	Solve();
    	cout << "\n";
    }
	return 0;
}