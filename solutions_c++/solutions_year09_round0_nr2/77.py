#include <cstdio>
#include <algorithm>

using namespace std;

#define MAXN 110

int dx[] = {-1,0,0,1};
int dy[] = {0,-1,1,0};

int m,n;
int hgt[MAXN][MAXN];

int nb;
int basin[MAXN][MAXN];
int mp[MAXN];

char resp[MAXN][MAXN];

void calc(int x,int y){
	if(basin[x][y] >= 0){
		return ;
	}
	int i;
	int minhgt = hgt[x][y];
	int nx,ny;
	
	for(i=0;i<4;i++){
		nx = x+dx[i];
		if(nx < 0 || nx >= m) continue;
		ny = y+dy[i];
		if(ny < 0 || ny >= n) continue;
		if(hgt[nx][ny] < hgt[x][y]){
			calc(nx,ny);
			if(hgt[nx][ny] < minhgt){
				minhgt = hgt[nx][ny];
				basin[x][y] = basin[nx][ny];
			}	
		}
	}
	
	if(basin[x][y] < 0){
		basin[x][y] = nb;
		mp[nb] = -1;
		nb++;
	}
	
}

int main(){
	
	int t,lp;
	int i,j,k;
	scanf("%d",&t);
	
	for(lp=1;lp<=t;lp++){
		scanf("%d %d",&m,&n);
		for(i=0;i<m;i++){
			for(j=0;j<n;j++){
				scanf("%d",&hgt[i][j]);
				basin[i][j] = -1;
				resp[i][j] = 0;	
			}	
		}
		
		nb = 0;
		
		for(i=0;i<m;i++){
			for(j=0;j<n;j++){
				calc(i,j);	
			}	
		}
		
		k = 0;
		
		printf("Case #%d:\n",lp);
		for(i=0;i<m;i++){
			for(j=0;j<n;j++){
				if(mp[basin[i][j]] < 0){
					mp[basin[i][j]] = k;
					k++;
				}
				if(j > 0){
					printf(" ");
				}
				printf("%c",'a'+mp[basin[i][j]]);
			}
			printf("\n");	
		}
		
	}

	return 0;
}
