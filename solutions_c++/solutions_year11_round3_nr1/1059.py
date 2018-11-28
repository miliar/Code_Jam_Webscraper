#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void){
	int t,k=0;
	freopen("A-large.in","r",stdin);
	freopen("result.txt","w",stdout);
	scanf("%d",&t);
	while(k++<t){
		char gp[60][60];
		int R,C,i,j,flag=1;
		scanf("%d%d",&R,&C);
		for(i=0;i<R;i++)
			scanf(" %s",gp[i]);
		for(i=0;i<R;i++)
			for(j=0;j<C;j++){
				if(gp[i][j]=='#'){
					if(i==R-1||j==C-1){
						flag=0;
						break;
					}
					if((gp[i][j+1]!='#') || (gp[i+1][j]!='#') || (gp[i+1][j+1]!='#')){
						flag=0;
						break;
					}else{
						gp[i][j]='/',gp[i][j+1]='\\',gp[i+1][j]='\\',gp[i+1][j+1]='/';
					}
				}
			}
		printf("Case #%d:\n",k);
		if(!flag){
			printf("Impossible\n");
		}else{
			for(i=0;i<R;i++)
				printf("%s\n",gp[i]);
		}
	}
	return 0;
}
