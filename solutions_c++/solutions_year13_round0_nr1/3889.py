#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <algorithm>
#include <vector>
#include <cmath>
#include <queue>
#include <string>
#include <map>

using namespace std;

char grid[10][10];
                                           // inicia em 0, 4
int inis[10][3] = { {0, 0, 0}, {1, 0, 0}, {2, 0, 0}, {3, 0, 0}, 
 					{0, 0, 1}, {0, 1, 1}, {0, 2, 1}, {0, 3, 1},
					{0, 0, 2}, {3, 0, 3} };
int range[4][2] = { {0, 1}, {1,0}, {1, 1}, {-1, 1} };

char check[4][5];

int main() {
	
	int casos, caso = 0;
	scanf("%d", &casos);
	bool notended;
	
	
	
	/*
	for (int a = 0; a < 10; ++a) {
		int ii = inis[a][0];
		int jj = inis[a][1];
		memset(check, '.', sizeof(check));
		
		for (int x = 0; x < 4; ++x) {
			check[ii][jj] = 'x';
			
			ii += range[inis[a][2]][0];
			jj += range[inis[a][2]][1];
		}
		printf("\n");
			for(int i = 0; i < 4; ++i){
				check[i][4] = 0;
				printf("%s\n", check[i]);
			}
	}
	*/
	while (casos--) {
		++caso;
		notended = false;
		for(int i = 0; i < 4; ++i) {
			scanf("%s", grid[i]);
			for( int j = 0; grid[i][j]; ++j) {
				if (grid[i][j] == '.') notended = true;
			}
		}
		printf("Case #%d: ", caso);
		char ats[2] = {'X', 'O'};
		for (int k = 0; k < 2; ++k) {
			char at = ats[k];
			for (int a = 0; a < 10; ++a) {
				int ii = inis[a][0];
				int jj = inis[a][1];
				
				bool ok = true;
				for (int x = 0; x < 4; ++x) {
					//printf("%d %d %c\n", ii, jj, at);
					if (grid[ii][jj] == at || grid[ii][jj] == 'T') {
					
					} else {
					//	printf(">> %d %d %c\n", ii, jj, grid[ii][jj]);
						ok = false; break;
					}
					check[ii][jj] = 'x';
					
					ii += range[inis[a][2]][0];
					jj += range[inis[a][2]][1];
				}
				if (ok) {
					printf("%c won\n", at);
					goto cont;
				}
			}
		}
		if (notended) {
			printf("Game has not completed\n");
		} else {
			printf("Draw\n");
		}
		cont: ;
	}
	
	
	return 0;
}