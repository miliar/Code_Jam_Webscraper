#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <cstdio>



using namespace std;


int m, val;


int x[20000];
int tp[20000]; // 1 - and, 0 - or
int ch[20000];
int mi;


const int MNOGO = 0x7f7f7f7f;
int dp[10000][2];

void Load()
{
	cin >> m >> val;
	mi = (m-1) / 2;
	int i;
	for (i = 1; i <= mi; i++)
	{
		cin >> tp[i] >> ch[i];
	}
	memset(dp, 0x7f, sizeof(dp));
	for (i = mi+1; i <= m; i++)
	{
		cin >> x[i];
		dp[i][x[i]] = 0;
	}
}





void Solve()
{
	int j;
	for (j = mi; j >= 1; j--)
	{
		int ca, cac, coc, co;
		int i1, i2;
		for (i1 = 0; i1 < 2; i1++)
		{
			if (dp[2*j][i1] == MNOGO) continue;
			for (i2 = 0; i2 < 2; i2++)
			{
				if (dp[2*j+1][i2] == MNOGO) continue;
				co = ca = 0;
				cac = coc = MNOGO;

				if (tp[j] == 0 || ch[j] == 1)
				{
					co = (i1 | i2);
					coc = dp[2*j][i1] + dp[2*j+1][i2] + tp[j];
				}

				if (tp[j] == 1 || ch[j] == 1)
				{
					ca = (i1 & i2);
					cac = dp[2*j][i1] + dp[2*j+1][i2] + 1 - tp[j];
				}
				if (dp[j][co] > coc) dp[j][co] = coc;
				if (dp[j][ca] > cac) dp[j][ca] = cac;
			}
		}

	}
	j = dp[1][val];
	if (j == MNOGO)
	{
		cout << "IMPOSSIBLE\n";
	}
	else cout << j << "\n";
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
    }
	return 0;
}