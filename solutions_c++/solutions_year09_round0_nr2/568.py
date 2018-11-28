#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

ifstream fin("B-large.in");
ofstream fout("B-large.out");
#define cin fin
#define cout fout

int dire[4][2] = {{-1,0},{0,-1},{0,1},{1,0}};
int data[110][110];
int next[110][110];
int H, W, T;

int tot;
int map[110][110];
char label[30];

void flood(int x, int y, int label)
{
	if (map[x][y] != 0) return;
	map[x][y] = label;

	int x1, y1, x2, y2, k1;

	for (int k = 0; k < 4; k++)
	{
		x1 = x + dire[k][0];
		y1 = y + dire[k][1];

		if (x1 >= 0 && x1 < H && y1 >= 0 && y1 < W && next[x1][y1] != -1)
		{
			k1 = next[x1][y1];
			x2 = x1 + dire[k1][0];
			y2 = y1 + dire[k1][1];
			if (x2 == x && y2 == y) flood(x1, y1, label);
		}
	}
}

int main()
{
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		cin >> H >> W;
		for (int x = 0; x < H; x++)
			for (int y = 0; y < W; y++)
				cin >> data[x][y];

		int x1, y1;

		for (int x = 0; x < H; x++)
			for (int y = 0; y < W; y++)
			{
				int best = -1;
				for (int k = 0; k < 4; k++)
				{
					x1 = x + dire[k][0];
					y1 = y + dire[k][1];
					if (x1 >= 0 && x1 < H && y1 >= 0 && y1 < W && data[x1][y1] < data[x][y] && (best == -1 || data[x1][y1] < best))
					{
						best = data[x1][y1];
						next[x][y] = k;
					}
				}
				if (best == -1) next[x][y] = -1;
			}

		memset(map, 0, sizeof(map));
		tot = 0;
		for (int x = 0; x < H; x++)
			for (int y = 0; y < W; y++)
				if (map[x][y] == 0 && next[x][y] == -1)
				{
					tot++;
					flood(x, y, tot);
				}

		for (int j = 1; j <= tot; j++)
			label[j] = ' ';

		char ch = 'a';
		for (int x = 0; x < H; x++)
			for (int y = 0; y < W; y++)
				if (label[map[x][y]] == ' ')
				{
					label[map[x][y]] = ch;
					ch++;
				}

		cout << "Case #" << i+1 << ":" << endl;
		for (int x = 0; x < H; x++)
		{
			for (int y = 0; y < W; y++)
			{
				if (y > 0) cout << " ";
				cout << label[map[x][y]];
			}
			cout << endl;
		}
	}
	return 0;
}