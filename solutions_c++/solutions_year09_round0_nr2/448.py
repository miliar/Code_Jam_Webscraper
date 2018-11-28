#include <iostream>

using namespace std;
int T, H, W;
char Now;
char map[128][128];
int att[128][128];

int dir[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
char mark(int i, int j)
{
	if (map[i][j] != 0) return map[i][j];

	int m = 1000000000;
	int my_d;
	int ii, jj;
	for (int d = 0; d < 4; d++)
	{
		ii = i + dir[d][0];
		jj = j + dir[d][1];
		if (ii >= 0 && ii < H && jj >= 0 && jj < W)
		{
			if (att[ii][jj] < m)
			{
				m = att[ii][jj];
				my_d = d;
			}
		}
	}
	ii = i + dir[my_d][0];
	jj = j + dir[my_d][1];
	if (att[ii][jj] >= att[i][j])
	{
		map[i][j] = Now;
		return Now++;
	}

	map[i][j] = mark(ii, jj);
	return map[i][j];
	

}
int main()
{

	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &T);
	for (int i = 0; i < T; i++)
	{
		scanf("%d%d", &H, &W);
		for (int i = 0; i <H; i++)
		{
			for (int j = 0; j < W; j++)
			{
				scanf("%d", &att[i][j]);
			}
		}

		memset(map, 0, sizeof(map));
		Now = 'a';
		for (int i = 0; i < H; i++)
		{
			for (int j = 0; j <  W; j++)
			{
				if (map[i][j] == 0)
				{
					mark(i, j);

				}
			}

			
		}

		printf("Case #%d:\n", i+1);
		for (int p = 0; p < H; p++)
			{
				for (int q = 0; q < W; q++)
				{
					printf("%c", map[p][q]);
					if (q < W-1)
						printf(" ");
				}
				printf("\n");
			}
	}
	

}