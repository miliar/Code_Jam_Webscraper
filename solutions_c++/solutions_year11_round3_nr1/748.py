#include <iostream>
#include <cstdio>

using namespace std;

char tile[60][60];

int main() {
	
	int t, r, c;
	
	scanf("%d", &t);
	
	for (int k = 1; k <= t; k++) {
		
		scanf("%d %d", &r, &c);
		
		for (int i = 0; i < r; i++)
			scanf("%s", &tile[i]);
		
		bool dasie = true;
		
		for (int i = 0; i < r && dasie; i++) {
			for (int j = 0; j < c && dasie; j++) {
				
				if (tile[i][j] == '#') {
					
					if (i < r - 1 && tile[i+1][j] == '#' && j < c - 1 && tile[i][j+1] == '#' && tile[i+1][j+1] == '#') {
						
						tile[i][j] = tile[i+1][j+1] = '/';
						tile[i+1][j] = tile[i][j+1] = '\\';
					} else {
						dasie = false;
						break;
					}
				}
			}
		}
		
		printf("Case #%d:\n", k);
		
		if (!dasie) {
			printf("Impossible\n");
		} else {
			for (int i = 0; i < r; i++)
				printf("%s\n", tile[i]);
		}
	}
	
	return 0;
	
}
