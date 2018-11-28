#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

char m[4][4];

int main(){
	int t, c = 1;
	
	scanf("%d", &t);
	while(t--){
		int incompleto = 0;
		for(int i = 0; i < 4; ++i){
			for(int j = 0; j < 4; ++j){
				scanf(" %c", &m[i][j]);
				if(m[i][j] == '.') incompleto = 1;
			}
		}
			
		//row
		int o = 0, x = 0;
		for(int i = 0; i < 4; ++i){
			x = 1; o = 1;
			for(int j = 0; j < 4; ++j){
				if(m[i][j] != 'X' && m[i][j] != 'T') x = 0;
				if(m[i][j] != 'O' && m[i][j] != 'T') o = 0;
			}
			if(x){
				printf("Case #%d: X won\n", c++);
				break;
			}
			if(o){
				printf("Case #%d: O won\n", c++);
				break;
			}
		}
		if(x || o) continue;
		
		//col
		x = o = 0;
		for(int i = 0; i < 4; ++i){
			x = 1; o = 1;
			for(int j = 0; j < 4; ++j){
				if(m[j][i] != 'X' && m[j][i] != 'T') x = 0;
				if(m[j][i] != 'O' && m[j][i] != 'T') o = 0;
			}
			if(x){
				printf("Case #%d: X won\n", c++);
				break;
			}
			if(o){
				printf("Case #%d: O won\n", c++);
				break;
			}
		}
		if(x || o) continue;
		
		//diag
		x = o = 1;
		for(int i = 0; i < 4; ++i){
			if(m[i][i] != 'X' && m[i][i] != 'T') x = 0;
			if(m[i][i] != 'O' && m[i][i] != 'T') o = 0;
		}
		if(x){
			printf("Case #%d: X won\n", c++);
			continue;
		}
		if(o){
			printf("Case #%d: O won\n", c++);
			continue;
		}
		
		x = o = 1;
		for(int i = 0; i < 4; ++i){
			if(m[i][3-i] != 'X' && m[i][3-i] != 'T') x = 0;
			if(m[i][3-i] != 'O' && m[i][3-i] != 'T') o = 0;
		}
		if(x){
			printf("Case #%d: X won\n", c++);
			continue;
		}
		if(o){
			printf("Case #%d: O won\n", c++);
			continue;
		}
		
		if(incompleto){
			printf("Case #%d: Game has not completed\n", c++);
			continue;
		}
		printf("Case #%d: Draw\n", c++);
	}

return 0;
}
