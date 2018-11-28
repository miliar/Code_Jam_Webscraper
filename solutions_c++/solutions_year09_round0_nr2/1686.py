#include<iostream>
#include<cstdio>
#include<cstring>

using namespace std;

int dir[4][2] = { {-1,0},{0,-1},{0,1},{1,0} };
int map[110][110];
int basin[110][110];
int ba;
int H,W;

void dfs(int i,int j){		//cout<<i<< " "<<j<<endl;system("pause");
	
	int mh = map[i][j];
	int nx,ny;
	for(int k = 0; k < 4; k++)
		if( map[i+dir[k][0]][j+dir[k][1]] < mh ){
			mh = map[i+dir[k][0]][j+dir[k][1]];
			nx = i+dir[k][0];
			ny = j+dir[k][1];
		}
	if( mh < map[i][j] ){
		if( basin[nx][ny] )
			basin[i][j] = basin[nx][ny];
		else{
			  dfs(nx,ny);
			  basin[i][j] = basin[nx][ny];
			}
	}
	else	basin[i][j] = ba++;
	
	return ;
}
	
	

int main()
{
	freopen("water.out","w",stdout);
	int t, cas = 1;
	scanf("%d",&t);
	while( t-- ){
		
		memset(map,127,sizeof(map));
		memset(basin,0,sizeof(basin));
		ba = 1;
				
		scanf("%d%d",&H,&W);
		for(int i = 1; i <= H; i++)
			for(int j = 1; j <= W; j++)
				scanf("%d",&map[i][j]);
		
		for(int i = 1; i <= H; i++)
			for(int j = 1; j <= W; j++)
				if( !basin[i][j] )
					dfs(i,j);
		
		printf("Case #%d:\n",cas++);
		for(int i = 1; i <= H; i++){
			for(int j = 1; j <= W; j++)
				printf("%c ",basin[i][j]+'a'-1);
			printf("\n");
		}
	}
	return 0;
}

					
