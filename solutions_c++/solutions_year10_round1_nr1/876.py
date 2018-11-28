// CodeJam1A_1.cpp : Defines the entry point for the console application.
//

#define _CRT_SECURE_NO_WARNINGS
#include "stdio.h"

typedef enum
{
	empty,
	red,
	blue
};

void print_grid(int ppnGrid[50][50], int N)
{
	for (int y = 0; y < N; y++)
	{
		for (int x = 0; x < N; x++)
			printf("%d ", ppnGrid[x][y]);

		printf("\n");
	}

	printf("\n");
}

int check_line(int ppnGrid[50][50], int N, int K, int color, int x, int y, int dx, int dy)
{
	for (int i = 1; i < K; i++)
	{
		x += dx;
		y += dy;

		if (x < 0 || x > N - 1 || y < 0 || y > N - 1)
			return (0);

		if (ppnGrid[x][y] != color)
			return (0);
	}

	return (1);
}

int check_k(int ppnGrid[50][50], int N, int K, int color)
{
	for (int x = 0; x < N; x++)
		for (int y = 0; y < N; y++)
			if (ppnGrid[x][y] == color)
			{
				if (check_line(ppnGrid, N, K, color, x, y, 1, 0) == 1)
					return (1);

				if (check_line(ppnGrid, N, K, color, x, y, 0, 1) == 1)
					return (1);

				if (check_line(ppnGrid, N, K, color, x, y, -1, 1) == 1)
					return (1);

				if (check_line(ppnGrid, N, K, color, x, y, 1, 1) == 1)
					return (1);
			}

	return (0);
}

int main(int argc, char *argv[])
{
	FILE
		*fpi = fopen("A-large.in", "r"),
		*fpo = fopen("A-large.out", "w");

	int
		T,
		N,
		K,
		ppnGrid[50][50],
		score;

	char
		szLine[51];

	fscanf(fpi, "%d", &T);

	for (int i = 0; i < T; i++)
	{
		fscanf(fpi, "%d", &N);
		fscanf(fpi, "%d", &K);

		for (int j = 0; j < N; j++)
		{
			fscanf(fpi, "%s", szLine);
			for (int k = 0; k < N; k++)
			{
				switch (szLine[k])
				{
					case '.': ppnGrid[N - j - 1][k] = empty; break;
					case 'R': ppnGrid[N - j - 1][k] = red; break;
					case 'B': ppnGrid[N - j - 1][k] = blue; break;
				}
			}
		}

		for (int j = 0; j < N; j++)
			for (int s = 0; s < N; s++)
				for (int k = N - 1; k > -1; k--)
					if (ppnGrid[j][k] == empty)
					{
						for (int l = k - 1; l > -1; l--)
							ppnGrid[j][l + 1] = ppnGrid[j][l];

						ppnGrid[j][0] = empty;
					}

		score = check_k(ppnGrid, N, K, red) * 10 + check_k(ppnGrid, N, K, blue);
		switch (score)
		{
			case 11: fprintf(fpo, "Case #%d: Both\n", i + 1); break;
			case 10: fprintf(fpo, "Case #%d: Red\n", i + 1); break;
			case 01: fprintf(fpo, "Case #%d: Blue\n", i + 1); break;
			case 00: fprintf(fpo, "Case #%d: Neither\n", i + 1); break;
		}
	}

	return 0;
}
