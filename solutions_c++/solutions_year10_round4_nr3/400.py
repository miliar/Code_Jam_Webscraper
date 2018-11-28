#include <cstdio>
#include <memory>

int mas[110][110];

bool Empty()
{
	for (int i=0; i<110; i++)
	{
		for (int j=0; j<110; j++)
		{
			if (mas[i][j])
				return false;
		}
	}
	return true;
}

int Step(int x, int y)
{
	if (mas[x][y])
	{
		if (mas[x-1][y] == 0 && mas[x][y-1] == 0)
			return 0;
	}
	else
	{
		if (mas[x-1][y] == 1 && mas[x][y-1] == 1)
			return 1;
	}
	return mas[x][y];
}

void NextStep()
{
	for (int i=109; i>0; i--)
	{
		for (int j=109; j>0; j--)
		{
			mas[i][j] = Step(i,j);
		}
	}
}

void Print()
{
	for (int i=0; i<10; i++)
	{
		for (int j=0; j<10; j++)
		{
			printf("%d", mas[i][j]);
		}
		printf("\n");
	}
}

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out.txt", "w", stdout);
	int C;
	scanf("%d", &C);
	for (int c=1; c<=C; c++)
	{
		int R;
		scanf("%d", &R);
		for (int i=0; i<R; i++)
		{
			int x1,y1,x2,y2;
			scanf("%d%d%d%d", &x1,&y1,&x2,&y2);
			for (int x=x1; x<=x2; x++)
			{
				for (int y=y1; y<=y2; y++)
				{
					mas[x][y] = 1;
				}
			}
		}
		int steps = 0;
		//Print();
		while (Empty() == false)
		{
			steps++;
			NextStep();
			//printf("%d\n", steps);
			//Print();
		}
		printf("Case #%d: %d\n", c, steps);
	}
	return 0;
}