#include <fstream>
#include <string>
#include <iostream>
#include <vector>
using namespace std;
typedef long long ll;

int w[501][501], wi[501][501], wj[501][501];
int s[501][501], si[501][501], sj[501][501];

bool isOK(int x, int y, int k)
{
	int sum = s[x+k][y+k] + s[x][y] - s[x+k][y] - s[x][y+k];
	int sumX = si[x+k][y+k] + si[x][y] - si[x+k][y] - si[x][y+k];
	int sumY = sj[x+k][y+k] + sj[x][y] - sj[x+k][y] - sj[x][y+k];

	sum -= (w[x][y] + w[x+k-1][y] + w[x][y+k-1] + w[x+k-1][y+k-1]);
	sumX -= (wi[x][y] + wi[x+k-1][y] + wi[x][y+k-1] + wi[x+k-1][y+k-1]);
	sumY -= (wj[x][y] + wj[x+k-1][y] + wj[x][y+k-1] + wj[x+k-1][y+k-1]);

	sumX *= 2;
	sumY *= 2;
	int targetX = sum * (2*x + k - 1);
	int targetY = sum * (2*y + k - 1);
	return sumX == targetX && sumY == targetY;
}

int main()
{
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");

	for (int i=0; i<501; ++i)
		s[0][i] = s[i][0] = si[0][i] = si[i][0] = sj[0][i] = sj[i][0] = 0;

	unsigned int numberOfCases;
	fin >> numberOfCases;

	int R,C,D;
	string ss;
	for (unsigned int zz=1; zz<=numberOfCases; ++zz)
	{
		fin >> R >> C >> D;
		

		for (int i=0; i<R; ++i)
		{
			fin >> ss;
			for (int j=0; j<C; ++j)
			{
				w[i][j] = ss[j]-'0';
				wi[i][j] = w[i][j] * i;
				wj[i][j] = w[i][j] * j;

				s[i+1][j+1] = w[i][j] + s[i][j+1] + s[i+1][j] - s[i][j];
				si[i+1][j+1] = wi[i][j] + si[i][j+1] + si[i+1][j] - si[i][j];
				sj[i+1][j+1] = wj[i][j] + sj[i][j+1] + sj[i+1][j] - sj[i][j];
			}
		}

		
		int res = 0;
		for (int k = min(R,C); k>=3; --k)
		{
			for (int x=0; x+k <= R; ++x)
				for (int y=0; y+k <= C; ++y)
				{
					if (res == 0 && isOK(x, y, k))
						res = k;
				}
		}

		if (res == 0)
		{
			fout << "Case #" << zz << ": " << "IMPOSSIBLE" << endl;
		}
		else
		{
			fout << "Case #" << zz << ": " << res << endl;
		}
	}

	return 0;
}
