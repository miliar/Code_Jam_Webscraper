#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <stdio.h>
using namespace std;

char map[4][4];

// 1 Xwin  2 O win   3 draw  4 noover

int judge(){
    int row1[4],row2[4],col1[4],col2[4],Trow[4],Tcol[4],Lxie1,Lxie2,TLxie,Rxie1,Rxie2,TRxie;
	for(int i = 0 ; i < 4; ++i){
	  row1[i] = 0; row2[i] = 0; col1[i] = 0;col2[i] = 0;
	  Trow[i] = 0; Tcol[i] = 0; Lxie1 = 0;Lxie2 = 0;
	  TLxie = 0; Rxie1 = 0; Rxie2 = 0; TRxie = 0;
	}
	for(int i = 0; i < 4; ++i){
		for(int j = 0; j < 4; ++j){
			if(map[i][j] == 'X'){
			  row1[i]++;
			}
			else if(map[i][j] == 'O'){
			  row2[i]++;
			}
			else if(map[i][j] == 'T'){
			  Trow[i]++;
			}
		}
	}
	for(int i = 0; i < 4; ++i){
		for(int j = 0; j < 4; ++j){
			if(map[j][i] == 'X'){
			   col1[i]++;
			}
			else if(map[j][i] == 'O'){
			   col2[i]++;
			}
			else if(map[j][i] == 'T'){
			  Tcol[i]++;
			}
		}
	}
	for(int i = 0; i < 4; ++i){
		if(map[i][i] == 'X'){
		   Lxie1++;
		}
		else if(map[i][i] == 'O'){
		  Lxie2++;
		}
		else if(map[i][i] == 'T'){
		  TLxie++;
		}
	}
	for(int i = 0; i < 4; ++i){
		if(map[i][3 - i] == 'X'){
		   Rxie1++;
		}
		else if(map[i][3 - i] == 'O'){
		  Rxie2++;
		}
		else if(map[i][3 - i] == 'T'){
		  TRxie++;
		}
	}
	for(int i = 0; i < 4; ++i){
		if( (row1[i] == 4) ||  ( (row1[i] == 3) && (Trow[i] == 1) )){
			return 1;
		}
		else if((row2[i] == 4) ||  ( (row2[i] == 3 ) && (Trow[i] == 1) )){
		   return 2;
		}
	}
	for(int i = 0; i < 4; ++i){
	  if((col1[i] == 4 ) || ((col1[i] == 3) && (Tcol[i] == 1))){
		  return 1;
	  }
	  else if(( col2[i] == 4 ) || ((col2[i] == 3) && (Tcol[i] == 1) ) )
		  return 2;
	}
	if((Lxie1 == 4) ||( (Lxie1 == 3) && (TLxie == 1) ) ){
		return 1;
	}
	else if((Lxie2 == 4 ) || ((Lxie2 == 3) && (TLxie == 1)))
		return 2;
	if((Rxie1 == 4 ) || ((Rxie1 == 3) && (TRxie == 1))){
		return 1;
	}
	else if((Rxie2 == 4 ) || ((Rxie2 == 3) && (TRxie == 1)))
		return 2;
	for(int i = 0; i < 4; ++i){
		for(int j = 0; j < 4; ++j){
		   if(map[i][j] == '.')
			   return 4;
		}
	}
	return 3;
}

int main(){
	freopen("1.txt","r",stdin);
	freopen("2.txt","w",stdout);
	int numcase;
	cin >> numcase;
	for(int cnt = 1; cnt <= numcase; ++cnt){
		for(int i = 0; i < 4; ++i){
			for(int j = 0; j < 4; ++j){
			   cin >> map[i][j];
			}
		}
	int x = judge();
	printf("Case #%d: ",cnt);
	if(x == 1)
		printf("X won\n");
	else if(x == 2)
		printf("O won\n");
	else if(x == 4){
	   printf("Game has not completed\n");
	}
	else{
	   printf("Draw\n");
	}
	}
	
	return 0;
}