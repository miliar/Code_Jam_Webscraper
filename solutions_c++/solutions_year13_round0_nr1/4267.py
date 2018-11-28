#include<cstdio>

#define X_WIN printf("Case #%d: X won\n",a)
#define O_WIN printf("Case #%d: O won\n",a)
#define DRAW printf("Case #%d: Draw\n",a)
#define NOT_END printf("Case #%d: Game has not completed\n",a)

char board[4][5];

int main(){
	int testcaseCount;
	int i,j,a;

	int sum;
	int checker;

	scanf("%d",&testcaseCount);
	for(a=1;a<=testcaseCount;a++){
			for(i=0;i<4;i++){
					scanf("%s",board[i]);
			}
			//Horizontally
			for(i=0;i<4;i++){
					sum = 0;
					checker = 0;
					for(j=0;j<4;j++){
							switch(board[i][j]){
								case 'X':
									sum++;
									break;
								case 'O':
									sum--;
									break;
								case 'T':
									checker = 1;
									break;
							}
					}
					if(sum == 4 || (sum == 3 && checker == 1)){
							X_WIN;
							break;
					}else if(sum == -4 || (sum == -3 && checker == 1)){
							O_WIN;
							break;
					}
			}
			if(i == 4){
					//Vertically
					for(i=0;i<4;i++){
							sum = 0;
							checker = 0;
							for(j=0;j<4;j++){
									switch(board[j][i]){
										case 'X':
											sum++;
											break;
										case 'O':
											sum--;
											break;
										case 'T':
											checker = 1;
											break;
									}
							}
							if(sum == 4 || (sum == 3 && checker == 1)){
									X_WIN;
									break;
							}else if(sum == -4 || (sum == -3 && checker == 1)){
									O_WIN;
									break;
							}
					}
					if(i == 4){
							//Diagonally

							sum = 0;
							checker = 0;
							for(j=0;j<4;j++){
									switch(board[j][j]){
										case 'X':
											sum++;
											break;
										case 'O':
											sum--;
											break;
										case 'T':
											checker = 1;
											break;
									}
							}
							if(sum == 4 || (sum == 3 && checker == 1)){
									X_WIN;
							}else if(sum == -4 || (sum == -3 && checker == 1)){
									O_WIN;
							}else{
									sum = 0;
									checker = 0;
									for(j=0;j<4;j++){
											switch(board[3-j][j]){
												case 'X':
													sum++;
													break;
												case 'O':
													sum--;
													break;
												case 'T':
													checker = 1;
													break;
											}
									}
									if(sum == 4 || (sum == 3 && checker == 1)){
											X_WIN;
									}else if(sum == -4 || (sum == -3 && checker == 1)){
											O_WIN;
									}else{
											checker = 0;
											for(i=0;i<4;i++){
													for(j=0;j<4;j++){
															if(board[i][j] == '.') checker = 1;
													}
											}
											if(checker == 1){
													NOT_END;
											}else{
													DRAW;
											}
									}
							}
					}
			}
	}

	return 0;
}
