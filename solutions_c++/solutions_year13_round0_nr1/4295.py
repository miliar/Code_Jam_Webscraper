/*
 * TicTac.cpp
 *
 *  Created on: 13-Apr-2013
 *      Author: saurav
 */

#include<iostream>
#include<cstdio>
#include<cstring>
#include<vector>
using namespace std;

void findoutput(char board[4][4],int c){
	/*for(int i=0;i<4;i++){
		printf("%s",board[i]);
		printf("\n");
	}*/
	char check[5],diagonal[5],rdiagonal[5];
	check[4]='\0';
	diagonal[4]='\0';
	rdiagonal[4]='\0';
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++){
			check[j]=board[i][j];
		}
		//printf("%s\n",check);
		if(!strcmp(check,"XXXX")||!strcmp(check,"XXXT")||!strcmp(check,"XXTX")||!strcmp(check,"XTXX")||!strcmp(check,"TXXX")) {
			printf("Case #%d: X won\n",c);
			return ;
		}else if(!strcmp(check,"OOOO")||!strcmp(check,"OOOT")||!strcmp(check,"OOTO")||!strcmp(check,"OTOO")||!strcmp(check,"TOOO")) {
			printf("Case #%d: O won\n",c);
			return ;
		}
		for(int j=0;j<4;j++){
			check[j]=board[j][i];
		}
		//printf("%s\n",check);
		if(!strcmp(check,"XXXX")||!strcmp(check,"XXXT")||!strcmp(check,"XXTX")||!strcmp(check,"XTXX")||!strcmp(check,"TXXX")) {
			printf("Case #%d: X won\n",c);
			return ;
		}else if(!strcmp(check,"OOOO")||!strcmp(check,"OOOT")||!strcmp(check,"OOTO")||!strcmp(check,"OTOO")||!strcmp(check,"TOOO")) {
			printf("Case #%d: O won\n",c);
			return ;
		}
		diagonal[i]=board[i][i];
		rdiagonal[i]=board[i][3-i];
	}
	if(!strcmp(diagonal,"XXXX")||!strcmp(diagonal,"XXXT")||!strcmp(diagonal,"XXTX")||!strcmp(diagonal,"XTXX")||!strcmp(diagonal,"TXXX")) {
		printf("Case #%d: X won\n",c);
	return ;
	}else if(!strcmp(diagonal,"OOOO")||!strcmp(diagonal,"OOOT")||!strcmp(diagonal,"OOTO")||!strcmp(diagonal,"OTOO")||!strcmp(diagonal,"TOOO")) {
		printf("Case #%d: O won\n",c);
		return ;
	}
	if(!strcmp(rdiagonal,"XXXX")||!strcmp(rdiagonal,"XXXT")||!strcmp(rdiagonal,"XXTX")||!strcmp(rdiagonal,"XTXX")||!strcmp(rdiagonal,"TXXX")) {
		printf("Case #%d: X won\n",c);
	return ;
	}else if(!strcmp(rdiagonal,"OOOO")||!strcmp(rdiagonal,"OOOT")||!strcmp(rdiagonal,"OOTO")||!strcmp(rdiagonal,"OTOO")||!strcmp(rdiagonal,"TOOO")) {
		printf("Case #%d: O won\n",c);
		return ;
	}
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++){
			if(board[i][j]=='.'){
				printf("Case #%d: Game has not completed\n",c);
				return;
			}
		}
	}
	printf("Case #%d: Draw\n",c);
}

int main(){
	int T;
	char board[4][4];
	scanf("%d",&T);
	for(int t=0;t<T;t++){
		for(int i=0;i<4;i++){
			scanf("%s",board[i]);
		}
		findoutput(board,t+1);
		string garbage;
		getline(cin,garbage);
	}
}
