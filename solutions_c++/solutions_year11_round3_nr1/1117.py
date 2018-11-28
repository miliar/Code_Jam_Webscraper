#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <string>
#include <algorithm>
#include <math.h>
using namespace std;
const int max_size=103;

char grid[max_size][max_size];

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T,R,C;
	scanf("%d",&T);
	for(int t=0;t<T;t++){
		scanf("%d%d",&R,&C);
		getchar();

		for(int i=0;i < R ; i++){
			for(int j=0; j<C; j++){
				grid[i][j] = getchar();
			}
			getchar();
		}
		bool can = true;
		for(int i=0;i < R && can ; i++){
			for(int j=0; j<C && can; j++){
				if(grid[i][j]=='#'){
					if(i<R-1 && j<C-1){
						if(grid[i+1][j]=='#' && grid[i][j+1]=='#' && grid[i+1][j+1]=='#'){\
							grid[i][j] = '/';
							grid[i+1][j+1] = '/';
							grid[i+1][j] = '\\';
							grid[i][j+1] = '\\';
						}
						else
							can = false;
					}
					else
						can = false;
				}
			}			
		}	
		printf("Case #%d:\n",t+1);
		if(can){
			for(int i=0;i < R ; i++){
				for(int j=0; j<C; j++){
					printf("%c",grid[i][j]);
				}
				printf("\n");
			}
		}
		else
			printf("Impossible\n");
	}
	return 0;
}