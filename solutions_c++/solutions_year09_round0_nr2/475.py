#include <cstdio>

struct point
{
	int x, y;
	point(int a, int b)
	{
		x = a;
		y = b;
	}
	point () {}
};

int h, w;
int map[100][100];
int drain[100][100];
int dx[4] = {-1, 0, 0, 1};
int dy[4] = {0, -1, 1, 0};

bool valid(int x, int y)
{
	if (x < 0)
		return 0;
	if (x >= h)
		return 0;
	if (y < 0)
		return 0;
	if (y >= w)
		return 0;
	return 1;
}

bool sink(int x, int y)
{
	int i;
	for (i = 0; i < 4; i++)
		if (valid(x+dx[i], y+dy[i]))
			if (map[x+dx[i]][y+dy[i]] < map[x][y])
				return 0;
	return 1;
}

int dto(int x, int y)
{
	int min = 9999999;
	int bestd;
	int i;
	for (i = 0; i < 4; i++)
		if (valid(x+dx[i], y+dy[i]) && map[x+dx[i]][y+dy[i]] < min)
		{
			min = map[x+dx[i]][y+dy[i]];
			bestd = i;
		}
	return bestd;
}

int follow(int x, int y)
{
	if (drain[x][y])
		return drain[x][y];
	int d = dto(x, y);
	drain[x][y] = follow(x+dx[d], y+dy[d]);
	return drain[x][y];
}

int main()
{
	FILE* input = fopen("drain.in", "r");
	FILE* output = fopen("drain.out", "w");
	int n;
	int i;
	fscanf(input, "%d", &n);
	for (i = 0; i < n; i++)
	{
		fscanf(input, "%d %d", &h, &w);
		int j, k;
		int s = 0;
		for (j = 0; j < h; j++)
			for (k = 0; k < w; k++)
			{
				fscanf(input, "%d", &map[j][k]);
				drain[j][k] = 0;
			}
		for (j = 0; j < h; j++)
			for (k = 0; k < w; k++)
				if (sink(j, k))
				{
					s++;
					drain[j][k] = s;
				}
		for (j = 0; j < h; j++)
			for (k = 0; k < w; k++)
				if (!drain[j][k])
					follow(j, k);
		fprintf(output, "Case #%d: \n", i+1);
		char which[30];
		for (j = 0; j < 30; j++)
			which[j]  = 0;
		char letter = 'a';
		for (j = 0; j < h; j++)
		{
			for (k = 0; k < w; k++)
			{
				if (!which[drain[j][k]])
				{
					which[drain[j][k]] = letter;
					letter++;
				}
				fprintf(output, "%c ", which[drain[j][k]]);
			}
			fprintf(output, "\n");
		}
	}
}