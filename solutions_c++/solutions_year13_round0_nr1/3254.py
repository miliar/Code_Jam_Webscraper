#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <cmath>

void Input(int **board, FILE *f1){
	char temp;
	for(int row=0; row<4; row++){
		for(int col=0; col<4; col++){
			fscanf(f1, "%c", &temp);
			if(temp=='X'){
				board[row][col] = 0;
			}
			else{
				if(temp=='O'){
					board[row][col] = 7;
				}
				else{
					if(temp=='.'){
						board[row][col] = 3;
					}
					else{
						board[row][col] = 1;
					}
				}
			}
		}
		fscanf(f1, "\n");
	}
	fscanf(f1,"\n");

}

void Output(int status, int case_num){
	FILE *f1;
	f1 = fopen("output.out", "a");
	switch(status){
	case 0: fprintf(f1, "Case #%d: X won\n",case_num+1);
			break;
	case 1: fprintf(f1, "Case #%d: O won\n",case_num+1);
			break;
	case 2: fprintf(f1, "Case #%d: Draw\n",case_num+1);
			break;
	case 3: fprintf(f1, "Case #%d: Game has not completed\n",case_num+1);
			break;

	}
	fclose(f1);
}

int isRow(int **board){
	for(int i=0; i<4; i++){
		int sum = 0;
		for(int j=0; j<4; j++){
			sum += board[i][j];
		}
		switch(sum){
		case 0:
		case 1: return 0;
				break;
		case 22:
		case 28:return 1;
				break;
		}
	}

	return 2;
}

int isCol(int **board){
	for(int i=0; i<4; i++){
		int sum = 0;
		for(int j=0; j<4; j++){
			sum += board[j][i];
		}
		switch(sum){
		case 0: 
		case 1: return 0;
				break;
		case 22:
		case 28:return 1;
				break;
			
		}
	}

	return 2;
}

int isDiag(int **board){
	int sum_1 = 0;
	int sum_2 = 0;
	for(int i=0; i<4; i++){
		sum_1 += board[i][i];
		sum_2 += board[3-i][i];
	}
	switch(sum_1){
	case 0:
	case 1: return 0;
			break;
	case 22:
	case 28:return 1;
			break;
			
	}
	switch(sum_2){
	case 0:
	case 1:  return 0;
			break;
	case 22:
	case 28: return 1;
			break;
			
	}
	return 2;
}

int isFull(int **board){
	for(int i=0; i<4; i++){
		for(int j=0; j<4; j++){
			if(board[i][j]==3)return 1;
		}
	}
	return 0;
}

int Status(int **board){
	switch(isRow(board)){
	case 0: return 0;
			break;
	case 1: return 1;
			break;
	case 2: switch(isCol(board)){
			case 0: return 0;
					break;
			case 1: return 1;
					break;
			case 2: switch(isDiag(board)){
					case 0: return 0;
							break;
					case 1: return 1;
							break;
					case 2: switch(isFull(board)){
							case 0: return 2;
									break;
							case 1: return 3;
									break;
							}
					}
			}
	}

	

	return(4);
}

int main(){
	int **board;
	board = new int*[4];
	for(int i=0; i<4; i++){
		board[i] = new int[4];
	}
	int num_cases;
	FILE *f1;
	f1 = fopen("A-large.in", "r");
	fscanf(f1, "%d\n", &num_cases);
	for(int i=0; i<num_cases; i++){
		Input(board, f1);
		Output(Status(board),i);
	}
	fclose(f1);
	for(int i=0; i<4; i++){
		delete[] board[i];
	}
	delete[] board;
	return 0;
}