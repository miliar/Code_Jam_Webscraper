#include<cstdio>
#include<cstring>

int p[100*100],mat[100][100];
char hash[100*100];
int Find_Set(int x)
{
	if(p[x] != x) p[x] = Find_Set(p[x]);
	return p[x];
}

void Union(int x,int y)
{
	int px = Find_Set(x);
	int py = Find_Set(y);
	p[px] = py;
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("ans3.txt","w",stdout);
	int n,m,Case,kk,d[4][2] = {{-1,0},{0,-1},{0,1},{1,0}};
	scanf("%d",&Case);
	for(kk = 1; kk <= Case; kk++){
		int i,j,k;
		scanf("%d%d",&n,&m);
		for(i = 0; i < n; i++)
			for(j = 0; j < m; j++){
				scanf("%d",&mat[i][j]);
				p[i * m + j] = i * m + j;
				hash[i * m + j] = 0;
			}
		for(i = 0; i < n; i++)
			for(j = 0; j < m; j++){
				int mmin = mat[i][j],mk;
				for(k = 0; k < 4; k++){
					int ni = d[k][0] + i, nj = d[k][1] + j;
					if(ni >= 0 && ni < n && nj >= 0 && nj < m && mat[ni][nj] < mmin){
						mmin = mat[ni][nj];
						mk = k;
					}
				}
				if(mat[i][j] != mmin)
					Union(i * m + j, (i + d[mk][0]) * m + j + d[mk][1]);
			}
		int len = 0;
				
		printf("Case #%d:\n",kk);
		for(i = 0; i < n; i++){
			for(j = 0; j < m; j++){
				int pp = Find_Set(i * m + j);
				if(hash[pp] == 0){
					hash[pp] = 'a' + len;
					++len;
				}
				if(j != 0)
					printf(" ");
				printf("%c",hash[pp]);
				
			}
			printf("\n");
		}
	}	
	return 0;
}