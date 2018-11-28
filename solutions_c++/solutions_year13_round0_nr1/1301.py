#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;
#define N 200005
#define MOD 1000000007
#define ll long long
#define eps 1e-8
char g[10][10];
bool c(char ch){
	for(int i = 0; i < 4; i++){
		int cnt = 0, t = 0;
		for(int j = 0; j < 4; j++){
			if(g[j][i] == ch) cnt++;
			if(g[j][i] == 'T') t++;
		}
		if(cnt + t == 4) return true;
	}
	return false;
}
bool r(char ch){
	for(int i = 0; i < 4; i++){
		int cnt = 0, t = 0;
		for(int j = 0; j < 4; j++){
			if(g[i][j] == ch) cnt++;
			if(g[i][j] == 'T') t++;
		}
		if(cnt + t == 4) return true;
	}	
	return false;
}
bool xl(char ch){
	int cnt = 0, t = 0;
	for(int i = 0; i < 4; i++){
		if(g[i][i] == ch) cnt++;
		if(g[i][i] == 'T') t++;
	}
	if(cnt + t == 4) return true;
	cnt = 0, t = 0;
	for(int i = 0; i < 4; i++){
		if(g[i][3-i] == ch) cnt++;
		if(g[i][3-i] == 'T') t++;
	}	
	if(cnt + t == 4) return true;
	return false;
}
int main() {
	freopen("A-large.in", "r", stdin);
	int cas = 1, C;
	scanf("%d", &C);
	while(C--){
		for(int i = 0; i < 4; i++){
			scanf("%s", g[i]);
		}
		bool flag = false;
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++){
				if(g[i][j] == '.')  flag = true;
			}
		}
		printf("Case #%d: ", cas++);
		if(c('X') || r('X') || xl('X')){
			puts("X won"); continue;
		}
		if(c('O') || r('O') || xl('O')){
			puts("O won"); continue;
		}
		if(!flag){
			puts("Draw");
		}
		else{
			puts("Game has not completed");
		}
	}
    return 0;
}
