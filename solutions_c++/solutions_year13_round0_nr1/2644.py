#include <cstdio>
#include <algorithm>
using namespace std;

int T;
char board[5][5];
bool win(char c){
	bool cwin = false;
	for(int i = 0; i < 4; i++){
		int sum = 0;
		for(int j = 0; j < 4; j++)
			sum += (board[i][j] == c);
		if(sum == 4){
			cwin = true;
			break;
		}
	}
	if(cwin) return true;
	//puts("X yoko");

	for(int i = 0; i < 4; i++){
		int sum = 0;
		for(int j = 0; j < 4; j++)
			sum += (board[j][i] == c);
		if(sum == 4){
			cwin = true;
			break;
		}
	}
	if(cwin) return true;
	//puts("X tate");

	int sum = 0;
	for(int i = 0; i < 4; i++)
		sum += (board[i][i] == c);
	if(sum == 4) return true;
	//puts("naname");

	sum = 0;
	for(int i = 0; i < 4; i++)
		sum += (board[3-i][i] == c);
	if(sum == 4) return true;
	//puts("naname");

	return false;
}
int main(){
	scanf("%d", &T);
	char c;
	for(int t = 1; t <= T; t++){
		scanf("%c", &c); //改行文字
		int th = -1, tw = -1;
		bool isFilled = true;
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++){
				scanf("%c", &board[i][j]);
				if(board[i][j] == 'T'){
					th = i;
					tw = j;
				}else if(board[i][j] == '.'){
					isFilled = false;
				}
				//printf("%c", board[i][j]);
			}
			scanf("%c", &c); //改行文字
			//puts("");
		}
		printf("Case #%d: ", t);
		if(th != -1 && tw != -1) board[th][tw] = 'X';
		if(win('X')){
			printf("X won\n");
			continue;
		}
		if(th != -1 && tw != -1) board[th][tw] = 'O';
		if(win('O')){
			printf("O won\n");
			continue;
		}
		if(isFilled){
			printf("Draw\n");
		}else{
			printf("Game has not completed\n");
		}
	}
	return 0;
}
