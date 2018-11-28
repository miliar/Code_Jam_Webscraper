#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <queue>
#include <map>
#include <vector>
#include <string>
#include <cctype>
#include <set>
#include <utility>
#include <stack>
#include <iostream>

using namespace std;

int n,t,tem;
typedef long long ll;

char ent[5][6];

int rangei[4] = { 1,1,1,0};
int rangej[4] = {-1,0,1,1};

bool check(char x){
	for(int i = 0; i < 4; ++i){
		for(int j = 0; j < 4; ++j){
			if(ent[i][j] == '.') tem = true;
			if(x == ent[i][j] || ent[i][j] == 'T'){
				for(int k = 0; k < 4; ++k){
					int ii = i, jj = j;
					for(int z = 0; z < 3; ++z){
						ii += rangei[k];
						jj += rangej[k];
						if(ii < 0 || ii > 3 || jj < 0 || jj > 3) goto sai;
						if(ent[ii][jj] != x && ent[ii][jj] != 'T') goto sai;
					}
					return true;
					sai:;
				}
			}
		}
	}
	return false;
}

int main (){
	#ifdef INTERNO
		freopen("in", "r", stdin);
		freopen("out", "w", stdout);
	#endif
	scanf("%d", &t);
	for(int _ = 1; _ <= t; ++_){
		tem = false;
		for(int i = 0; i < 4; ++i) scanf("%s", ent[i]);
		printf("Case #%d: ", _);
		if(check('X')) printf("X won\n");
		else if(check('O')) printf("O won\n");
		else if(tem) printf("Game has not completed\n");
		else printf("Draw\n");
	}
	return 0;
}
