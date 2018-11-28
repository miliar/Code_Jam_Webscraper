#include <iostream>
#include <cstdio>
using namespace std;

#define FOR(i, M) for( int i = 0; i < (M); ++i )

#define MAX 51
char grid[MAX][MAX];
int R , C;

bool transform(){
	FOR(i, R){
		FOR(j, C){
			if(grid[i][j] == '#'){
				if (i < R - 1 && j < C - 1 && grid[i+1][j] == '#' && grid[i][j+1] == '#' && grid[i+1][j+1] == '#'){
					grid[i][j] = '/';
					grid[i+1][j] = '\\';
					grid[i][j+1] = '\\';
					grid[i+1][j+1] = '/';
				}
				else return false;
			}
		}
	}
	return true;
}

int main(){
    int T;
    cin >> T;
    for( int t = 1; t <= T; ++t ){
    	cin >> R >> C;
    	FOR(i, R){
			FOR(j, C){
				cin >> grid[i][j];
			}
		}
		printf("Case #%d:\n", t);
		if (transform()) {
			FOR(i, R){
				FOR(j,C){
					printf("%c", grid[i][j]);
				}
				printf("\n");
			}
		}
		else printf("Impossible\n");
		
    }
}
