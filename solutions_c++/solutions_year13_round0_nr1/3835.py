#include <iostream>
#include <cstdio>
using namespace std;
#define X 'X'
#define O 'O'
#define T 'T'
#define DOT '.'

bool hasBlanks(const char board[4][5]){
	bool hasit=false;
	for(int i=0;i<4;++i){
		for(int j=0;j<4;++j){
			if( board[i][j] == DOT ){
				hasit=true;
				break;
			}
		}
	}
	return hasit;
}
bool wins(const char board[4][5],const char player){
	bool wins=true;
	char other = player==X?O:X;
	//cout<<"other player = "<<other<<endl;
	//row major
	for(int i=0;i<4;++i){
		wins = true;
		for(int j=0;j<4;++j){
			if( board[i][j] == other || board[i][j] == DOT ){
				wins=false;
				break;
			}
		}
		if( wins )break;
	}
	if( !wins ){

		//col major
		for(int i=0;i<4;++i){
			wins=true;
			for(int j=0;j<4;++j){
				if( board[j][i] == other || board[j][i] == DOT ){
					wins=false;
					break;
				}
			}
			if( wins )break;
		}

	}

	if( !wins ){
		wins=true;
		//diagonal
		for(int i=0;i<4;++i){
			if( board[i][i] == other || board[i][i] == DOT){
				wins=false;
				break;
			}
		}
	}

	if( !wins ){
		wins=true;
		//diagonal
		for(int i=0;i<4;++i){
			if( board[i][3-i] == other || board[i][3-i] == DOT){
				wins=false;
				break;
			}
		}
	}
	//cout<<player<<"  "<<wins<<endl;
	return wins;
}

int main() {
	int t;
	char board[4][5];
	scanf("%d",&t);
	for(int i=1;i<=t;++i){
		for(int j=0;j<4;++j){
			scanf("%s",board[j]);
		}


		bool xwins=false, owins=false;
		xwins = wins(board,X);
		owins = wins(board,O);

		if( xwins && owins ){
			printf("Case #%d: Draw\n",i);
		}else if( xwins && !owins ){
			printf("Case #%d: %c won\n",i,X);
		}else if( !xwins && owins ){
			printf("Case #%d: %c won\n",i,O);
		}
		else{
			if( !hasBlanks(board) ){
				printf("Case #%d: Draw\n",i);
			}else{
				printf("Case #%d: Game has not completed\n",i);
			}
		}

	}
	return 0;
}
