#include <iostream>
#include <fstream>
#include <string>

using namespace std;

ifstream fin("D-small-attempt0.in.txt");
ofstream fout("D-small-attempt0.out.txt");

int n, H, W, R;
int rock[200][200];
int ans[200][200];

int main()
{
	fin >> n;
	for (int cases = 1; cases <= n; cases++)
	{
		fin >> H >> W >> R;

		memset(rock, 0, sizeof(rock));
		for (int i = 0; i < R; i++)
		{
			int j, k;
			fin >> j >> k;
			rock[j-1][k-1] = 1;
		}

		memset(ans, 0, sizeof(ans));
		ans[0][0] = 1;
		for (int i = 0; i < H; i++)
		{
			for (int j = 0; j < W; j++)
			if (ans[i][j] > 0)
			{
				int x, y;
				x = i + 1;
				y = j + 2;
				if (rock[x][y] == 0 && x < H && y < W)
					ans[x][y] = (ans[x][y] + ans[i][j]) % 10007;

				x = i + 2;
				y = j + 1;
				if (rock[x][y] == 0 && x < H && y < W)
					ans[x][y] = (ans[x][y] + ans[i][j]) % 10007;

			}
		}
		
		fout << "Case #" << cases << ": " << ans[H-1][W-1] << endl;
	}
	
	return 0;
}