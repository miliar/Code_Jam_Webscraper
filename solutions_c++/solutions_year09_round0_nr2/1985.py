#include <stdio.h>
#include <memory.h>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int matr[100][100];
char result[100][110];
int hist[20000][2];
int T, H, W;
int dir[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};

int main()
{
	freopen("output.txt", "w", stdout);
	scanf("%d", &T);
	for (int t = 0; t < T; t++)
	{
		char c = 'a';
		scanf("%d%d", &H, &W);
		for (int i = 0; i < H; i++)
			for (int j = 0; j < W; j++)
				scanf("%d", &matr[i][j]);
		memset(result, 0, sizeof(char) * 100 * 110);

		for (int j = 0; j < W; j++)
			for (int i = 0; i < H; i++)
			{
				int x = i;
				int y = j;
				int h = 0;
				while (result[x][y] == 0)
				{
					hist[h][0] = x;
					hist[h][1] = y;
					h++;
					int mx = x;
					int my = y;
					int mn = matr[x][y];
					for (int d = 0; d < 4; d++)
					{
						int xx = x + dir[d][0];
						int yy = y + dir[d][1];
						if (xx >= 0 && xx < H && yy >= 0 && yy < W && matr[xx][yy] < mn)
						{
							mn = matr[xx][yy];
							mx = xx;
							my = yy;
						}
					}
					if (mx != x || my != y)
					{
						x = mx;
						y = my;
					}
					else
					{
						result[x][y] = c;
						c++;
						break;
					}
				}
				for (int k = 0; k < h; k++)
					result[hist[k][0]][hist[k][1]] = result[x][y];
			}
		printf("Case #%d:\n", t + 1);
		for (int i = 0; i < H; i++)
		{
			printf("%c", result[i][0]);
			for (int j = 1; j < W; j++)
				printf(" %c", result[i][j]);
			printf("\n");
		}
	}
	fclose(stdout);

	return 0;
}