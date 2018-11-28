#include <iostream>
#include <cstdio>
#include <vector>
#include <fstream>
#include <utility>
#include <algorithm>

#define SQR(X) X*X
#define MAX(X,Y) (X)>(Y)? (X) : (Y)


using namespace std;

int main() {
	freopen("in.txt","r",stdin);
	freopen("outB.txt","w",stdout);
	int tcount;
	cin >> tcount;
	for(int tt=1;tt<=tcount;++tt){
		char s;
		int R, C, D;
		cin >> R >> C >> D;

		vector<vector<int> > a(R, vector<int>(C));
		for (int i = 0; i < R; i++)
		{
			for (int j = 0; j < C; j++)
			{
				cin >> s;
				a[i][j] = D + (s - '0');
			}
		}

		double c;
		int x, y, res=-1;
		bool done = false;
		for (int k = min(R, C); k >= 3 && !done; k--)
		{
			c = (k + .0) / 2;
			for (int i = 0; i <= R - k && !done; i++)
			{
				for (int j = 0; j <= C - k && !done; j++)
				{
					double xx = 0, yy = 0;
					for (int m = 0; m < k; m++)
					{
						for (int n = 0; n < k; n++)
						{
							if (!((m == 0 && n == 0) || (m == 0 && n == k - 1) || (m == k - 1 && n ==0) || (m == k -1 && n == k -1)))
							{
								x = i + m;
								y = j + n;
								xx += (k - m - 0.5 - c) * a[x][y];
								yy += (k - n - 0.5 - c) * a[x][y];
							}
						}
					}

					if (xx == 0 && yy == 0)
					{
						done = true;
						res = k;
					}
				}
			}
		}

		if (!done)
		{
			cout << "Case #" << tt << ": IMPOSSIBLE" << endl;
		} else {
			cout << "Case #" << tt << ": " << res << endl;
		}
	}
	fclose(stdout);
	return 0;
}
