/*
ID: qazzaq71
PROG: packrec
LANG: C++
*/
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>

using namespace std;

typedef long long ll;

char s[10][10];
int res;

bool win(char p){
	for(int i = 0; i < 4; i++){
		int ok = 1;
		for(int j = 0; j < 4; j++){
			if(s[i][j] != p){
				ok = 0;
				break;
			}
		}
		if(ok){
			return true;
		}
		ok = 1;
		for(int j = 0; j < 4; j++){
			if(s[j][i] != p){
				ok = 0;
				break;
			}
		}
		if(ok){
			return true;
		}		
	}
	int ok = 1;
	for(int i = 0; i < 4; i++){
		if(s[i][i] != p){
			ok = 0;
			break;
		}
	}
	if(ok){
		return true;
	}
	ok = 1;
	for(int i = 0; i < 4; i++){
		if(s[i][3 - i] != p){
			ok = 0;
			break;
		}
	}
	if(ok){
		return true;
	}
	return false;
}
bool full(){
	for(int i = 0; i < 4; i++){
		for(int j = 0; j < 4; j++){
			if(s[i][j] == '.'){
				return false;
			}
		}
	}
	return true;
}
void status(){
	if(win('X')){
		res = 1;
	} else if(win('O')){
		res = 2;
	} else if(full()){
		res = 0;
	} else {
		res = -1;
	}
}
int main(){
#ifdef DEBUG
	FILE * ptrFILE=freopen("a.in","r",stdin);
	assert(ptrFILE!=NULL);
	ptrFILE=freopen("a.out","w",stdout);
	assert(ptrFILE!=NULL);
#endif
	int t;
	scanf("%d", &t);
	for(int cs = 1; cs <= t; cs++){
		for(int i = 0; i < 4; i++){
			scanf(" %s ", s[i]);
		}
		int tr = -1, tc = -1;
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++){
				if(s[i][j] == 'T'){
					tr = i;
					tc = j;
				}
			}
		}
		if(tr != -1 && tc != -1){
			s[tr][tc] = 'O';
			status();
			if(res == -1 || res == 0){
				s[tr][tc] = 'X';
				status();				
			}

		} else{
			status();
		}
		if(res  == -1){
			printf("Case #%d: Game has not completed\n", cs);
		} else if(res == 0){
			printf("Case #%d: Draw\n", cs);
		} else if(res == 1){
			printf("Case #%d: X won\n", cs);
		} else {
			printf("Case #%d: O won\n", cs);
		}
	}
    return 0;
}
