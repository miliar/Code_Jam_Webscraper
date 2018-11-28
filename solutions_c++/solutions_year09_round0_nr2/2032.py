#include <fstream>
#include <algorithm>
using namespace std;

int map[105][105];
int codes[105][105];

int dx[4] = { 0, -1, 1, 0 };
int dy[4] = { -1, 0, 0, 1 };

int T = 0, W = 0, H = 0;

void Replace(int from, int to)
{
	for (int i = 0; i < H; i++)
	{
		for (int j = 0; j < W; j++)
		{
			if (codes[i][j] == from)
			{
				codes[i][j] = to;
			}
		}
	}
}

int nx, ny;

int main()
{
	ifstream fin("data.txt");
	fin >> T;
	int temp = 0;
	ofstream fout("result.txt");
	for (int i = 0; i < T; i++)
	{
		fin >> H >> W;
		int code = 1000;
		for (int j = 0; j < H; j++)
		{
			for (int k = 0; k < W; k++)
			{
				fin >> map[j][k];
			}
		}

		memset(&codes, 0, sizeof(codes));

		for (int y = 0; y < H; y++)
		{
			for (int x = 0; x < W; x++)
			{
				int mmin = INT_MAX;
				for (int m = 0; m < 4; m++)
				{
					nx = x + dx[m];
					ny = y + dy[m];
					if (nx >= 0 && nx < W && ny >= 0 && ny < H)
					{
						mmin = min(mmin, map[ny][nx]);
					}
				}
				if (mmin >= map[y][x])
				{
					if (codes[y][x] == 0)
					{
						codes[y][x] = code;
						code++;
					}
					continue;
				}
				for (int m = 0; m < 4; m++)
				{
					nx = x + dx[m];
					ny = y + dy[m];
					if (nx >= 0 && nx < W && ny >= 0 && ny < H && map[ny][nx] == mmin)
					{
						if (codes[y][x] == 0)
						{
							if (codes[ny][nx] == 0)
							{
								codes[y][x] = codes[ny][nx] = code;
								code++;
							}
							else
							{
								codes[y][x] = codes[ny][nx];
							}
						}
						else
						{
							if (codes[ny][nx] == 0)
							{
								codes[ny][nx] = codes[y][x];
							}
							else
							{
								Replace(codes[ny][nx], codes[y][x]);
							}
						}
						break;
					}
				}
			}
		}
		// remake
		int start = 'a';
		for (int y = 0; y < H; y++)
		{
			for (int x = 0; x < W; x++)
			{
				if (codes[y][x] > 900)
				{
					Replace(codes[y][x], start);
					start++;
				}
			}
		}
		// write answer
		fout << "Case #" << i + 1 << ":" << endl;
		for (int y = 0; y < H; y++)
		{
			for (int x = 0; x < W; x++)
			{
				fout << (char)codes[y][x] << ' ';
			}
			fout << endl;
		}
	}
	fout.close();
	return 0;
}