#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>

#include <string>
#include <iostream>
#include <algorithm>

#include <vector>
#include <map>
#include <queue>

#define dbg(a) cout << a << endl

using namespace std;

char mat[5][5];

void read(){
	for(int i = 0; i < 4; i++){
		for(int j = 0; j < 4; j++){
			scanf(" %c", &mat[i][j]);
		}
	}
}

void process(){
	bool x , o;

	for(int i = 0; i < 4; i++){
		x = o = true;
		for(int j = 0; j < 4; j++){
			if(mat[i][j] != 'T' && mat[i][j] != 'X')
				x = false;
			if(mat[i][j] != 'T' && mat[i][j] != 'O')
				o = false;
		}
		if(o){
			printf("O won\n");
			return;
		}else if(x){
			printf("X won\n");
			return;
		}

		x = o = true;
		for(int j = 0; j < 4; j++){
			if(mat[j][i] != 'T' && mat[j][i] != 'X')
				x = false;
			if(mat[j][i] != 'T' && mat[j][i] != 'O')
				o = false;
		}
		if(o){
			printf("O won\n");
			return;
		}else if(x){
			printf("X won\n");
			return;
		}
	}

	x = o = true;
	for(int i = 0; i < 4; i++){
		if(mat[i][i] != 'T' && mat[i][i] != 'X')
			x = false;
		if(mat[i][i] != 'T' && mat[i][i] != 'O')
			o = false;
	}
	if(o){
		printf("O won\n");
		return;
	}else if(x){
		printf("X won\n");
		return;
	}

	x = o = true;
	for(int i = 0; i < 4; i++){
		if(mat[i][3-i] != 'T' && mat[i][3-i] != 'X')
			x = false;
		if(mat[i][3-i] != 'T' && mat[i][3-i] != 'O')
			o = false;
	}
	if(o){
		printf("O won\n");
		return;
	}else if(x){
		printf("X won\n");
		return;
	}

	for(int i = 0; i < 4; i++){
		for(int j = 0; j < 4; j++){
			if(mat[i][j] == '.'){
				printf("Game has not completed\n");
				return;
			}
		}
	}

	printf("Draw\n");
}

int main(){

	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int t;
	scanf("%d", &t);

	for(int i = 1; i <= t; i++){
		read();

		printf("Case #%d: ", i);
		process();
	}

	return 0;
}
