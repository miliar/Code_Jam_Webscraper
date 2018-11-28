#include <stdio.h>

char mat[53][53];

int main() {
	freopen("input.in","r",stdin);
	freopen("output.in","w",stdout);
	
	int tests,rows,cols;
	scanf("%d",&tests);
	
	for(int testNo=1; testNo<=tests; testNo++) {
		scanf(" %d %d",&rows,&cols);
		
		for(int i=1;i<=rows;i++) {
			for(int j=1;j<=cols;j++) {
				scanf(" %c",&mat[i][j]);
			}
		}
		
		printf("Case #%d:\n",testNo);
		
		for(int i=1;i<=rows;i++) {
			for(int j=1;j<=cols;j++) {
				if(mat[i][j]=='#') {
					if( i<rows && j<cols && mat[i][j+1]=='#' && mat[i+1][j]=='#' && mat[i+1][j+1]=='#' ) {
						mat[i+1][j+1]=mat[i][j]='/';
						mat[i][j+1]=mat[i+1][j]='\\';
					} else {
						printf("Impossible\n");
						goto loopEnd;
					}
				}
			}
		}
		
		for(int i=1;i<=rows;i++) {
			for(int j=1;j<=cols;j++) {
				printf("%c",mat[i][j]);
			}
			printf("\n");
		}
		
		loopEnd:;
	}
	return 0;
}
