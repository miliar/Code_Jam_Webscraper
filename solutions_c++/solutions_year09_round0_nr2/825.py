#include<stdio.h>
#include<string.h>

const int MAXN = 105;

int des[4][2] = {{-1,0},{0,-1},{0,1},{1,0}};
int h, w, k, f, c;
int mat[MAXN][MAXN];
int basin[MAXN][MAXN];

void dfs(int x, int y)
{
	int p, q, i, tx, ty,Min=100000000;
	tx = -1;
	for(i=0; i<4; i++){
		p = x+des[i][0];
		q = y+des[i][1];
		if(p<0 || q<0 || p>=h || q>=w) continue;
		if(mat[p][q]>=mat[x][y]) continue;
		if(mat[p][q]<Min)  tx=p, ty=q, Min = mat[p][q];
	}
	if(tx==-1){
		basin[x][y] = k;
		return;
	}
	if(basin[tx][ty]!=-1){
		f = 1;
		c = basin[x][y] = basin[tx][ty];
		return;
	}
	dfs(tx, ty);
	if(f==1) basin[x][y] = c;
	else basin[x][y] = k;
	return;
}

void solve(void)
{
	int i, j;
	scanf("%d %d", &h, &w);
	for(i=0; i<h; i++)
		for(j=0; j<w; j++)
			scanf("%d", &mat[i][j]);
	memset(basin, -1, sizeof(basin));
	
	k = 0;
	for(i=0; i<h; i++)
		for(j=0; j<w; j++)
			if(basin[i][j]==-1){
				f = 0;
				dfs(i, j);
				if(f==0) k++;
			}
	
	for(i=0; i<h; i++){
		printf("%c", basin[i][0]+'a');
		for(j=1; j<w; j++)
			printf(" %c", basin[i][j]+'a');
		puts("");
	}
	return;	
}

int main()
{
	int t, ti;
	
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	
	scanf("%d\n", &t);
	for(ti=1; ti<=t; ti++){
		printf("Case #%d:\n", ti);
		solve();
	}
	return 0;
}


