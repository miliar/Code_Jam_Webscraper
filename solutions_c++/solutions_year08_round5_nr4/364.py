#include <iostream>
#include <fstream>
using namespace std;

#define cin fin
#define cout fout

ifstream fin("aD-small-attempt0.in");
ofstream fout("a.out");

const int maxh = 105;
const int x[2] = {1, 2};
const int y[2] = {2, 1};
int ans[maxh][maxh];
int main()
{
	int num, n, h , r, w;
	int i,j,k, row, col;

	cin >> n;
	for (num= 1;num <= n;num ++)
	{
		cin >> h >> w >> r;
		memset(ans, 0, sizeof(ans));
		for (i = 1;i <= r;i ++)
		{
			cin >> row >> col;
			ans[row][col] = -1;
		}
		ans[1][1] = 1;
		for (i = 1;i <= h - 1;i ++)
			for (j = 1;j<= w - 1;j ++)
				if (ans[i][j] >= 0)
				for (k = 0;k <= 1;k ++)
					if (i + x[k] <= h && j + y[k] <= w && ans[i + x[k]][j + y[k]] >=  0 ) 
					{
						ans[i + x[k]][j + y[k]] += ans[i][j];
						ans[i + x[k]][j + y[k]] = ans[i + x[k]][j + y[k]] % 10007;
					}
		cout << "Case #" << num << ": " << ans[h][w] << endl;

	}
	return 0;
}

