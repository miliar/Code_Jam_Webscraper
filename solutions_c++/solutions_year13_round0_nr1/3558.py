#include <stdio.h>
FILE	*in = fopen("input", "r"),
		*out= fopen("output", "w");


char mat[4][4];
char next_result()
{
	char chr;
	int i, j;
	bool not_complete_possible = false;

	for(i = 0; i < 4; i++)
	{
		for(j = 0; j < 4; j++)
		{
			fscanf(in, "%c", &chr);
			if(chr == 'X')
				mat[i][j] = 1;
			else if(chr == 'O')
				mat[i][j] = 2;
			else if(chr == 'T')
				mat[i][j] = 3;
			else // it's a point ('.') it can't be complete
			{
				mat[i][j] = 0;
				not_complete_possible = true;
			}
		}
		fscanf(in, "\n");
	}

	char and_result;
	for(i = 0; i < 4; i++)
	//checking if any row is a winning one
	{
		and_result = 3;
		for(j = 0; j < 4; j++)
			and_result &= mat[i][j];

		if(and_result & 1)
			return 'X';
		else if(and_result & 2)
			return 'O';
	}
	for(i = 0; i < 4; i++)
	//checking if any column is a winning one
	{
		and_result = 3;
		for(j = 0; j < 4; j++)
			and_result &= mat[j][i];

		if(and_result & 1)
			return 'X';
		else if(and_result & 2)
			return 'O';
	}

	//checking if any diagonal is a winning one
	and_result = 3;
	for(i = 0; i < 4; i++)
		and_result &= mat[i][i];
	if(and_result & 1)
		return 'X';
	else if(and_result & 2)
		return 'O';

	//checking if any diagonal is a winning one
	and_result = 3;
	for(i = 0; i < 4; i++)
		and_result &= mat[i][3-i];
	if(and_result & 1)
		return 'X';
	else if(and_result & 2)
		return 'O';

	if(not_complete_possible)
		return 'F';
	return 'D';
}

int main()
{
	int T;
	char res;
	fscanf(in, "%i\n", &T);
	int i;
	for(i = 1; i <= T; i++)
	{
		res = next_result();
		fprintf(out, "Case #%i: ", i);
		switch(res)
		{
			case 'X': fprintf(out, "X won\n"); break;
			case 'O': fprintf(out, "O won\n"); break;
			case 'D': fprintf(out, "Draw\n"); break;
			case 'F': fprintf(out, "Game has not completed\n"); break;
		}
	}
}
