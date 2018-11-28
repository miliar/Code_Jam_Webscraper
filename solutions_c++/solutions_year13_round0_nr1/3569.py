#include <iostream>
using namespace std;

char judgeWinner(char *line)
{
	char first = ('T'==line[0]) ? line[1] : line[0];
	for (int i=1; i<4; ++i)
	{
		if ('T' != line[i] && first != line[i])
			return 'D';
	}
	return ('.'==first) ? 'D' : first;
}

bool hasDot(char board[4][4])
{
	for (int i=0; i<4; ++i)
		for (int j=0; j<4; ++j)
			if ('.' == board[i][j])
				return true;
	return false;
}

void setCurrentLine (int flag, char board[4][4], char *line);

char searchWinner(char board[4][4])
{
	char line[4];
	char result = '.';
	for (int i=0; i<10; ++i)
	{
		setCurrentLine(i, board, line);
		result = judgeWinner(line);
		cout<<result<<endl;
		if ('X' == result || 'O' == result)
			return result;
	}
	return hasDot(board) ? '.' : result;
}

int main()
{
	int group = 0;
	char board[4][4];
	FILE* fInput = fopen("a.in", "r");
	FILE* fOut = fopen("a.out", "w");
	fscanf(fInput, "%d", &group);
	char winner = '.';
	for (int i=0; i<group; ++i)
	{
		fgetc(fInput);
		//fgets(board[0], 5, fInput);
		//fgets(board[1], 5, fInput);
		fscanf(fInput, "%c%c%c%c", &board[0][0], &board[0][1], &board[0][2], &board[0][3]);fgetc(fInput);
		fscanf(fInput, "%c%c%c%c", &board[1][0], &board[1][1], &board[1][2], &board[1][3]);fgetc(fInput);
		fscanf(fInput, "%c%c%c%c", &board[2][0], &board[2][1], &board[2][2], &board[2][3]);fgetc(fInput);
		fscanf(fInput, "%c%c%c%c", &board[3][0], &board[3][1], &board[3][2], &board[3][3]);fgetc(fInput);
		
		fprintf(fOut, "Case #%d: ", i+1);
		winner = searchWinner(board);
		if ('D' == winner)
			fprintf(fOut, "Draw");
		else if ('.' == winner)
			fprintf(fOut, "Game has not completed");
		else
			fprintf(fOut, "%c won", winner);
		fprintf(fOut, "\n");
	}
	fclose(fInput);
	fclose(fOut);
	
	return 0;
}

void setCurrentLine (int flag, char board[4][4], char *line)
{
	switch(flag)
	{
		case 0: 
			line[0]=board[0][0];
			line[1]=board[0][1];
			line[2]=board[0][2];
			line[3]=board[0][3];
			break;
		case 1: 
			line[0]=board[1][0];
			line[1]=board[1][1];
			line[2]=board[1][2];
			line[3]=board[1][3];
			break;
		case 2: 
			line[0]=board[2][0];
			line[1]=board[2][1];
			line[2]=board[2][2];
			line[3]=board[2][3];
			break;
		case 3: 
			line[0]=board[3][0];
			line[1]=board[3][1];
			line[2]=board[3][2];
			line[3]=board[3][3];
			break;
		case 4: 
			line[0]=board[0][0];
			line[1]=board[1][0];
			line[2]=board[2][0];
			line[3]=board[3][0];
			break;
		case 5: 
			line[0]=board[0][1];
			line[1]=board[1][1];
			line[2]=board[2][1];
			line[3]=board[3][1];
			break;
		case 6: 
			line[0]=board[0][2];
			line[1]=board[1][2];
			line[2]=board[2][2];
			line[3]=board[3][2];
			break;
		case 7: 
			line[0]=board[0][3];
			line[1]=board[1][3];
			line[2]=board[2][3];
			line[3]=board[3][3];
			break;
		case 8: 
			line[0]=board[0][0];
			line[1]=board[1][1];
			line[2]=board[2][2];
			line[3]=board[3][3];
			break;
		case 9: 
			line[0]=board[3][0];
			line[1]=board[2][1];
			line[2]=board[1][2];
			line[3]=board[0][3];
			break;
	}
}
