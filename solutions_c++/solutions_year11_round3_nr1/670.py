#include<stdio.h>

#define MAX_H 51
#define MAX_W 51

char Matrix[MAX_H][MAX_W];
int H, W;
int firstR, firstC;

void leerEntrada()
{
	scanf("%d %d\n", &H, &W);
	for (int r = 0; r < H; r++)
	{
		for (int c = 0; c < W; c++)
			scanf("%c", &(Matrix[r][c]));
		scanf("\n");
	}
}

void findFirst()
{
	for (int r = 0; r < H; r++)
		for (int c = 0; c < W; c++)
			if (Matrix[r][c] == '#')
			{
				firstR=r;
				firstC=c;
				return;
			}
	firstR=-1;
	firstC=-1;
	return;
}

void show_matrix()
{
	for (int r = 0; r < H; r++)
	{
		for (int c = 0; c < W; c++)
			printf("%c", Matrix[r][c]);
		printf("\n");
	}
	return;
}

int go()
{
	while (true)
	{
		findFirst();
		if (firstR == -1) return 0;
		if (firstR + 1 >= H) return -1;
		if (firstC + 1 >= W) return -1;
		if (Matrix[firstR][firstC + 1] != '#') return -1;
		if (Matrix[firstR + 1][firstC] != '#') return -1;
		if (Matrix[firstR + 1][firstC + 1] != '#') return -1;
		Matrix[firstR][firstC] = '/';
		Matrix[firstR][firstC + 1] = '\\';
		Matrix[firstR + 1][firstC] = '\\';
		Matrix[firstR + 1][firstC + 1] = '/';
	}
}

int main(void)
{
	int T;
	scanf("%d\n", &T);
	for (int t = 1; t <= T; t++)
	{
		leerEntrada();
		int ret = go();
		printf("Case #%d:\n", t);
		if (ret != -1)
			show_matrix();
		else
			printf("Impossible\n");
	}
}