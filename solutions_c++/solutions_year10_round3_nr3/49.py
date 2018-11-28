#include <cstdio>
#include <cstdlib>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>

using namespace std;

struct square
{
	int row;
	int col;
	int size;
	friend bool operator < (square a, square b)
	{
		return a.size == b.size? (a.row == b.row? a.col < b.col: a.row < b.row) : a.size > b.size;
	}
};

int best_square[513][513][2];
int total[513];
int m, n;
int board[512][512];
char hex[16] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'};
int bad[512][512];
square all[262144];

void fillIn(int row, int col, char what)
{
	int i, j;
	for (i = 0; hex[i] != what; i++);
	for (j = 3; j >= 0; j--)
	{
		board[row][col*4+j] = i%2;
		i/=2;
	}
}

int getBest(int row, int col)
{
	return 1+min(best_square[row+1][col][!board[row][col]], min(best_square[row][col+1][!board[row][col]], best_square[row+1][col+1][board[row][col]]));
}

void clear()
{
	int i, j;
	for (i = 0; i < 512; i++)
	{
		for (j = 0; j < 512; j++)
		{
			best_square[i][j][0] = 0;
			best_square[i][j][1] = 0;
			bad[i][j] = 0;
		}
		total[i] = 0;
	}
	total[512] = 0;
}

void makeBad(square what)
{
	int i, j;
	for (i = 0; i < what.size; i++)
		for (j = 0; j < what.size; j++)
			bad[i+what.row][j+what.col] = 1;
}

void show(int s)
{
	int i, j;
	printf("\n");
	for (i = 0; i < s; i++)
		printf("%d ", all[i].size);
	printf("\n");
}

bool isBad(square what)
{
	int i, j;
	for (i = 0; i < what.size; i++)
		for (j = 0; j < what.size; j++)
			if (bad[what.row+i][what.col+j])
				return 1;
	return 0;
}

int doDP()
{
	int j, k;
	int s = 0;
	for (j = m-1; j >= 0; j--) 
	{
		for (k = n-1; k >= 0; k--)
		{
			best_square[j][k][board[j][k]] = bad[j][k]? 0: getBest(j, k);
			all[s].row = j;
			all[s].col = k;
			all[s].size = best_square[j][k][board[j][k]];
			s++;
		}
	}
	return s;
}

int main()
{
	int t;
	int i, j, k;
	char temp;
	scanf("%d", &t);
	for (i = 0; i < t; i++)
	{
		scanf("%d %d\n", &m, &n);
		for (j = 0; j < m; j++)
		{
			for (k = 0; k < n / 4; k++)
			{
				scanf("%c\n", &temp);
				fillIn(j, k, temp);
			}
		}
		clear();
		int s = doDP();
		sort(all, all+s);
		while (all[0].size != 0) 
		{	
			for (j = 0; j < s && all[j].size == all[0].size; j++) 
			{
				if (!isBad(all[j])) 
				{
					total[all[j].size]++;
					makeBad(all[j]);
				}
			}
			s = doDP();
			sort(all, all+s);
		}
		int count = 0;
		for (j = 0; j < 513; j++)
			count+=(total[j] > 0);
		printf("Case #%d: %d\n", i+1, count);
		for (j = 512; j > 0; j--)
			if (total[j] > 0)
				printf("%d %d\n", j, total[j]);
	}
	
}