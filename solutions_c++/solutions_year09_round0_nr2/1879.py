#include<stdio.h>
#include<string.h>
int Map[150][150],X[4]={-1,0,0,1},Y[4]={0,-1,1,0};
int n,m,Temp[150][150],Value;
char Res[150][150];
int DFS(int x,int y){
	int i,Min=2147483647,Index;
	for(i = 0 ; i < 4 ; i++){
		if(Min > Map[x+X[i]][y+Y[i]]){
			Min=Map[x+X[i]][y+Y[i]];
			Index=i;
		}
	}
	if(Map[x][y] > Map[x+X[Index]][y+Y[Index]]) Res[x][y]=DFS(x+X[Index],y+Y[Index]);
	else if(Res[x][y]==0) Res[x][y]='a'+Value++;
	
	return Res[x][y];
	
	
}
int main(){
	int Case,i,j;
	freopen("input_la.txt","r",stdin);
	freopen("output_la.txt","w",stdout);
	scanf("%d",&Case);
	for(int I = 1 ; I <= Case ; I++){
		scanf("%d%d",&n,&m);
		memset(Map,1,sizeof(Map));
		memset(Res,0,sizeof(Res));
		for(i = 1 ; i <= n ; i++){
			for(j = 1 ; j <= m ; j++){
				scanf("%d",&Map[i][j]);
			}
		}
		Value=0;
		for(i = 1 ; i <= n ; i++){
			for(j = 1 ; j <= m ; j++){
				if(Res[i][j]==0) DFS(i,j);
			}
		}
		printf("Case #%d:\n",I);
		for(i = 1 ; i <= n ; i++){
			for(j = 1 ; j <= m ; j++){
				printf("%c ",Res[i][j]);
			}
			printf("\n");
		}
	}
	return 0;
}