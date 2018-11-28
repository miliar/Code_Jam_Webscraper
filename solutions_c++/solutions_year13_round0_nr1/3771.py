/*
 * ProbA.cpp
 *
 *  Created on: 13-Apr-2013
 *      Author: nataraj
 */



#include <cmath>
#include <cstdio>
#include <cstring>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int T;
char inp[5][5];

bool checkxWon(){
	bool retVal=false;
	for(int i=0;i<4;i++){
		if(inp[i][0]=='X' && inp[i][1]=='X' && inp[i][2]=='X' && inp[i][3]=='X')
			return true;
		if(inp[0][i]=='X' && inp[1][i]=='X' && inp[2][i]=='X' && inp[3][i]=='X')
			return true;
	}
	if(inp[0][0]=='X' && inp[1][1]=='X' && inp[2][2]=='X' && inp[3][3]=='X')
		return true;

	if(inp[0][3]=='X' && inp[1][2]=='X' && inp[2][1]=='X' && inp[3][0]=='X')
		return true;

	return false;
}
bool checkyWon(){
	bool retVal=false;
	for(int i=0;i<4;i++){
		if(inp[i][0]=='O' && inp[i][1]=='O' && inp[i][2]=='O' && inp[i][3]=='O')
			return true;
		if(inp[0][i]=='O' && inp[1][i]=='O' && inp[2][i]=='O' && inp[3][i]=='O')
			return true;
	}
	if(inp[0][0]=='O' && inp[1][1]=='O' && inp[2][2]=='O' && inp[3][3]=='O')
		return true;

	if(inp[0][3]=='O' && inp[1][2]=='O' && inp[2][1]=='O' && inp[3][0]=='O')
		return true;

	return false;
}

bool checkDraw(){
	for(int i=0;i<4;i++){
		for(int j=0;j<4;++j){
			if(inp[i][j]=='.')
				return false;
		}

	}
	return true;
}
char* solve(){
	int xt=0,yt=0;
	bool contFlag=true;
	bool tFlag=false;
	for(int i=0;i<4 && contFlag;++i){
		for(int j=0;j<4 && contFlag;++j){
			if(inp[i][j]=='T'){
				xt=i;yt=j;
				contFlag=false;
				tFlag = true;
			}
		}
	}
	if(tFlag){
	//replace with X
		inp[xt][yt]='X';
	}

	if(checkxWon())
		return "X won";
	if(tFlag){
	//replace with Y
		inp[xt][yt]='O';
	}
	if(checkyWon())
		return "O won";
	if(checkDraw())
		return "Draw";
	else
		return "Game has not completed";
}
int main(int argc, char **argv) {
	scanf("%d",&T);
	int prob=1;
	while(T--){
		memset(inp,0,sizeof(inp));
		scanf("%s",inp[0]);
		scanf("%s",inp[1]);
		scanf("%s",inp[2]);
		scanf("%s",inp[3]);
		printf("Case #%d: %s\n", prob++, solve());
	}
	return 0;
}

