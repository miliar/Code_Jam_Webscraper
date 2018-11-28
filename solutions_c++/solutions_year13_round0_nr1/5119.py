#include<stdio.h>

#define UNKNOWN 0
#define GOING_ON 1
#define DRAW 2
#define O_WINS 3
#define X_WINS 4


int isCell(char tableCell, char value)
{
	if(tableCell == 'T' || tableCell==value)
		return 1;

	return 0;
}

int find_result(char table[4][4], int containEmpty)
{
	for(int h=0; h<4; h++)
	{
		if(isCell(table[h][0],'X') && isCell(table[h][1],'X') && isCell(table[h][2],'X') && isCell(table[h][3],'X'))
			return X_WINS;

		if(isCell(table[h][0],'O') && isCell(table[h][1],'O') && isCell(table[h][2],'O') && isCell(table[h][3],'O'))
			return O_WINS;

		if(isCell(table[0][h],'X') && isCell(table[1][h],'X') && isCell(table[2][h],'X') && isCell(table[3][h],'X'))
			return X_WINS;

		if(isCell(table[0][h],'O') && isCell(table[1][h],'O') && isCell(table[2][h],'O') && isCell(table[3][h],'O'))
			return O_WINS;
	}

	if(isCell(table[0][0],'X') && isCell(table[1][1],'X') && isCell(table[2][2],'X') && isCell(table[3][3],'X'))
		return X_WINS;
	if(isCell(table[0][3],'X') && isCell(table[1][2],'X') && isCell(table[2][1],'X') && isCell(table[3][0],'X'))
		return X_WINS;

	if(isCell(table[0][0],'O') && isCell(table[1][1],'O') && isCell(table[2][2],'O') && isCell(table[3][3],'O'))
		return O_WINS;
	if(isCell(table[0][3],'O') && isCell(table[1][2],'O') && isCell(table[2][1],'O') && isCell(table[3][0],'O'))
		return O_WINS;

	if(containEmpty)
		return GOING_ON;

	return DRAW;
}

int main()
{
	int N;

	FILE* fin = fopen("input.txt","r");
	FILE* fout = fopen("output.txt","w");

	fscanf(fin, "%d\n", &N);
	for(int h=0; h<N; h++)
	{
		int result = UNKNOWN;
		char table[4][4];

		for(int y=0; y<4; y++)
		{
			for(int x=0; x<4; x++)
			{
				fscanf(fin, "%c", &table[x][y]);
				if(table[x][y] == '.')
					result = GOING_ON;
			}
			fscanf(fin, "\n");			
		}
		fscanf(fin, "\n");

		result=find_result(table, result!=UNKNOWN);

		fprintf(fout, "Case #%d: ", h+1);
		switch(result)
		{
			case GOING_ON:
				fprintf(fout, "Game has not completed\n");
				break;
			case DRAW:
				fprintf(fout, "Draw\n");
				break;
			case O_WINS:
				fprintf(fout, "O won\n");
				break;
			case X_WINS:
				fprintf(fout, "X won\n");
				break;
		}		
	}
		
	fclose(fin);
	fclose(fout);	
}