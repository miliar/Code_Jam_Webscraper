#include <cstdio>
#include <cmath>
#include <cstring>
#include <memory.h>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <map>
#include <queue>
using namespace std;
char str[5][5];

void init(){
	memset(str,0,sizeof(str));
	for (int i=0;i<4;i++){
		scanf("%s",str[i]);
	}
	return;
}

bool checkrow(int id,int clr){
	for (int i=0;i<4;i++){
		if (str[id][i]==clr){
			continue;
		}
		if (str[id][i]==-1){
			continue;
		}
		return false;
	}
	return true;
}

bool checkclm(int id,int clr){
	for (int i=0;i<4;i++){
		if (str[i][id]==clr){
			continue;
		}
		if (str[i][id]==-1){
			continue;
		}
		return false;
	}
	return true;
}

bool checkdg1(int clr){
	for (int i=0;i<4;i++){
		if (str[i][i]==clr){
			continue;
		}
		if (str[i][i]==-1){
			continue;
		}
		return false;
	}
	return true;
}

bool checkdg2(int clr){
	for (int i=0;i<4;i++){
		if (str[i][4-i-1]==clr){
			continue;
		}
		if (str[i][4-i-1]==-1){
			continue;
		}
		return false;
	}
	return true;
}

void xwon(){
	puts("X won");
	return;
}

void owon(){
	puts("O won");
	return;
}

void check(){
	int nx=0;
	int no=0;
	int nt=0;
	for (int i=0;i<4;i++){
		for (int j=0;j<4;j++){
			if (str[i][j]=='.'){
				str[i][j]=0;
			}
			if (str[i][j]=='X'){
				str[i][j]=1;
				nx++;
			}
			if (str[i][j]=='O'){
				str[i][j]=2;
				no++;
			}
			if (str[i][j]=='T'){
				str[i][j]=-1;
				nt++;
			}
		}
	}
	for (int i=0;i<4;i++){
		if (checkrow(i,1)){
			xwon();
			return;
		}
		if (checkrow(i,2)){
			owon();
			return;
		}
		if (checkclm(i,1)){
			xwon();
			return;
		}
		if (checkclm(i,2)){
			owon();
			return;
		}
	}
	if (checkdg1(1)||checkdg2(1)){
		xwon();
		return;
	}
	if (checkdg1(2)||checkdg2(2)){
		owon();
		return;
	}
	if ((nx+no+nt)==16){
		puts("Draw");
		return;
	}
	puts("Game has not completed");
	return;
}

int main(){
	int tcase;
	scanf("%d",&tcase);
	for (int i=1;i<=tcase;i++){
		init();
		printf("Case #%d: ",i);
		check();
	}
	return 0;
}
