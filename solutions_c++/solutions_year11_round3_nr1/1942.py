#include<stdio.h>
#define MAX 52
int T,caseno=1;
int R,C;
char c;
char grid[MAX][MAX];

void replace(){
		int i,j,k;
		for(i=0;i<R;i++){
			for(j=0;j<C;j++){
				if(grid[i][j]=='#' && grid[i+1][j]=='#' && grid[i][j+1]=='#' &&grid[i+1][j+1]=='#'){
						grid[i][j]='/';
						grid[i][j+1]='\\';
						grid[i+1][j]='\\';
						grid[i+1][j+1]='/';
				}		
			}
		}
		
}

bool check(){
	int i,j,k;
	for(i=0;i<R;i++){
			for(j=0;j<C;j++){
				if(grid[i][j]=='#'){ return false;}
			}
	}
	return true;
}

int main(){
		int i,j,k;
		scanf("%d",&T);
		while(caseno<=T){
				scanf("%d%d",&R,&C);
				
				scanf("%c",&c);
				for(i=0;i<R;i++){
					for(j=0;j<C;j++)
						scanf("%c",&grid[i][j]);
					scanf("%c",&c);
				}
				/*for(i=0;i<R;i++){
					for(j=0;j<C;j++)
						printf("%c",grid[i][j]);
					printf("\n");
				}*/
				replace();
				printf("Case #%d:\n",caseno++);
				if(check()){
					for(i=0;i<R;i++){
					for(j=0;j<C;j++)
						printf("%c",grid[i][j]);
					printf("\n");
				}
				}
				else
					printf("Impossible\n");
				
				
		}
		
		return 0;
}
