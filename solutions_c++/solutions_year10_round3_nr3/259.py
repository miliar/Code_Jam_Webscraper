#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

FILE
	*fpi = fopen("C-small.in", "r"),
	*fpo = fopen("C-small.out", "w");

int
	T,
	M,
	N,
	grid[512][512],
	boards[513],
	diff;

char
	s[513],
	c;

void print_grid()
{
	for (int y = 0; y < M; y++)
	{
		for (int x = 0; x < N; x++)
			printf("%d ", grid[x][y]);

		printf("\n");
	}

	printf("\n");
}

int find_largest(int x, int y, int size)
{
	if (x + size >= N)
		return (size);

	if (y + size >= M)
		return (size);

	for (int i = 0; i < size; i++)
		if (grid[x + size][y + i] != 3 - grid[x + size - 1][y + i])
			return (size);

	for (int i = 0; i < size + 1; i++)
		if (grid[x + i][y + size] != 3 - grid[x + i][y + size - 1])
			return (size);

	size++;
	return (find_largest(x, y, size));
}

bool cut_largest_board()
{
	int
		largest = -1,
		bestx,
		besty,
		curr_size;

	for (int y = 0; y < M; y++)
		for (int x = 0; x < N; x++)
			if (grid[x][y])
			{
				curr_size = find_largest(x, y, 1);
				if (largest == -1 || curr_size > largest)
				{
					largest = curr_size;
					bestx = x;
					besty = y;
				}
			}

	if (largest > 0)
	{
		for (int x = 0; x < largest; x++)
			for (int y = 0; y < largest; y++)
				grid[bestx + x][besty + y] = 0;

		if (!boards[largest])
			diff++;

		boards[largest]++;
		return (true);
	}

	return (false);
}

void cut_boards()
{
	diff = 0;
	for (int i = 0; i < 512; i++)
		boards[i] = 0;

	while (cut_largest_board())
		;
}

int main(int argc, char *argv[])
{
	fscanf(fpi, "%d", &T);
	for (int i = 0; i < T; i++)
	{
		fscanf(fpi, "%d", &M);
		fscanf(fpi, "%d", &N);
		for (int j = 0; j < M; j++)
		{
			fscanf(fpi, "%s", s);
			for (int k = 0; k < N / 4; k++)
			{
				c = s[k];
				c = c >= 'A' ? 10 + c - 'A' : c - '0';
				for (int l = 0; l < 4; l++)
					grid[k * 4 + l][j] = (c & (1 << (3 - l))) ? 1 : 2;
			}
		}

		cut_boards();
		fprintf(fpo, "Case #%d: %d\n", i + 1, diff);
		for (int j = 512; j > 0; j--)
			if (boards[j])
				fprintf(fpo, "%d %d\n", j, boards[j]);
	}

	fclose(fpi);
	fclose(fpo);
	return 0;
}
