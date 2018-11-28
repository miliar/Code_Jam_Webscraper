#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#define NMAX 5
#define LMAX 131
#define WinValue 4
#define TotalElems 16
using namespace std;
string line;
int tests;
char A[NMAX][NMAX];
int whoWon, mapping[LMAX];

inline int checkLine(int i, char value)
{
	int j, res = 0;
	for (j = 1; j < NMAX; j++)
		if (A[i][j] == value || A[i][j] == 'T')
			res++;
		
	return res;
}

inline int checkColumn(int j, char value)
{
	int i, res = 0;
	for (i = 1; i < NMAX; i++)
		if (A[i][j] == value || A[i][j] == 'T')
			res++;
		
	return res;
}

inline int checkFirstDiagonal(int i, int j, char value)
{
	int res = 0, i2 = i, j2 = j;
	while (i2 && j2)
	{
		if (A[i2][j2] == value || A[i2][j2] == 'T')
			res++;
		
		i2--; j2--;
	}
	
	i2 = i + 1; j2 = j + 1;
	while (i2 < NMAX && j2 < NMAX)
	{
		if (A[i2][j2] == value || A[i2][j2] == 'T')
			res++;
		
		i2++; j2++;
	}
	
	return res;
}

inline int checkSecondDiagonal(int i, int j, char value)
{
	int res = 0, i2 = i, j2 = j;
	while (i2 < NMAX && j2)
	{
		if (A[i2][j2] == value || A[i2][j2] == 'T')
			res++;
		
		i2++; j2--;
	}
	
	i2 = i - 1; j2 = j + 1;
	while (i2 && j2 < NMAX)
	{
		if (A[i2][j2] == value || A[i2][j2] == 'T')
			res++;
		
		i2--; j2++;
	}
	
	return res;
}

int main()
{
	freopen("input", "r", stdin);
	freopen("output", "w", stdout);
	scanf("%d", &tests);
	mapping['X'] = 1; mapping['O'] = 2;
	
	int i, j, k, nrElems;
	for (i = 1; i <= tests; i++)
	{
		nrElems = 0;
		for (j = 1; j < NMAX; j++)
		{
			cin >> line;
			for (k = 1; k < NMAX; k++)
			{
				A[j][k] = line[k - 1];
				if (A[j][k] == 'X' || A[j][k] == 'O' || A[j][k] == 'T')
					nrElems++;
			}
		}
		
		whoWon = 0;
		for (j = 1; j < NMAX; j++)
		{
			for (k = 1; k < NMAX; k++)
				if (A[j][k] == 'X' || A[j][k] == 'O')
				{
					//check line
					if (checkLine(j, A[j][k]) == WinValue || 
						checkColumn(k, A[j][k]) == WinValue ||
						checkFirstDiagonal(j, k, A[j][k]) == WinValue || 
						checkSecondDiagonal(j, k, A[j][k]) == WinValue)
					{
						whoWon = mapping[A[j][k]];
						break ;
					}
				}					
		}
		
		printf("Case #%d: ", i);
		
		if (whoWon == 0 && nrElems == TotalElems)
		{
			printf("Draw\n");
			continue ;
		}
		
		if (whoWon == 0)
		{
			printf("Game has not completed\n");
			continue ;
		}
		
		if (whoWon == 1)
		{
			printf("X won\n");
			continue ;
		}
		
		printf("O won\n");
	}
	return 0;
}
