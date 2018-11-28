#include <stdio.h>

int T, H, W;
int map[100][100];
char map_s[100][100];

int direction[][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};

int getNext(int x, int y)
{
	int min_x = x;
	int min_y = y;
	for (int i = 0; i < 4; i++)
	{
		int now_x = x + direction[i][0];
		int now_y = y + direction[i][1];


		if (now_x >= 0 && now_x < H
				&& now_y >= 0 && now_y < W
				&& map[now_x][now_y] < map[min_x][min_y])
		{
			min_x = now_x;
			min_y = now_y;
		}
	}

	return (min_x << 16) + min_y;
}

int main()
{
	scanf("%d", &T);
	for (int i = 0; i < T; i++)
	{
		scanf("%d %d", &H, &W);
		for (int j = 0; j < H; j++)
		{
			for (int k = 0; k < W; k++)
			{
				scanf("%d", &map[j][k]);
				map_s[j][k] = ' ';
			}
		}

		char char_to_set = 'a';
		for (int j = 0; j < H; j++)
		{
			for (int k = 0; k < W; k++)
			{
				if (map_s[j][k] != ' ')
				{
					continue;
				}
				int start_x = j;
				int start_y = k;
				while (map_s[start_x][start_y] == ' ')
				{
					map_s[start_x][start_y] = char_to_set;
					int tmp = getNext(start_x, start_y);
					int now_x = tmp >> 16;
					int now_y = tmp & 0xFFFF;

					if (now_x == start_x && now_y == start_y)
					{
						char_to_set++;
						break;
					}
					else
					{
						if (map_s[now_x][now_y] == ' ')
						{
							start_x = now_x;
							start_y = now_y;
						}
						else
						{
							for (int m = 0; m < H; m++)
							{
								for (int n = 0; n < W; n++)
								{
									if (map_s[m][n] == char_to_set)
									{
										map_s[m][n] = map_s[now_x][now_y];
									}
								}
							}
							break;
						}
					}
				}
			}
		}

		printf("Case #%d:\n", i+1);
		for (int j = 0; j < H; j++)
		{
			printf("%c", map_s[j][0]);
			for (int k = 1; k < W; k++)
			{
				printf(" %c", map_s[j][k]);
			}
			printf("\n");
		}
	}
	return 0;
}
