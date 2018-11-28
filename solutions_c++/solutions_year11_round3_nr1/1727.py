#include <stdio.h>
#include <string.h>

#include <iostream>
#include <algorithm>
using namespace std;

char field[51][51];
int R, C;

int main() {

	int tt;
	scanf("%d", &tt);
	
	for (int casen=1;casen<=tt;++casen) {
		printf("Case #%d:\n", casen);
		scanf("%d%d", &R, &C);
		
		
		for (int i=0;i<R;i++) {
			scanf("%s", field[i]);
		}
		
		bool broken=false;
		
		for (int y=0;y<R;y++) {
			for (int x=0;x<C;x++) {
				if (field[y][x]=='#') {
				
					if (x==C-1||y==R-1) {
						broken=true;
						break;
					}
					
					if (field[y+1][x]=='#'&&field[y][x+1]=='#'&&field[y+1][x+1]=='#') {
						field[y][x]='/';
						field[y+1][x]='\\';
						field[y][x+1]='\\';
						field[y+1][x+1]='/';
					
					} else if (
						field[y+1][x]=='#'||
						field[y][x+1]=='#'||
						field[y+1][x+1]=='#') {
					
						broken=true;
						break;
					}
					
				}
			}
			if (broken) break;
		}
		
		
		if (!broken) {
			for (int y=0;y<R;y++) {
				printf("%s\n", field[y]);
			}
		} else {
			printf("Impossible\n");
		}
	}
}
