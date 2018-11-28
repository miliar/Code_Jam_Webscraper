#include <stdio.h>

using namespace std;

#define XWON 1
#define OWON 2
#define DRAW 3
#define NOTC 4

#define NOTFOUND 1

char mat[4][10];


int checksymbol (char ch)
{
	int d1flag = !NOTFOUND;
	int d2flag = !NOTFOUND;

	for (int i = 0; i < 4; i++)
	{
		int j;

		for (j = 0; j < 4; j++)
		{
			if (ch != mat[i][j] && mat[i][j] != 'T')
				break;
		}
		if (j == 4)
			return 1;

		for (j = 0; j < 4; j++)
		{
			if (ch != mat[j][i] && mat[j][i] != 'T')
				break;
		}
		if (j == 4)
			return 1;

		if (ch != mat[i][i] && mat[i][i] != 'T')
		{
			d1flag = NOTFOUND;
		}

		if (ch != mat[i][3-i] && mat[i][3-i] != 'T')
		{
			d2flag = NOTFOUND;
		}
	}
	if (d1flag != NOTFOUND || d2flag != NOTFOUND)
		return 1;

	return 0;
}

int checkspace(void)
{
	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			if (mat[i][j] == '.')
				return 1;
	return 0;
}

int check_solution (void)
{
	if (checksymbol('X'))
		return XWON;
	if (checksymbol('O'))
		return OWON;

	if (checkspace())
		return NOTC;
	return DRAW;
}

int main (int argc, char *argv[])
{
	FILE *ifp, *ofp;

	ifp = fopen(argv[1], "r");
	ofp = fopen(argv[2], "w");

	if (ifp == NULL || ofp == NULL)
		return 0;

	int T;
	fscanf (ifp, "%d\n", &T);

	for (int i = 1; i <= T; i++)
	{
		int j;
		for (j = 0; j < 4; j++)
			fgets(mat[j], 10, ifp);
		fgets(mat[j], 10, ifp); //removing waste line

		int retVal = check_solution();

		if (retVal == XWON)
		{
			fprintf (ofp, "Case #%d: X won\n", i);
			printf("Case #%d: X won\n", i);
		}
		else if (retVal == OWON)
		{
			fprintf (ofp, "Case #%d: O won\n", i);
			printf("Case #%d: O won\n", i);
		}
		else if (retVal == DRAW)
		{
			fprintf (ofp, "Case #%d: Draw\n", i);
			printf("Case #%d: Draw\n", i);
		}
		else	
		{
			fprintf (ofp, "Case #%d: Game has not completed\n", i);
			printf("Case #%d: Game has not completed\n", i);
		}
	}
}