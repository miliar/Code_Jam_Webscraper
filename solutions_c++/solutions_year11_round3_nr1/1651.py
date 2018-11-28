#include <cstdlib>
#include <cstdio>

int main(){
	int CASES, CASESNUMBER = 1;
	scanf("%d\n",&CASES);
	char grid[100][100];
	int R, C;
	int success;
	while(CASES--){
		scanf("%d %d\n",&R, &C);
		for(int i=0; i<R; i++){
			scanf("%s\n",grid[i]);
		}
		success = 1;
		for(int i=0; i<C+1; i++){
			grid[R][i] = '.';
		}
		
		for(int i=0; success && i<R; i++){
			for(int j=0; success && j<C; j++){
				if(grid[i][j] == '#'){
					if(grid[i+1][j] == '#' && grid[i][j+1] == '#'
						&& grid[i+1][j+1] == '#'){
						grid[i][j] = '/';
						grid[i][j+1] = '\\';
						grid[i+1][j+1] = '/';
						grid[i+1][j] = '\\';
					}else {
						success = 0;
					}
				}
			}
		}
		printf("Case #%d:\n",CASESNUMBER++);
		if(success){
			for(int i=0;i<R;i++){
				printf("%s\n",grid[i]);
			}
		}else {
			printf("Impossible\n");
		}
		
		
	}
	
}
