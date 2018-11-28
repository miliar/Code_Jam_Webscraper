#include <iostream>

using namespace std;

const int MAX = 505;

int g[MAX][MAX], row[MAX][MAX], col[MAX][MAX], sum[MAX][MAX];
int c1[MAX][MAX], c2[MAX][MAX];

int main()
{
  freopen("b.in", "r", stdin);
  freopen("b.out", "w", stdout);
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++)
  {
    cout << "Case #" << t << ": ";
		int r, c, d;
		cin >> r >> c >> d;
		for (int i = 0; i < r; i++)
			for (int j = 0; j < c; j++)
			{
				char ch;
				cin >> ch;
				g[i][j] = ch - '0';
				sum[i][j] = col[i][j] = row[i][j] = g[i][j];
				if (i > 0)
				{
					row[i][j] += row[i-1][j];
					sum[i][j] += sum[i-1][j];
				}
				if (j > 0)
				{
					col[i][j] += col[i][j-1];
					sum[i][j] += sum[i][j-1];
				}
				if (i > 0 && j > 0)
					sum[i][j] -= sum[i-1][j-1];
			}
		int ans = 0;
		for (int k = 3; k <= r && k <= c; k++)
		{
//			cout << "k " << k << endl;
			for (int i = 0; i <= r - k; i++)
			{
//				cout << "i " << i << endl;
				__int64 cur = 0;
				for (int j = 0; j < k; j++)
				{
					cur += (row[i+k-1][j] - ((i > 0) ? row[i-1][j] : 0)) * (2 * j - (k-1));
				}
				for (int j = 0; j <= c-k; j++)
				{
//					cout << cur << endl;
					if (cur + (g[i+k-1][j] + g[i][j] - g[i+k-1][j+k-1] - g[i][j+k-1]) * (k-1) == 0)
						c1[i][j] = 1;
					else
						c1[i][j] = 0;
					cur += (k-1) * (row[i+k-1][j] - ((i > 0) ? row[i-1][j] : 0) + row[i+k-1][j+k] - ((i > 0) ? row[i-1][j+k] : 0));
//					cout << cur << endl;
					cur -= 2 * (sum[i+k-1][j+k-1] - sum[i+k-1][j] - ((i > 0) ? (sum[i-1][j+k-1] - sum[i-1][j]) : 0));
				}
			}
			for (int j = 0; j <= c - k; j++)
			{
				__int64 cur = 0;
				for (int i = 0; i < k; i++)
				{
					cur += (col[i][j+k-1] - ((j > 0) ? col[i][j-1] : 0)) * (2 * i - (k-1));
				}
				for (int i = 0; i <= r-k; i++)
				{
					if (cur + (g[i][j+k-1] + g[i][j] - g[i+k-1][j+k-1] - g[i+k-1][j]) * (k-1) == 0)
						c2[i][j] = 1;
					else
						c2[i][j] = 0;
					if (c1[i][j] && c2[i][j])
						ans = k;
					cur += (k-1) * (col[i][j+k-1] - ((j > 0) ? col[i][j-1] : 0) + col[i+k][j+k-1] - ((j > 0) ? col[i+k][j-1] : 0));
					cur -= 2 * (sum[i+k-1][j+k-1] - sum[i][j+k-1] - ((j > 0) ? (sum[i+k-1][j-1] - sum[i][j-1]) : 0));
				}
			}
		}
		if (ans)
			cout << ans;
		else
			cout << "IMPOSSIBLE";
    cout << endl;
  }
  return 0;
}