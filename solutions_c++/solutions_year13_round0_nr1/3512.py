#include<stdio.h>
#include<string.h>
#define MAXN 1000

char board[4][4];
FILE *in;
FILE *out;
int result[MAXN];

int main(){

	int i, j, t;
	int x = 0, o = 0;

	int dotc = 0;

	in = fopen("A-large.in", "r");
	out = fopen("A-large.out", "w");

	fscanf(in, "%d", &t);

	for(j=0 ; j<t ; j++){
		memset(board, NULL, 16*sizeof(char));
		for(i=0 ; i<4 ; i++)
			fscanf(in, "%s", &board[i]);
		for(i=0 ; i<4 ; i++){
			//가로
			if( (board[i][0] == 'O' || board[i][0] == 'T') && (board[i][1] == 'O' || board[i][1] == 'T') && (board[i][2] == 'O' || board[i][2] == 'T') && (board[i][3] == 'O' || board[i][3] == 'T'))
				o = 1;
			if( (board[i][0] == 'X' || board[i][0] == 'T') && (board[i][1] == 'X' || board[i][1] == 'T') && (board[i][2] == 'X' || board[i][2] == 'T') && (board[i][3] == 'X' || board[i][3] == 'T'))
				x = 1;
			//세로
			if( (board[0][i] == 'O' || board[0][i] == 'T') && (board[1][i] == 'O' || board[1][i] == 'T') && (board[2][i] == 'O' || board[2][i] == 'T') && (board[3][i] == 'O' || board[3][i] == 'T'))
				o = 1;
			if( (board[0][i] == 'X' || board[0][i] == 'T') && (board[1][i] == 'X' || board[1][i] == 'T') && (board[2][i] == 'X' || board[2][i] == 'T') && (board[3][i] == 'X' || board[3][i] == 'T'))
				x = 1;
			//대각선
			if( (board[0][0] == 'O' || board[0][0] == 'T') && (board[1][1] == 'O' || board[1][1] == 'T') && (board[2][2] == 'O' || board[2][2] == 'T') && (board[3][3] == 'O' || board[3][3] == 'T'))
				o = 1;
			if( (board[0][0] == 'X' || board[0][0] == 'T') && (board[1][1] == 'X' || board[1][1] == 'T') && (board[2][2] == 'X' || board[2][2] == 'T') && (board[3][3] == 'X' || board[3][3] == 'T'))
				x = 1;
			if( (board[3][0] == 'O' || board[3][0] == 'T') && (board[2][1] == 'O' || board[2][1] == 'T') && (board[1][2] == 'O' || board[1][2] == 'T') && (board[0][3] == 'O' || board[0][3] == 'T'))
				o = 1;
			if( (board[3][0] == 'X' || board[3][0] == 'T') && (board[2][1] == 'X' || board[2][1] == 'T') && (board[1][2] == 'X' || board[1][2] == 'T') && (board[0][3] == 'X' || board[0][3] == 'T'))
				x = 1;
		}
		if(o == 1)
			result[j] = 1; // O가 이김

		else if(x == 1)
			result[j] = 2; // X가 이김

		else{
			for(i=0 ; i<4 ; i++){
				if(board[0][i] == '.')
					dotc = 1;
				if(board[1][i] == '.')
					dotc = 1;
				if(board[2][i] == '.')
					dotc = 1;
				if(board[3][i] == '.')
					dotc = 1;
			}
			if(dotc == 1)
				result[j] = 3; // 게임안끝남
			else
				result[j] = 4; // 비김
		}
		o = 0;
		x = 0;
		dotc = 0;
	}
	for(j=0 ; j<t ; j++){
		fprintf(out, "Case #%d: ", j+1);
		switch(result[j]){
		case 1 :
			fprintf(out, "O won\n");
			break;
		case 2 : 
			fprintf(out, "X won\n");
			break;
		case 3 :
			fprintf(out, "Game has not completed\n");
			break;
		case 4 : 
			fprintf(out, "Draw\n");
			break;
		}
	}

	return 0;
}