#include <iostream>
#include <fstream>
using namespace std;

int waterMap[110][110];
char results[110][110];
int steps[4][2] = {0, -1, -1, 0, 1, 0, 0, 1};

char dfs(int x, int y, int w, int h, char label)
{
	if (results[y][x] != 0) {
		return results[y][x];
	}

	int lowest = waterMap[y][x];
	int lx = -1, ly = -1;
	for (int i = 0; i < 4; ++ i)
	{
		int ny = y + steps[i][1];
		int nx = x + steps[i][0];
		if (0 <= nx && nx < w && 0 <= ny && ny < h) {
			if (waterMap[ny][nx] < lowest) {
				lowest = waterMap[ny][nx];
				lx = nx;
				ly = ny;
			}
		}
	}
	if (lx == -1) {
		return (results[y][x] = label);
	}
	return (results[y][x] = dfs(lx, ly, w, h, label));
}

void floodFill(int w, int h)
{
	memset(results, 0, sizeof(results));
	char nextLabel = 'a';
	for (int y = 0; y < h; ++ y)
	{
		for (int x = 0; x < w; ++ x)
		{
			if (results[y][x] == 0) {
				char l = dfs(x, y, w, h, nextLabel);
				if (l == nextLabel) {
					++ nextLabel;
				}
			}
		}
	}
}

int main()
{
	int mapCount;
	fstream file("B-small.in");
	fstream output("B-small.out", ios_base::out);
	file >> mapCount;

	int caseIndex = 0;
	while (++caseIndex <= mapCount)
	{
		int w, h;
		file >> h >> w;
		for (int i = 0;  i < h; ++ i)
		{
			for (int j = 0; j < w; ++ j)
			{
				file >> waterMap[i][j];
			}
		}
		floodFill(w, h);
		output << "Case #" << caseIndex << ':' << endl;
		for (int i = 0; i < h; ++ i)
		{
			for (int j = 0; j < w - 1; ++ j)
			{
				output << results[i][j] << ' ';
			}
			output << results[i][w - 1] << endl;
		}
	}

	file.close();
	output.close();
	return 0;
}