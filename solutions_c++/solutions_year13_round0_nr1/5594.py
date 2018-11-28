#include <stdio.h>
#include <string.h>

char ttt[5][5];

void check(char c, bool &win);

int main(){
	int N;
	scanf("%d", &N);
	for(int t=1;t<=N;++t){
		int numX = 0;
		int numO = 0;
		int numEmpty = 0;
		for(int i=0;i<4;++i){
			scanf("%s", &ttt[i]);
			for(int j=0;j<4;++j){
				if(ttt[i][j] == 'X') ++numX;
				if(ttt[i][j] == 'O') ++numO;
				if(ttt[i][j] == '.') ++numEmpty;
			}
		}
		
		bool Xwin = false;
		check('X', Xwin);
		bool Owin = false;
		check('O', Owin);
		
		if(Xwin && !Owin){
			printf("Case #%d: X won\n", t);
		}
		else if(!Xwin && Owin){
			printf("Case #%d: O won\n", t);
		}
		else if(!Xwin && !Owin){
			if(numEmpty > 0)printf("Case #%d: Game has not completed\n", t);
			else			printf("Case #%d: Draw\n", t);
		}
		else{
			if(numX > numO) printf("Case #%d: O won\n", t);
			else			printf("Case #%d: X won\n", t);
		}
	}
	
	return 0;
}

void check(char c, bool &win){
	// row
	for(int i=0;i<4;++i){
		if(ttt[i][0] == c){
			bool find = true;
			for(int j=1;j<4;++j){
				if(ttt[i][j] != c && ttt[i][j] != 'T'){
					find = false;
					break;
				}
			}
			if(find) win = true;
		}
	}
	for(int i=0;i<4;++i){
		if(ttt[i][3] == c){
			bool find = true;
			for(int j=2;j>=0;--j){
				if(ttt[i][j] != c && ttt[i][j] != 'T'){
					find = false;
					break;
				}
			}
			if(find) win = true;
		}
	}
	
	// column
	for(int i=0;i<4;++i){
		if(ttt[0][i] == c){
			bool find = true;
			for(int j=1;j<4;++j){
				if(ttt[j][i] != c && ttt[i][j] != 'T'){
					find = false;
					break;
				}
			}
			if(find) win = true;
		}
	}
	for(int i=0;i<4;++i){
		if(ttt[3][i] == c){
			bool find = true;
			for(int j=2;j>=0;--j){
				if(ttt[j][i] != c && ttt[i][j] != 'T'){
					find = false;
					break;
				}
			}
			if(find) win = true;
		}
	}
	
	// diagonal
	if(ttt[0][0] == c){
		bool find = true;
		for(int i=1;i<4;++i){
			if(ttt[i][i] != c && ttt[i][i] != 'T'){
				find = false;
				break;
			}
		}
		if(find) win = true;
	}
	if(ttt[3][3] == c){
		bool find = true;
		for(int i=2;i>=0;--i){
			if(ttt[i][i] != c && ttt[i][i] != 'T'){
				find = false;
				break;
			}
		}
		if(find) win = true;
	}
	if(ttt[0][3] == c){
		bool find = true;
		for(int i=1;i<4;++i){
			if(ttt[i][3-i] != c && ttt[i][3-i] != 'T'){
				find = false;
				break;
			}
		}
		if(find) win = true;
	}
	if(ttt[3][0] == c){
		bool find = true;
		for(int i=1;i<4;++i){
			if(ttt[3-i][i] != c && ttt[3-i][i] != 'T'){
				find = false;
				break;
			}
		}
		if(find) win = true;
	}
}
