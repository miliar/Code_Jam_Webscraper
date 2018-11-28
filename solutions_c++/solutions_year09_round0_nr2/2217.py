#include <cstdio>
#include <cstring>

int map[110][110];
char ret[110][110];
char basin;
int w,h;

int dir[4][2] = {{-1,0},{0,-1},{0,1},{1,0}};

char dfs(int i,int j){
	if (ret[i][j])
		return ret[i][j];
	int tx,ty,low_k,lowest = map[i][j];
	for (int k=0;k<4;k++){
		tx = i + dir[k][0];
		ty = j + dir[k][1];
		if (tx >= 0 && tx < h && ty >=0 && ty < w){
			if (map[tx][ty] < lowest){
				lowest = map[tx][ty];
				low_k = k;
			}
		}
	}
	if (lowest == map[i][j])
		return ret[i][j] = basin++;
	else
		return ret[i][j] = dfs(i+dir[low_k][0],j+dir[low_k][1]);
}

int main(){
	int count,i,j,t;
	freopen("B-large.in","r",stdin);
	freopen("output.out","w",stdout);
	scanf("%d",&count);
	for (t=1;t<=count;t++){
		scanf("%d%d",&h,&w);
		for (i=0;i<h;i++)
			for (j=0;j<w;j++)
				scanf("%d",&map[i][j]);
		memset(ret,0,sizeof(ret));
		basin = 'a';
		for (i=0;i<h;i++)
			for (j=0;j<w;j++)
				if (!ret[i][j])
					dfs(i,j);
		printf("Case #%d:\n",t);
		for (i=0;i<h;i++){
			for (j=0;j<w;j++)
				printf("%c ",ret[i][j]);
			printf("\n");
		}
	}

	return 0;
}