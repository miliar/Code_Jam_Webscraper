#include<stdio.h>
#include<assert.h>
#include<string.h>

#define INF 1000000000
#define MAX 105

int R,C;
int mat[MAX][MAX];
char map[MAX][MAX];
char out[MAX][MAX];

int col;

int _r[] = {-1,0,0,1};
int _c[] = {0,-1,1,0};

char dfs(int r,int c){

	if(map[r][c] != -1)
		return map[r][c];

	int r1,c1,i,b,br,bc;

	b = INF;

	for(i=0;i<4;i++){
		r1 = r + _r[i];
		c1 = c + _c[i];
		if(!(0<=r1&&r1<R&&0<=c1&&c1<C))
			continue;
		if(mat[r1][c1] < b){
			b = mat[r1][c1];
			br= r1;
			bc= c1;
		}
	}

	if(b < mat[r][c])
		return (map[r][c] = dfs(br,bc));
	else{
		col++;
		return (map[r][c] = col);
	}
}

void dfs2(int r,int c){
	int r1,c1,i;
	out[r][c] = col;

	for(i=0;i<4;i++){
		r1 = r + _r[i];
		c1 = c + _c[i];
		if(!(0<=r1&&r1<R&&0<=c1&&c1<C))
			continue;
		if(map[r1][c1] == map[r][c] && out[r1][c1]==-1)
			dfs2(r1,c1);
	}
}


int main(){

	int N,T,r,c;

	scanf("%d",&T);

	for(N=1;N<=T;N++){
		scanf("%d%d",&R,&C);
		for(r=0;r<R;r++)for(c=0;c<C;c++)
			scanf("%d",&mat[r][c]);

		memset(map,-1,sizeof(map));
		col = -1;
		for(r=0;r<R;r++)for(c=0;c<C;c++){
			if(map[r][c]==-1)
				dfs(r,c);
		}
		assert(col <= 26);

		memset(out,-1,sizeof(out));
		col = 'a'-1;
		for(r=0;r<R;r++)for(c=0;c<C;c++){
			if(out[r][c]==-1){
				col++;
				dfs2(r,c);
			}
		}
		assert(col <= 'z');

		printf("Case #%d:\n",N);
		for(r=0;r<R;r++){
			for(c=0;c<C;c++){
				if(c)printf(" ");
				printf("%c",out[r][c]);
			}
			printf("\n");
		}


	}

	return 0;
}