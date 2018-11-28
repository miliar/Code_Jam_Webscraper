#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<iostream>
using namespace std;
char board[4][4];

void boardInit(){
	int i,j;
	for(i=0;i<4;i++){
		for(j=0;j<4;j++){
		cin>>board[i][j];
		}
	}
}

int checkRow(){
	int i,j;
	int countX=0,countO=0,countT=0;
	for(i=0;i<4;i++){
		countX=0;
		countO=0;
		countT=0;
				for(j=0;j<4;j++){
					if(board[i][j]=='X') countX++;
					if(board[i][j]=='O') countO++;
					if(board[i][j]=='T') countT++;
		}
		if(countX==4||(countX==3&&countT==1)) return 1;
		else if(countO==4||(countO==3&&countT==1)) return 2;
	}
	for(i=0;i<4;i++)
		for(j=0;j<4;j++)
			if(board[i][j]=='.') return -1;
	return 0;
}
//draw 0,not finished -1, x 1 o 2

int checkCol(){
	int i,j;
	int countX=0,countO=0,countT=0;
	for(j=0;j<4;j++){
		countX=0;
		countO=0;
		countT=0;
				for(i=0;i<4;i++){
					if(board[i][j]=='X') countX++;
					if(board[i][j]=='O') countO++;
					if(board[i][j]=='T') countT++;
		}
		if(countX==4||(countX==3&&countT==1)) return 1;
		else if(countO==4||(countO==3&&countT==1)) return 2;
	}
	for(i=0;i<4;i++)
		for(j=0;j<5;j++)
			if(board[i][j]=='.') return -1;
	return 0;
}

int checkDiag(){
	int i,j;
	int countX=0,countO=0,countT=0;
	if(board[0][0]=='X') countX++;
	if(board[1][1]=='X') countX++;
	if(board[2][2]=='X') countX++;
	if(board[3][3]=='X') countX++;
	if(board[0][0]=='O') countO++;
	if(board[1][1]=='O') countO++;
	if(board[2][2]=='O') countO++;
	if(board[3][3]=='O') countO++;
	if(board[0][0]=='T') countT++;
	if(board[1][1]=='T') countT++;
	if(board[2][2]=='T') countT++;
	if(board[3][3]=='T') countT++;
	if(countX==4||(countX==3&&countT==1)) return 1;
		else if(countO==4||(countO==3&&countT==1)) return 2;
	/*for(i=0;i<4;i++){
		for(j=0;j<4;j++){
			if(i==j){
					if(board[i][j]=='X') countX++;
					if(board[i][j]=='O') countO++;
					if(board[i][j]=='T') countT++;
		}
	}
		if(countX==4||(countX==3&&countT==1)) return 1;
		else if(countO==4||(countO==3&&countT==1)) return 2;
	}*/
	for(i=0;i<4;i++)
		for(j=0;j<4;j++)
			if(board[i][j]=='.') return -1;
	return 0;
}

int checkRevDaig(){
	int i,j;
	int countX=0,countO=0,countT=0;
	if(board[0][3]=='X') countX++;
	if(board[1][2]=='X') countX++;
	if(board[2][1]=='X') countX++;
	if(board[3][0]=='X') countX++;
	if(board[0][3]=='O') countO++;
	if(board[1][2]=='O') countO++;
	if(board[2][1]=='O') countO++;
	if(board[3][0]=='O') countO++;
	if(board[0][3]=='T') countT++;
	if(board[1][2]=='T') countT++;
	if(board[2][1]=='T') countT++;
	if(board[3][0]=='T') countT++;
	if(countX==4||(countX==3&&countT==1)) return 1;
		else if(countO==4||(countO==3&&countT==1)) return 2;
	/*for(i=0;i<4;i++){
		for(j=0;j<4;j++){
			if((3-i)==j){
				printf("%d %d\n",i,j);
					if(board[i][j+1]=='X') countX++;
					if(board[i][j+1]=='O') countO++;
					if(board[i][j+1]=='T') countT++;
		}
	}
		if(countX==4||(countX==3&&countT==1)) return 1;
		else if(countO==4||(countO==3&&countT==1)) return 2;
	}*/
	//printf("\n%d %d %d",countX,countO,countT);
	for(i=0;i<4;i++)
		for(j=0;j<4;j++)
			if(board[i][j]=='.') return -1;
	return 0;
}
	
int main(void){
	int T;
	int i;
	scanf("%d",&T);
	int boards[T];
	for(i=0;i<T;i++){
		boardInit();
		if(checkCol()!=-1) {boards[i]=checkCol();}
		else if(checkRow()!=-1) {boards[i]=checkRow();}
		else if(checkDiag()!=-1) {boards[i]=checkDiag();}
		else if(checkRevDaig()!=-1) {boards[i]=checkRevDaig();}
		else boards[i]=-1;
	}
	for(i=0;i<T;i++){
		if(boards[i]>0){
			if(boards[i]==1){
		printf("Case #%d: %c won", i+1, 'X');
		printf("\n");}
			else {
				printf("Case #%d: %c won", i+1, 'O');
				printf("\n");}
		}
		else if(boards[i]==-1) {printf("Case #%d: Game has not completed",i+1);
								printf("\n");}
			else {printf("Case #%d: Draw",i+1);
				printf("\n");}
	}
	return 0;
}
	
	
