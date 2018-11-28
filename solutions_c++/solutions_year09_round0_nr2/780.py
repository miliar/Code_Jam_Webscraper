#include <iostream>
#include <cmath>
#include <string>

#define TASK "file"
#define N 150
using namespace std;

int dx[5]={0,-1, 0, 0, 1};
int dy[5]={0, 0,-1, 1, 0};
int ref[5]={0,3,4,1,2};

int map[N][N];
int dir[N][N];
int used[N][N];
char name[N][N];
int test,n,m;
int ans;

void dfs(int x,int y){
	if (used[x][y]) return;
	//printf("%i %i ->",x,y);
	used[x][y]=1;
	if (dir[x][y]==0){
		ans++;
		name[x][y]=(char)('a'+ans-1);		
	}else{
		int nx=x+dx[dir[x][y]];
		int ny=y+dy[dir[x][y]];
			
		dfs(nx,ny);
		name[x][y]=name[nx][ny];		
	}
}

int main(void){
	freopen(TASK".in","r",stdin);
	freopen(TASK".out","w",stdout);
	cin>>test;
	for (int z=0;z<test;z++){
		printf("Case #%i:\n",z+1);
		cin>>n>>m;
		for (int i=0;i<n;i++){
			for (int j=0;j<m;j++){
				cin>>map[i][j];
				dir[i][j]=0;
				used[i][j]=0;
			}
		}
		for (int i=0;i<n;i++){
			for (int j=0;j<m;j++){
				int flag=0;
				int small = map[i][j];
				for (int k=1;k<5;k++){
					int nx=i+dx[k];
					int ny=j+dy[k];
					if (nx>=0 && ny>=0 && nx<n && ny<m){
						if (map[nx][ny]<small){
							small=map[nx][ny];
							flag=k;
						}
					}
				}
				dir[i][j]=flag;
				
			}
		}
		ans=0;
		for (int i=0;i<n;i++){
			for (int j=0;j<m;j++){
				if (!used[i][j]){
					dfs(i,j);

				}
				//printf("\n");
			}
		}
		for (int i=0;i<n;i++){
			for (int j=0;j<m;j++){
				printf("%c ",name[i][j]);
			}
			printf("\n");
		}
	}

	return 0;
}