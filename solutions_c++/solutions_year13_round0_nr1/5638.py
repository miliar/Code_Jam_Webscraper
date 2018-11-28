#include <cstdio>

char board[10][10];

bool equal(char a,char b){
	if ( a == '.' || b == '.') return false;
	if ( a == 'T' || b == 'T' )
		return true;
	return a == b;
}

bool isEmpty(){
	for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
			if ( board[i][j] == '.' )
				return false;
	return true;
}

int main(){
	int t;
	
	scanf("%d",&t);
	int test = 1;
	while(t--){

		bool xwin = false;
		bool owin = false;

		for(int i=0;i<4;i++){
			scanf("%s",board[i]);
		}

		// vertical
		for(int i = 0 ; i < 4 ; i++ ){
			char c = board[0][i];
			if ( equal(c,board[1][i]) && equal(board[1][i],board[2][i]) && equal(board[2][i],board[3][i]) && equal(board[3][i],c)){
				if ( c == 'T' ) c == board[1][i];
				if ( c == 'O' ) owin = true;
				else xwin = true;
				//printf("H%d win %c\n",i,c);
			}
		}

		// horizontal
		for(int i = 0 ; i < 4 ; i++ ){
			char c = board[i][0];
			if ( equal(c,board[i][1]) && equal(board[i][1],board[i][2]) && equal(board[i][2],board[i][3]) && equal(board[i][3],c)){
				if ( c == 'T' ) c == board[1][i];
				if ( c == 'O' ) owin = true;
				else xwin = true;
				//printf("V%d win %c\n",i,c);
			}						
		}

		// diagonal hacia abajo derecha
		char c = board[0][3];
		if ( equal(c,board[1][2]) && equal(board[1][2],board[2][1]) && equal(board[2][1],board[3][0]) && equal(board[3][0],c)){
			if ( c == 'T' ) c == board[1][2];
			if ( c == 'O' ) owin = true;
			else xwin = true;
			//printf("\\ win %c\n",c);
		}
		//diagonal abajo a la izquierda
		c = board[0][0];
		if ( equal(c,board[1][1]) && equal(board[1][1],board[2][2]) && equal(board[2][2],board[3][3]) && equal(board[3][3],c)){
			if ( c == 'T' ) c == board[1][1];
			if ( c == 'O' ) owin = true;
			else xwin = true;
			//printf("/ win %c\n",c);
		}


		if ( xwin == false && owin == false ){
			if ( isEmpty() ){
				printf("Case #%d: Draw\n",test++);
			}else{
				printf("Case #%d: Game has not completed\n",test++);
			}
		}
		else if ( xwin == true && owin == false ){
			printf("Case #%d: X won\n",test++);
		}
		else if ( xwin == false && owin == true ){
			printf("Case #%d: O won\n",test++);
		}else{

		}

	}
	return 0;
}
