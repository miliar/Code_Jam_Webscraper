#include<iostream>
#include<algorithm>
#include<queue>
using namespace std;

struct 
{
	int x,y;
}offset[4]={{-1,0},{0,-1},{0,1},{1,0}};

int mat[110][110];
char ans[110][110];
char letter;


char  dfs(int x,int y)
{
	if( ans[x][y] )return ans[x][y];
	ans[x][y]=letter;
	int Min=100000;
	for(int i=0;i<4;i++)
		Min=min(Min,mat[x+offset[i].x][y+offset[i].y]);
	if( Min>=mat[x][y]){
		ans[x][y]=letter;
		letter++;
		return ans[x][y];
	}
	for(int i=0;i<4;i++){
		int xx,yy;
		xx=offset[i].x+x;
		yy=offset[i].y+y;
		if( Min==mat[xx][yy] ){
			ans[x][y]=dfs(xx,yy);
			return ans[x][y];
		}
	}
}


int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T,H,W;
	int Case=1;
	scanf("%d",&T);
	while(T--){
		scanf("%d %d",&H,&W);
		for(int i=0;i<=H+1;i++)
			for(int j=0;j<=W+1;j++)
				mat[i][j]=100000;
		for(int i=1;i<=H;i++)
			for(int j=1;j<=W;j++)
				scanf("%d",&mat[i][j]);
		memset(ans,0,sizeof(ans));
		 letter='a';
		for(int i=1;i<=H;i++){
			for(int j=1;j<=W;j++){
				if( ans[i][j])continue;
				dfs(i,j);
			}
		}
		printf("Case #%d:\n",Case);
		Case++;
		for(int i=1;i<=H;i++){
			int j=1;
			for( ;j<W;j++)
				printf("%c ",ans[i][j]);
			printf("%c\n",ans[i][j]);
		}
	}
	return 0;
}
				