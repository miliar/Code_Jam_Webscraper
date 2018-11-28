#include <stdio.h>

static int board[4][4];
void printBoard(){
	printf("-----------\n");
	int i =0,j=0;
	for(i=0;i<4;i++){
		for(j=0;j<4;j++){
			printf("%c",board[i][j]);
		}
		printf("\n");
	}
	printf("-----------\n");
}

bool isX(int i ,int j){
	if(board[i][j] == 'X' || board[i][j] == 'T') return true;
	return false;
}

bool isO(int i ,int j){
	if(board[i][j] == 'O' || board[i][j] == 'T') return true;
	return false;
}

int main(void){
	FILE* inp = fopen("inp.txt","r");
	FILE* out = fopen("out.txt","w");

	int t=0;
	char c = 0,c1,c2,c3,c4;
	int i =0,j=0;
	char* xWon = "X won";
	char* oWon = "O won";
	char* draw = "Draw";
	char* inComplete = "Game has not completed";
	bool isFull,isXwon,isOwon;
	int num =0;
	fscanf(inp,"%d",&t);
	for(num = 1;num <=t;num++){
		for(i=0;i<4;i++){
			for(j=0;j<4;){
				c = (char)fgetc(inp);
				if(c == 'X' || c == 'O' || c == '.' || c == 'T'){
					board[i][j] = c;
					j++;
				}
			}
		}
		isXwon = false;
		isOwon = false;
		isFull = true;
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				c1 = board[i][j];
				if(c1=='.') isFull = false;
				if(i==0 ){
					
						if(isX(i,j) && isX(i+1,j) && isX(i+2,j) && isX(i+3,j)){
							isXwon = true;
							goto out;
						}

						if(isO(i,j) && isO(i+1,j) && isO(i+2,j) && isO(i+3,j)){
							isOwon = true;
							goto out;
						}
					
				}

				if(j==0){
					if(isX(i,j) && isX(i,j+1) && isX(i,j+2) && isX(i,j+3)){
							isXwon = true;
							goto out;
						}
					if(isO(i,j) && isO(i,j+1) && isO(i,j+2) && isO(i,j+3)){
							isOwon = true;
							goto out;
						}
				}
				if(i==0 && j==0){
					if(isX(i,j) && isX(i+1,j+1) && isX(i+2,j+2) && isX(i+3,j+3)){
							isXwon = true;
							goto out;
						}
					if(isO(i,j) && isO(i+1,j+1) && isO(i+2,j+2) && isO(i+3,j+3)){
							isOwon = true;
							goto out;
						}
				}

				if(i==3 && j == 0){
					if(isX(i,j) && isX(i-1,j+1) && isX(i-2,j+2) && isX(i-3,j+3)){
							isXwon = true;
							goto out;
						}
					if(isO(i,j) && isO(i-1,j+1) && isO(i-2,j+2) && isO(i-3,j+3)){
							isOwon = true;
							goto out;
						}
				}
			}
		}
		
out:
		if(isXwon){
			fprintf(out,"Case #%d: %s\n",num,xWon);
			continue;
		}
		if(isOwon){
			fprintf(out,"Case #%d: %s\n",num,oWon);
			continue;
		}
		if(isFull){
			fprintf(out,"Case #%d: %s\n",num,draw);
			
		}
		else{
			fprintf(out,"Case #%d: %s\n",num,inComplete);
		}
		//printBoard();


	}

	return 0;
}