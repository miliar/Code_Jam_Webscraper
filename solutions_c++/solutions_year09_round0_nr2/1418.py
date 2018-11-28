#include<cstdio>

int h,w;

int t[105][105];

int res[105][105];

int dir[105][105];

bool v[105][105];

int dy[] = {-1,0,0,1};
int dx[] = {0,-1,1,0};

void dfs(int y,int x){
	v[y][x] = 1;
	int ny = y+dy[dir[y][x]];
	int nx = x+dx[dir[y][x]];
	if(!v[ny][nx]) dfs(ny,nx);
	res[y][x] = res[ny][nx];
}

char letter[10005];

void alg(){
	for(int i=0;i<105;i++) for(int j=0;j<105;j++){
		t[i][j] = 1000000000;
		v[i][j] = 0;
	}
	for(int i=1;i<=1000;i++) letter[i] = 0;
	scanf("%d%d",&h,&w);
	for(int i=1;i<=h;i++){
		for(int j=1;j<=w;j++){
			scanf("%d",&t[i][j]);
		}
	}
	int cs = 1;
	for(int i=1;i<=h;i++){
		for(int j=1;j<=w;j++){
			int csm = t[i][j];
			dir[i][j] = -1;
			for(int k=0;k<4;k++){
				if(t[i+dy[k]][j+dx[k]] < csm){
					csm = t[i+dy[k]][j+dx[k]];
					dir[i][j] = k;
				}
			}
			if(dir[i][j] == -1){
				v[i][j] = 1;
				res[i][j] = cs++;
			}
		}
	}
	for(int i=1;i<=h;i++){
		for(int j=1;j<=w;j++){
			if(!v[i][j]){
				dfs(i,j);
			}
		}
	}
	char cl = 'a';
	for(int i=1;i<=h;i++){
		for(int j=1;j<=w;j++){
			if(!letter[res[i][j]]) letter[res[i][j]] = cl++;
			printf("%c",letter[res[i][j]]);
			if(j<w) printf(" ");
		}
		printf("\n");
	}
}

int main(){
	int d;
	scanf("%d",&d);
	for(int i=1;i<=d;i++){
		printf("Case #%d:\n",i);
		alg();
	}
}
