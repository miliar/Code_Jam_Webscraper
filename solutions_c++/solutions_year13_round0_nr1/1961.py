#include <stdio.h>
int A[4][4], B[4][4];
int T;

int assess(char x)
{
	if (x == '.')	return 0;
	if (x == 'X')	return 1;
	if (x == 'O')	return 2;

	return -1;
}

void read()
{
	char a[10];

	gets(a);					//get rid of the endline symbol

	for (int i = 0; i < 4; i++)
	{
		gets(a);

		for (int j = 0; j < 4; j++)
		{
			A[i][j] = B[i][j] = assess(a[j]);

			if (A[i][j] == 2)	A[i][j] = 0;
			if (A[i][j] == -1)	A[i][j] = 1;

			if (B[i][j] == 1)	B[i][j] = 0;
			if (B[i][j] == -1)	B[i][j] = 2;
		}
	}
}

int checkGameState()
{
	//check diagonals

	if (A[0][0] * A[1][1] * A[2][2] * A[3][3] != 0)		return 1;
	if (A[0][3] * A[1][2] * A[2][1] * A[3][0] != 0)		return 1;

	if (B[0][0] * B[1][1] * B[2][2] * B[3][3] != 0)		return 2;
	if (B[0][3] * B[1][2] * B[2][1] * B[3][0] != 0)		return 2;

	//check lines & columns

	for (int i = 0; i < 4; i++)
	{
		if (A[i][0] * A[i][1] * A[i][2] * A[i][3] != 0)		return 1;
		if (B[i][0] * B[i][1] * B[i][2] * B[i][3] != 0)		return 2;

		if (A[0][i] * A[1][i] * A[2][i] * A[3][i] != 0)		return 1;
		if (B[0][i] * B[1][i] * B[2][i] * B[3][i] != 0)		return 2;
	}
	
	//check if game hasn't reached final stage yet

	int p = 0;

	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			if (A[i][j] || B[i][j])
				p++;

	if (p == 16)		return 0;

	return -1;
}

void solve(int number)
{
	int gameState = checkGameState();

	printf ("Case #%d: ", number);

	if (gameState == 1)		printf ("X won\n");
	if (gameState == 2)		printf ("O won\n");
	if (gameState == 0)		printf ("Draw\n");
	if (gameState == -1)	printf ("Game has not completed\n");
}

int main()
{
	freopen ("input.txt", "r", stdin);
	freopen ("output.txt", "w", stdout);

	scanf ("%d", &T);

	for (int t = 1; t <= T; t++)
	{
		read();
		solve(t);
	}

	return 0;
}