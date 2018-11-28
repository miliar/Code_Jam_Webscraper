#include <stdio.h>

char map[4][20];

void docase()
{
	int sx[10] = {0,1,2,3,0,0,0,0,3,0};
	int sy[10] = {0,0,0,0,0,1,2,3,0,0};
	int dx[10] = {0,0,0,0,1,1,1,1,-1,1};
	int dy[10] = {1,1,1,1,0,0,0,0,1,1};
	char playchar[2] = {'O', 'X'};

	int winner = -1;
	for (int player = 0; player < 2; player++)
	{
		for (int state = 0; state < 10; state++)
		{
			int x = sx[state];
			int y = sy[state];
			bool ok = true;
			for (int now = 0; now < 4; now++, x+= dx[state], y+=dy[state])
			{
				if (map[y][x] != playchar[player] && map[y][x] != 'T') ok = false;
			}

			if (ok)
			{
				winner = player;
			}
		}
	}

	if (winner == -1)
	{
		bool allfilled = true;
		for (int y = 0; y < 4; y++)
		{
			for (int x = 0; x < 4; x++)
			{
				allfilled &= map[y][x] != '.';
			}
		}

		if (allfilled) printf("Draw\n");
		else
			printf("Game has not completed\n");
	}
	else
		printf("%c won\n", playchar[winner]);
}

int main()
{
	int T;
	scanf("%d", &T);

	for (int i = 0; i < T; i++)
	{
		for (int y = 0; y < 4; y++)
		{
			scanf("%s", map[y]);
		}

		printf("Case #%d: ", i + 1);
		docase();
	}
}