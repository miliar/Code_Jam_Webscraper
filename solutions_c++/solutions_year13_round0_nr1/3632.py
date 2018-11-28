#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <utility>
#include <iostream>
#include <algorithm>
using namespace std;

typedef long long llg;

const int N = 1001;

void run() {
	char str[4][6];
	int T, res, tx, ty;
	bool fx, fo;
	scanf("%d", &T);
	for(int Case = 1; Case <= T; Case++) {
		for(int i = 0; i < 4; i++)  scanf("%s", str[i]);
		res = 0;
		tx = ty = -1;
		for(int i = 0; i < 4; i++)
			for(int j = 0; j < 4; j++) {
				res += str[i][j]=='.';
				if(str[i][j] == 'T') {
					tx = i;
					ty = j;
				}
			}
		fx = fo = false;
		if(tx != -1)  str[tx][ty] = 'X';
		for(int i = 0; i < 4; i++) {
			if(strcmp(str[i], "XXXX") == 0)  fx = true;
			if(strcmp(str[i], "OOOO") == 0)  fo = true;
			if(str[0][i]==str[1][i] && str[1][i]==str[2][i] && str[2][i]==str[3][i] && str[0][i]=='X')  
				fx = true;
			if(str[0][i]==str[1][i] && str[1][i]==str[2][i] && str[2][i]==str[3][i] && str[0][i]=='O')  
				fo = true;
		}
		if(str[0][0]==str[1][1] && str[1][1]==str[2][2] && str[2][2]==str[3][3] && str[0][0]=='X')  
			fx = true;
		if(str[0][3]==str[1][2] && str[1][2]==str[2][1] && str[2][1]==str[3][0] && str[0][3]=='X')  
			fx = true;
		if(str[0][0]==str[1][1] && str[1][1]==str[2][2] && str[2][2]==str[3][3] && str[0][0]=='O')  
			fo = true;
		if(str[0][3]==str[1][2] && str[1][2]==str[2][1] && str[2][1]==str[3][0] && str[0][3]=='O')  
			fo = true;
		if(tx != -1)  str[tx][ty] = 'O';
		for(int i = 0; i < 4; i++) {
			if(strcmp(str[i], "XXXX") == 0)  fx = true;
			if(strcmp(str[i], "OOOO") == 0)  fo = true;
			if(str[0][i]==str[1][i] && str[1][i]==str[2][i] && str[2][i]==str[3][i] && str[0][i]=='X')  
				fx = true;
			if(str[0][i]==str[1][i] && str[1][i]==str[2][i] && str[2][i]==str[3][i] && str[0][i]=='O')  
				fo = true;
		}
		if(str[0][0]==str[1][1] && str[1][1]==str[2][2] && str[2][2]==str[3][3] && str[0][0]=='X')  
			fx = true;
		if(str[0][3]==str[1][2] && str[1][2]==str[2][1] && str[2][1]==str[3][0] && str[0][3]=='X')  
			fx = true;
		if(str[0][0]==str[1][1] && str[1][1]==str[2][2] && str[2][2]==str[3][3] && str[0][0]=='O')  
			fo = true;
		if(str[0][3]==str[1][2] && str[1][2]==str[2][1] && str[2][1]==str[3][0] && str[0][3]=='O')  
			fo = true;
		printf("Case #%d: ", Case);
		if(fx && !fo)  printf("X won\n");
		else if(!fx && fo)  printf("O won\n");
		else if((fx&&fo) || (!fx && !fo && res==0))  printf("Draw\n");
		else  printf("Game has not completed\n");
	}
}

int main() {
	freopen("data.in", "r", stdin);
	freopen("data.out", "w", stdout);
	run();
	return  0;
}













