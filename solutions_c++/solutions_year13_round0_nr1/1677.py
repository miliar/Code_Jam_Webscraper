/*
 * A.cpp
 *
 *  Created on: 2013-4-13
 *      Author: chen
 */

#include<iostream>
using namespace std;
char grid[4][4];

bool checkH(char t){
	int i,j;
	for(i = 0;i<4;i++){
		for(j = 0;j<4;j++){
			if(grid[i][j] != t && grid[i][j] != 'T')
				break;
		}
		if(j == 4)return true;
	}
	return false;
}

bool checkV(char t){
	int i,j;
	for(j = 0;j<4;j++){
		for(i = 0;i<4;i++){
			if(grid[i][j] != t && grid[i][j] != 'T')
				break;
		}
		if(i == 4)return true;
	}
	return false;
}
bool checkD(char t){
	int i,cnt=0;
	for(i = 0;i<4;i++)
		if(grid[i][i] == t || grid[i][i] == 'T')
			cnt++;
	if(cnt == 4)return true;
	cnt = 0;
	for(i = 0;i<4;i++)
		if(grid[i][3-i] == t || grid[i][3-i] == 'T')
					cnt++;
	if(cnt == 4)return true;
	return false;
}
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int cases,cas;
	cin >> cases;
	for(int cas = 1; cas <= cases; cas++){
		int cnt = 0;
		for(int i = 0;i< 4;i++){
			scanf("%s",grid[i]);
			for(int j=0;j < 4;j++)
				if(grid[i][j] == '.')
					cnt++;
		}
		if(checkH('X') || checkV('X')||checkD('X')){
			printf("Case #%d: %s\n",cas,"X won");
		}else if(checkH('O') || checkV('O')||checkD('O')){
			printf("Case #%d: %s\n",cas,"O won");
		}else if(cnt == 0){
			printf("Case #%d: %s\n",cas,"Draw");
		}else{
			printf("Case #%d: %s\n",cas,"Game has not completed");
		}
	}
	return 0;
}
