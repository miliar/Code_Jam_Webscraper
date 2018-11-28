#include <iostream>
#include <cstring>
using namespace std;

const int MAXN = 120;
const int INF = (1<<28);
int imp[MAXN][MAXN];
char cmp[MAXN][MAXN], val[MAXN*MAXN];

int p[MAXN*MAXN];

void Make_set(){
	for(int i = 0; i < MAXN*MAXN; ++i)
		p[i] = i;
}
int Find(int x){
	if(x == p[x])return x;
	return p[x] = Find(p[x]);
}
void Union(int x, int y){
	p[x] = y;
}
int R, C;
int dir[][2] = {{-1,0}, {0, -1}, {0, 1}, {1, 0}};
bool valid(int r, int c){
	return r>=1 && r<=R && c>=1 && c<=C;
}
void calc(){
	int i, j, k, u, nr, nc, m;
	for(i = 1; i <= R; ++i)
		for(j = 1; j <= C; ++j){
			u = -1, m = imp[i][j];
			for(k = 0; k < 4; ++k){
				nr = i + dir[k][0];
				nc = j + dir[k][1];
				if(valid(nr, nc)){
					if(imp[nr][nc] < m){
						m = imp[nr][nc];
						u = k;
					}
				}
			}
			if(u != -1){
				nr = i + dir[u][0];
				nc = j + dir[u][1];
				Union(i*C+j, nr*C+nc);
			}
		}
	memset(val, 0, sizeof(val));
	char ch = 'a';
	for(int i = 1; i <= R; ++i)
		for(int j = 1; j <= C; ++j){
			int u = Find(i*C+j);
			if(!val[u]){
				val[u] = ch++;
			}
			cmp[i][j] = val[u];
		}
}

int main()
{
	int T;
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	scanf("%d", &T);
	for(int tt = 1; tt <= T; ++tt){
		scanf("%d %d", &R, &C);
		for(int i = 1; i <= R; ++i)
			for(int j = 1; j <= C; ++j)
				scanf("%d", &imp[i][j]);
		Make_set();
		calc();
		printf("Case #%d:\n", tt);
		for(int i = 1; i <= R; ++i){
			printf("%c", cmp[i][1]);
			for(int j = 2; j <= C; ++j)
				printf(" %c", cmp[i][j]);
			printf("\n");
		}
	}
	return 0;
}


