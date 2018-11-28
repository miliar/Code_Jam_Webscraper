#include<stdio.h>
#include<string.h>

#define MAX 1005

#define _max(x,y)	(((x)>(y))?(x):(y))
#define _min(x,y)	(((x)<(y))?(x):(y))

int X,Y;
int mat[MAX][MAX];

int main(){

	int x,x1,x2,y,y1,y2,i,n,t;
	int T,N;

	scanf("%d",&T);
	for(N=1;N<=T;N++){

		memset(mat,0,sizeof(mat));
		scanf("%d",&n);

		X = Y = 0;
		for(i=0;i<n;i++){
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			for(x=x1;x<=x2;x++){
				for(y=y1;y<=y2;y++){
					mat[x][y] = 1;
				}
			}
			X = _max(X,x2);
			Y = _max(Y,y2);
		}
		
		int flag;
		for(t=0;;t++){
			
/*			printf("!!\n");
			for(x=0;x<=X;x++){
				for(y=0;y<=Y;y++)
					printf("%d",mat[x][y]);
				printf("\n");
			}*/

			flag = 0;
			for(x=X+1;x>=1;x--){
				for(y=Y+1;y>=1;y--){
					if(mat[x][y]==0){
						if(mat[x][y-1]==1 && mat[x-1][y]==1){
							mat[x][y] = 1;
							flag=1;
//							X = _max(X,x);
//							Y = _max(Y,y);
						}
					}
					else{
						flag = 1;
						if(mat[x][y-1]!=1 && mat[x-1][y]!=1){
							mat[x][y] = 0;	
						}
					}
				}
			}
			if(flag==0)
				break;
			X++;
			Y++;
		}

		printf("Case #%d: %d\n",N,t);


	}

	return 0;
}