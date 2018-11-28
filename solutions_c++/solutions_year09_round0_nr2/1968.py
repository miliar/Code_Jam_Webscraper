#include<iostream>
#include<cstring>
using namespace std;
#define SM 12
#define LG 110
#define inf 1<<30
int data[LG][LG],r,c,v,t,txt;
int dx[]={-1,0,0,1};
int dy[]={0,-1,1,0};
char mask[LG][LG];
int pos;
char dfs(int x,int y){
	int nx,ny,xx,yy,i,j;
	if(mask[x][y])return mask[x][y];
	nx=ny=inf;
	for(i=0;i<4;i++){
		xx=x+dx[i];
		yy=y+dy[i];
		if(xx>r||xx<1||yy>c||yy<1)continue;
		if(data[xx][yy]<data[x][y]){
			if(nx==inf||ny==inf)nx=xx,ny=yy;
			else if(data[xx][yy]<data[nx][ny])nx=xx,ny=yy;
		}
	}
	if(nx==inf||ny==inf){
		mask[x][y]=pos++;
		return mask[x][y];
	}
	char ch=dfs(nx,ny);
	return mask[x][y]=ch;
}
int main(){
	//freopen("1.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	int i,j,k;
	while(scanf("%d",&t)==1){
		while(t--){
			scanf("%d%d",&r,&c);
			memset(mask,0,sizeof(mask));
			for(i=1;i<=r;i++)for(j=1;j<=c;j++)scanf("%d",&data[i][j]);
			pos='a';
			for(i=1;i<=r;i++){
				for(j=1;j<=c;j++){
					//printf("%d ",data[i][j]);
					if(mask[i][j])continue;
					char ch=dfs(i,j);
				}
				//printf("\n");
			}
			printf("Case #%d:\n",++txt);
			for(i=1;i<=r;i++){
				for(j=1;j<=c;j++){
					if(j>1)printf(" ");
					printf("%c",mask[i][j]);
				}
				printf("\n");
			}
		}
	}
	return 0;
}