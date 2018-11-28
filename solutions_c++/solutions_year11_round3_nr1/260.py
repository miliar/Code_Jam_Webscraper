#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
using namespace std;

char ans[55][55], map[55][55];
bool f[55][55];
int n, m;

bool game1(int i1, int j1){
	if ((i1 == n - 1) || (j1 == m - 1)){
		return false;
	}
	if ((f[i1][j1]) || (f[i1][j1 + 1]) || (f[i1 + 1][j1]) || (f[i1 + 1][j1 + 1])){
		return false;
	}
	if ((map[i1][j1] == '.') || (map[i1][j1 + 1] == '.') || (map[i1 + 1][j1] == '.') || (map[i1 + 1][j1 + 1] == '.')){
		return false;
	}
	f[i1][j1] = true;f[i1][j1 + 1] = true;f[i1 + 1][j1] = true;f[i1 + 1][j1 + 1] = true;
	ans[i1][j1] = '/';ans[i1][j1 + 1] = '\\';ans[i1 + 1][j1] = '\\';ans[i1 + 1][j1 + 1] = '/';
	return true;
}

void game(){
	int i, j;
	for (i = 0;i < n;i++){
		for (j = 0;j < m;j++){
			ans[i][j] = '.';
			f[i][j] = false;
		}
	}
	for (i = 0;i < n;i++){
		for (j = 0;j < m;j++){
			if ((map[i][j] == '#') && (!f[i][j])){
				if (!game1(i, j)){
					printf("Impossible");
					return ;
				}
			}
		}
	}
	for (i = 0;i < n;i++){
		if (i)
			printf("\n");
		for (j = 0;j < m;j++){
			printf("%c",ans[i][j]);
		}
	}
}

int main(){
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
	int test, t, i, j;
	scanf("%d\n",&test);
	for (t = 0;t < test;t++){
		if (t)
			printf("\n");
		printf("Case #%d:\n",t + 1);
		scanf("%d %d\n",&n,&m);
		for (i = 0;i < n;i++){
			for (j = 0;j < m;j++){
				scanf("%c",&map[i][j]);
			}
			scanf("\n");
		}
		game();
	}
	return 0;
}