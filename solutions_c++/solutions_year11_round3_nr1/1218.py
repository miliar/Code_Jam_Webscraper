#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>

using namespace std;

char pic[52][52];
int T,n,m;


void mostra(){
	int i,j;
	for(i=1;i<=n;i++){
	 for(j=1;j<=m;j++){
	  printf("%c",pic[i][j]);
	 }
	 printf("\n");
	}

}

int main(){
	int i,j,erro,teste=1;
	
	scanf("%d",&T);
	
	while(T--){
	
		scanf("%d %d",&n,&m);
	
		for(i=1;i<=n;i++){
			scanf("%s",&pic[i][1]);
		}
		
		for(i=0;i<n+2;i++)
		  pic[i][0] = pic[i][m+1] = '.';
		
		for(i=0;i<m+2;i++)
		  pic[0][i] = pic[n+1][i] = '.';
		
		//mostra();
		
		erro = 0;
		
		for(i=1;i<=n;i++){
			for(j=1;j<=m;j++){
				if(pic[i][j]=='#'){
					if(pic[i][j+1]=='#' && pic[i+1][j]=='#' && pic[i+1][j+1]=='#'){
						pic[i][j] = '/';
						pic[i][j+1]='\\';
						pic[i+1][j]='\\';
						pic[i+1][j+1]='/';
						//mostra();
					}else{
						erro =1;
					}  
				}
			}
		}
		
		printf("Case #%d:\n",teste++);
		if(erro){
			printf("Impossible\n");
		}else{
		  mostra();
		}
			
	
	}
	
	
  return 0;
}
