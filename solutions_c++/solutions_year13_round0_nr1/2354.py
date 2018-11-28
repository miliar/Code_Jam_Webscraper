#include "stdio.h"
#include "string.h"
#include <algorithm>
#include <queue>
#include <map>
#include <iostream>
#include <vector>
#include <string>
using namespace std;
void Check(char board[][5]){
	for(int i=0;i<4;i++){
		bool O=true,X=true;
		for(int j=0;j<4;j++){
			if(board[i][j]!='O'&&board[i][j]!='T')
				O=false;
			if(board[i][j]!='X'&&board[i][j]!='T')
				X=false;
		}
		if(O){
			printf("O won\n");
			return;
		}
		if(X){
			printf("X won\n");
			return;
		}
	}
	for(int i=0;i<4;i++){
		bool O=true,X=true;
		for(int j=0;j<4;j++){
			if(board[j][i]!='O'&&board[j][i]!='T')
				O=false;
			if(board[j][i]!='X'&&board[j][i]!='T')
				X=false;
		}
		if(O){
			printf("O won\n");
			return;
		}
		if(X){
			printf("X won\n");
			return;
		}
	}
	bool O, X;
	O=X=true;
	for(int i=0;i<4;i++){
		if(board[i][i]!='O'&&board[i][i]!='T')
			O=false;
		if(board[i][i]!='X'&&board[i][i]!='T')
			X=false;
	}
	if(O){
		printf("O won\n");
		return;
	}
	if(X){
		printf("X won\n");
		return;
	}

	O=X=true;
	for(int i=0;i<4;i++){
		if(board[i][3-i]!='O'&&board[i][3-i]!='T')
			O=false;
		if(board[i][3-i]!='X'&&board[i][3-i]!='T')
			X=false;
	}
	if(O){
		printf("O won\n");
		return;
	}
	if(X){
		printf("X won\n");
		return;
	}

	int empty=0;
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++){
			if(board[i][j]=='.')
				empty++;
		}
	}
	if(empty==0){
		printf("Draw\n");
		return;
	}
	printf("Game has not completed\n");
}
int main(){
	freopen("D:\\Test\\in.txt","r",stdin);
	freopen("D:\\Test\\out.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		char board[4][5];
		for(int i=0;i<4;i++)
			scanf("%s",board[i]);
		printf("Case #%d: ",t);
		Check(board);
	}
    return 0;
}