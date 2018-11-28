#include <cstdio>
#include <vector>
#include <queue>
#include <set>
#include <stack>
#include <map>
#include <cmath>
#include <string>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <ctype.h>

using namespace std;

bool ended, wino, winx;
string s[5];
map <char, int> has;

void lines(){
	for(int i=0;i<4;i++){
		has.clear();
		for(int j=0;j<4;j++){
			if(s[i][j]=='.'){
				ended = false;
				has['.']=1;
			}
			if(s[i][j]=='X'){
				has['X']=1;
			}
			if(s[i][j]=='O'){
				has['O']=1;
			}
		}
		if(has['X'] && !has['O'] && !has['.'])
			winx=true;
		if(!has['X'] && has['O'] && !has['.'])
			wino=true;
	}
}

void colunes(){
	for(int j=0;j<4;j++){
		has.clear();
		for(int i=0;i<4;i++){
			if(s[i][j]=='.'){
				ended = false;
				has['.']=1;
			}
			if(s[i][j]=='X'){
				has['X']=1;
			}
			if(s[i][j]=='O'){
				has['O']=1;
			}
		}
		if(has['X'] && !has['O'] && !has['.'])
			winx=true;
		if(!has['X'] && has['O'] && !has['.'])
			wino=true;
	}
}

void diagonals(){
	has.clear();
	for(int i=0;i<4;i++){
		if(s[i][i]=='.'){
			ended = false;
			has['.']=1;
		}
		if(s[i][i]=='X'){
			has['X']=1;
		}
		if(s[i][i]=='O'){
			has['O']=1;
		}
	}
	if(has['X'] && !has['O'] && !has['.'])
		winx=true;
	if(!has['X'] && has['O'] && !has['.'])
		wino=true;
		
	has.clear();
	for(int i=0;i<4;i++){
		if(s[i][3-i]=='.'){
			ended = false;
			has['.']=1;
		}
		if(s[i][3-i]=='X'){
			has['X']=1;
		}
		if(s[i][3-i]=='O'){
			has['O']=1;
		}
	}
	if(has['X'] && !has['O'] && !has['.'])
		winx=true;
	if(!has['X'] && has['O'] && !has['.'])
		wino=true;
}

int main(){
	int i, j, t;
	scanf(" %d", &t);
	for(i=1;i<=t;i++){
		wino = winx = false;
		ended = true;
		for(j=0;j<4;j++)
			cin >> s[j];
		lines();
		colunes();
		diagonals();
		printf("Case #%d: ", i);
		if(wino)
			printf("O won\n");
		else if(winx)
			printf("X won\n");
		else if(ended)
			printf("Draw\n");
		else
			printf("Game has not completed\n");
	}
	return 0;
}

