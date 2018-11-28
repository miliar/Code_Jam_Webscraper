#include <stdio.h>
#include <string.h>
#include <assert.h>

int T,R,C,A[101][101],L[101][101];
int dr[] = {-1, 0, 0, 1};
int dc[] = {0, -1, 1, 0};

int flow(int r, int c, int label){
	if (L[r][c]!=-1) return L[r][c];

	int d = -1, da = -1;
	for (int i=0; i<4; i++){
		int nr = r+dr[i], nc = c+dc[i];
		if (nr<0 || nc<0 || nr>=R || nc>=C || A[nr][nc]>=A[r][c]) continue;
		if (d==-1 || da > A[nr][nc]) d = i, da = A[nr][nc];
	}

	if (d==-1) return L[r][c] = label;
	int nr = r+dr[d], nc = c+dc[d];
	return L[r][c] = flow(nr,nc,label);	
}

int main(){
	scanf("%d",&T);
	for (int t=1; t<=T; t++){
		printf("Case #%d:\n",t);
		scanf("%d %d",&R,&C);
		for (int i=0; i<R; i++)
			for (int j=0; j<C; j++)
				scanf("%d",&A[i][j]);

		int label = 'a';
		memset(L,-1,sizeof(L));
		for (int i=0; i<R; i++)
			for (int j=0; j<C; j++)
				if (flow(i,j,label)==label)
					label++;

		for (int i=0; i<R; i++){
			for (int j=0; j+1<C; j++)
				printf("%c ",L[i][j]);
			printf("%c\n",L[i][C-1]);
		}
	}
}
