#include <iostream>
#include <stdio.h>
using namespace std;

char s[4][4];

char slution(){
	char c = 0;
	int i, j;
	for(i = 0; i < 4; ++i){
		c = s[i][0];
		if(c == 'T') c = s[i][1];
		for(j = 0; j < 4; ++j){
			char a = s[i][j];
			if(a == '.' || (a != c && a != 'T')) break;
		}
		if(j == 4) return c;
	}
	
	for(j = 0; j < 4; ++j){
		c = s[0][j];
		if(c == 'T') c = s[1][j];
		for(i = 0; i < 4; ++i){
			char a = s[i][j];
			if(a == '.' || (a != c && a != 'T')) break;
		}
		if(i == 4) return c;
	}
	
	c = s[0][3];
	if(c == 'T') c = s[1][2];
	for(i = 0; i < 4; ++i){
		char a = s[i][3 - i];
		if(a == '.' ||(a != c && a != 'T')) break;
	}
	if(i == 4) return c;
	
	c = s[0][0];
	if(c == 'T') c = s[1][1];
	for(i = 0; i < 4; ++i){
		char a = s[i][i];
		if(a == '.' || (a != c && a != 'T')) break;
	}
	if(i == 4) return c;
	
	return 0;
}

int main(void){
	int n = 0, k = 0, flag = 0;
	char c = 0;
	cin >> n;
	while(k++ < n){
		flag = 0;
		for(int i = 0; i < 4; ++i){
			for(int j = 0; j < 4; ++j){
				cin >> c;
				if(c == '.') flag = 1;
				s[i][j] = c;
			}
		}
		char r = slution();
		if(r == 0 && !flag) printf("Case #%d: Draw\n", k);
		else if(r == 0 && flag) printf("Case #%d: Game has not completed\n", k);
		else printf("Case #%d: %c won\n", k, r);
	}
	return 0;
}

