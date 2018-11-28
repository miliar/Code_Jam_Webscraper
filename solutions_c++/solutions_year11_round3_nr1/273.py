#include <iostream>
#include <algorithm>
#include <cstdio>
using namespace std;
char mat[55][55], n_case, r, c;
int main(){
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
	int C;
	scanf("%d", &C);
	while(C--){
		scanf("%d%d", &r, &c);
		for(int i = 0; i < r; i++){
			scanf("%s", mat[i]);	
		}
		for(int i = 0; i < r; i++){
			for(int j = 0; j < c; j++){
				if(i+1 >= r || j+1 >= c) continue;
				if(mat[i][j] != '#') continue;
				if(mat[i+1][j] != '#') continue;
				if(mat[i][j+1] != '#') continue;
				if(mat[i+1][j+1] != '#') continue;
				mat[i][j] = '/', mat[i][j+1] = '\\', mat[i+1][j] = '\\', mat[i+1][j+1] = '/';
			}	
		}
		int fail = 0;
		for(int i = 0; i < r; i++){
			for(int j = 0; j < c; j++){
				if(mat[i][j] == '#') {
					fail = 1;
					break;	
				}	
			}	
		}
		printf("Case #%d:\n", ++n_case);
		if(fail){
			printf("Impossible\n");	
		} else {
			for(int i = 0; i < r; i++){
				for(int j = 0; j < c; j++){
					printf("%c", mat[i][j]);
					if(j == c-1) printf("\n");	
				}	
			}
		}
	}	
}
