#include <iostream>
#include <fstream>

using namespace std;

ifstream fin("in.txt");
ofstream fout("out.txt");

const int dx[4] = {-1, 0, 0, 1};
const int dy[4] = {0, -1, 1, 0};

int T, H, W;
char letter;
int lat[102][102];
char lab[102][102];

char bloodfill(int x, int y)
{
	if (lab[x][y] != '#') return lab[x][y];
	int lowest = 10000;
	int lx, ly;
	for (int dir = 0; dir < 4; ++dir)
	{
		int tx = x + dx[dir];
		int ty = y + dy[dir];
		if (lat[tx][ty] < lat[x][y] && lat[tx][ty] < lowest)
			lowest = lat[tx][ty], lx = tx, ly = ty;
	}
	if (lowest == 10000)
		return lab[x][y] = letter++;
	else
		return lab[x][y] = bloodfill(lx, ly);
}

void solve()
{
	fin >> H >> W;
	for (int i = 0; i < W + 2; ++i) lat[0][i] = 10000;
	for (int i = 0; i < W + 2; ++i) lat[H + 1][i] = 10000;
	for (int i = 0; i < H + 2; ++i) lat[i][0] = 10000;
	for (int i = 0; i < H + 2; ++i) lat[i][W + 1] = 10000;

	for (int i = 1; i <= H; ++i)
		for (int j = 1; j <= W; ++j)
		{
			fin >> lat[i][j];
			lab[i][j] = '#';
		}

	letter = 'a';
	for (int i = 1; i <= H; ++i)
		for (int j = 1; j <= W; ++j)
			if (lab[i][j] == '#') bloodfill(i, j);
	for (int i = 1; i <= H; ++i)
	{
		for (int j = 1; j < W; ++j) fout << lab[i][j] << " ";
		fout << lab[i][W] << endl;
	}
}

int main()
{
	fin >> T;
	for (int cas = 1; cas <= T; ++cas)
	{
		fout << "Case #" << cas << ":" << endl;
		solve();
	}
	return 0;
}
