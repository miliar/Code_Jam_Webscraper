#include <iostream>
#include <cstdio>
#include <string>

int x[10][4]={{0,1,2,3},{0,1,2,3},{0,1,2,3},{0,1,2,3},{0,0,0,0},{1,1,1,1},{2,2,2,2},{3,3,3,3},{0,1,2,3},{3,2,1,0}};
int y[10][4]={{0,0,0,0},{1,1,1,1},{2,2,2,2},{3,3,3,3},{0,1,2,3},{0,1,2,3},{0,1,2,3},{0,1,2,3},{0,1,2,3},{0,1,2,3}};

using namespace std;

int main(){

	int T;
	char tgt;
	bool chk, flg, ex_dot=false;
	char board[4][5];
	
	scanf("%d", &T);
	
	for(int k=0; k<T; ++k){
		
		ex_dot=false;
		flg=false;	
		
		for(int i=0; i<4; ++i){
			scanf("%s", board[i]);
		}
		
		cin.ignore();
		
		for(int j=0; j<10; ++j){
			
			chk=true;
			tgt=(board[y[j][0]][x[j][0]]=='T'?board[y[j][3]][x[j][3]]:board[y[j][0]][x[j][0]]);
			
			if(tgt=='.'){
				ex_dot=true;
				continue;
			}
			
			for(int i=0; i<4; ++i){
				if(board[y[j][i]][x[j][i]]!=tgt&&board[y[j][i]][x[j][i]]!='T'){
					chk=false;
					break;
				}
			}
			
			if(chk){
				printf("Case #%d: %c won\n", k+1, tgt);
				flg = true;
				break;
			}
		}
		
		if(!flg){
			if(!ex_dot){
				for(int i=0; i<4; ++i){
					for(int j=0; j<4; ++j){
						ex_dot |= board[i][j]=='.';
					}
				}
			}
			
			if(ex_dot)
				printf("Case #%d: Game has not completed\n", k+1);
			else
				printf("Case #%d: Draw\n", k+1);
		}
	}
	
	return 0;
}
