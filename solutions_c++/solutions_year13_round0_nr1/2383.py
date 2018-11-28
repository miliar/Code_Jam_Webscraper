#include <stdio.h>
#include <string.h>

int n;
char data[10][10];

void inputData()
{
	for (int i = 0; i < 4; ++ i)
	{
		scanf("%s", &data[i]);
	}
}

inline bool isValid(char src, char tag)
{
	return (src == 'T' || src == tag);
}

bool checkRow(int row, char tag)
{
	for (int i = 0; i < 4; ++ i)
	{
		if (!isValid(data[row][i], tag))
		{
			return false;
		}
	}
	
	return true;
}

bool checkCol(int col, char tag)
{
	for (int i = 0; i < 4; ++ i)
	{
		if (!isValid(data[i][col], tag))
		{
			return false;
		}
	}
	
	return true;
}

bool checkDiag(char tag)
{
	if (isValid(data[0][0], tag) &&
		isValid(data[1][1], tag) &&
		isValid(data[2][2], tag) &&
		isValid(data[3][3], tag))
	{
		 return true;
	}
	
	if (isValid(data[0][3], tag) &&
		isValid(data[1][2], tag) &&
		isValid(data[2][1], tag) &&
		isValid(data[3][0], tag))
	{
		 return true;
	}

	return false;
}

bool checkRole(char tag)
{
	for (int i = 0; i < 4; ++ i)
	{
		if (checkRow(i, tag))
		{
			return true;
		}
	}
	
	for (int i = 0; i < 4; ++ i)
	{
		if (checkCol(i, tag))
		{
			return true;
		}
	}
	
	return checkDiag(tag);
}

bool checkEmpty()
{
	for (int i = 0; i < 4; ++ i)
	{
		for (int j = 0; j < 4; ++ j)
		{
			if (data[i][j] == '.')
			{
				return true;
			}
		}
	}

	return false;
}

void process(int cases)
{
	if (checkRole('X'))
	{
		printf("Case #%u: X won\n", cases);
	}
	else if (checkRole('O'))
	{
		printf("Case #%u: O won\n", cases);
	}
	else if (checkEmpty())
	{
		printf("Case #%u: Game has not completed\n", cases);
	}
	else
	{
		printf("Case #%u: Draw\n", cases);
	}
}

int main()
{
	//freopen("A-large.in", "r", stdin);
	//freopen("out.txt", "w", stdout);

	scanf("%d", &n);
	for (int i = 0; i < n; ++ i)
	{
		inputData();
		process(i + 1);
	}
	return 0;
}