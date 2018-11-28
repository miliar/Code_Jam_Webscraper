#include <stdio.h>

const int d[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};

int rows, cols;
int alt[102][102];
char label[102][102];
char sinklabel;

void Init()
{
	scanf("%d %d", &rows, &cols);
	int i, k;
	for(i=0; i<rows+2; i++)
	{
		alt[i][0] = alt[i][cols+1] = 10000;
	}
	for(i=0; i<cols+2; i++)
	{
		alt[0][i] = alt[rows+1][i] = 10000;
	}
	for(i=1; i<=rows; i++)
	{
		for(k=1; k<=cols; k++)
		{
			scanf("%d", &alt[i][k]);
			label[i][k] = 0;
		}
	}
	sinklabel = 'a';
}

inline bool Sink(int row, int col)
{
	int i;
	for(i=0; i<4; i++)
	{
		if(alt[row+d[i][0]][col+d[i][1]] < alt[row][col])
			return false;
	}
	return true;
}

void Print()
{
	int i, k;
	for(i=1; i<=rows; i++)
	{
		for(k=1; k<=cols; k++)
		{
			printf("%d ", alt[i][k]);
		}
		printf("\n");
	}
	for(i=1; i<=rows; i++)
	{
		for(k=1; k<=cols; k++)
		{
			printf("%d ", label[i][k]);
		}
		printf("\n");
	}
}

char DFS(int row, int col)
{
	if(!label[row][col])
	{
		if(Sink(row, col))
			label[row][col] = sinklabel++;
		else
		{
			int i, curalt = alt[row][col], direction;
			for(i=0; i<4; i++)
			{
				if(alt[row+d[i][0]][col+d[i][1]] < curalt)
				{
					curalt = alt[row+d[i][0]][col+d[i][1]];
					direction = i;
				}
			}
			label[row][col] = DFS(row+d[direction][0], col+d[direction][1]);
		}
	}
	return label[row][col];
}

void Label()
{
	int i, k;
	for(i=1; i<=rows; i++)
	{
		for(k=1; k<=cols; k++)
		{
			DFS(i, k);
			printf("%c ", label[i][k]);
		}
		printf("\n");
	}
}

int main() 
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
    int cases;
	scanf("%d", &cases);
	int i;
	for(i=1; i<=cases; i++)
	{
		Init();
//		FindSink();
//		Print();
		printf("Case #%d:\n", i);
		Label();
	}
	return 0;
}