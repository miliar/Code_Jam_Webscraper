#include <stdio.h>

int T,r,c;
char t[100][100];

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int lT,i,j;
	scanf("%d",&T);
	for(lT=1;lT<=T;lT++){
		scanf("%d%d",&r,&c);
		for(i=0;i<r;i++)
			scanf("%s",t[i]);
		for(i=0;i<r-1;i++){
			for(j=0;j<c-1;j++){
				if(t[i][j]=='#'&&t[i][j+1]=='#'&&t[i+1][j]=='#'&&t[i+1][j+1]=='#'){
					t[i][j]=t[i+1][j+1]='/';
					t[i][j+1]=t[i+1][j]='\\';
				}
			}
		}
		for(i=0;i<r;i++){
			for(j=0;j<c;j++)
				if(t[i][j]=='#')
					break;
			if(j<c)break;
		}
		printf("Case #%d:\n",lT);
		if(i<r){
			printf("Impossible\n");
		}else{
			for(i=0;i<r;i++)
				printf("%s\n",t[i]);
		}
	}
	return 0;
}