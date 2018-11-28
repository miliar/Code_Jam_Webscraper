#include <cstdio>
#include <algorithm>

using namespace std;

const int maxn = 100;

int T,R,C;
char grd[maxn][maxn];
char tmp[maxn][maxn];

bool check() {
	for(int i = 0; i < R; i++) {
		for(int j = 0; j < C; j++) {
			tmp[i][j] = grd[i][j];
		}
	}
	for(int i = 0; i < R; i++) {
		for(int j = 0; j < C; j++) {
			if (tmp[i][j] == '#') {
				if(!((i + 1 < R && j + 1 < C) && tmp[i + 1][j] == '#' 
					&& tmp[i][j + 1] == '#' && tmp[i + 1][j + 1] =='#'))
					return false;
				else {
					tmp[i][j] =  tmp[i + 1][j + 1] ='/';
					tmp[i + 1][j] = tmp[i][j + 1] ='\\';
				}
			}
		}
	}
	return true;
}
int main() {
	int nCase = 0;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&T);
	while(T--) {
		scanf("%d%d",&R,&C);
		for(int i = 0; i < R; i++) {
			scanf("%s",grd[i]);
		}
		printf("Case #%d:\n", ++nCase);
		if (!check()) {
			printf("Impossible\n");
		} else {
			for(int i = 0; i < R; i++) {
				for(int j = 0; j < C; j++) {
					printf("%c",tmp[i][j]);
				}
				printf("\n");
			}
		}
	}
	return 0;
}