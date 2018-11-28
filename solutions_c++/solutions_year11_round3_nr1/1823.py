#include<stdio.h>
int main(){
	int t,i;
	scanf("%d",&t);
	for(i=0;i<t;i++){
		int r,c,j,k,hn;
		char p[51][51],ch;
		scanf("%d %d ",&r,&c);
		hn=0;
		for(j=0;j<r;j++){
			for(k=0;k<c;k++){
				scanf("%c",&p[j][k]);
				if(p[j][k]=='#')
					hn++;
			}
			scanf("%c",&ch);
		}
		if(hn==0){
			printf("Case #%d:\n",i+1);
			for(j=0;j<r;j++){
				for(k=0;k<c;k++){
					printf("%c",p[j][k]);
				}
				printf("\n");
			}
		}
		else if(hn%4!=0){
			printf("Case #%d:\nImpossible\n",i+1);
		}
		else{
			int flag=0;
			for(j=0;j<r-1;j++){
				for(k=0;k<c-1;k++){
					if(p[j][k]=='#'){
						if(p[j][k+1]=='#' && p[j+1][k]=='#' && p[j+1][k+1]=='#'){
							p[j][k]=47;p[j][k+1]=92;p[j+1][k]=92;p[j+1][k+1]=47;
						}
						else{
							flag=1;
							break;
						}
					}
				}
				if(flag==1)
					break;
			}
			if(flag==1)
				printf("Case #%d:\nImpossible\n",i+1);
			else{
				flag=0;
				for(j=0;j<c;j++){
					if(p[r-1][j]=='#'){
						flag=1;
						break;
					}
				}
				if(flag!=1){
					for(j=0;j<r;j++){
						if(p[j][c-1]=='#'){
							flag=1;
							break;
						}
					}
				}
				if(flag==1)
					printf("Case #%d:\nImpossible\n",i+1);
				else{
					printf("Case #%d:\n",i+1);
					for(j=0;j<r;j++){
						for(k=0;k<c;k++){
							printf("%c",p[j][k]);
						}
						printf("\n");
					}
				}
			}
		}
	}
	return 0;
}
