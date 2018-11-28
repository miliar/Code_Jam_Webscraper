#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

#define MAXN 1010

struct R{
	int x1, y1, x2, y2;
}rec[MAXN];

int n;

bool g[MAXN][MAXN];
int vs[MAXN];

inline int ABS(int x){
	if (x < 0)return -x;
	return x;
}

void dfs(int x, int tag){
	vs[x] = tag;
	for (int i = 1; i <= n; i++){
		if (vs[i] == 0 && g[x][i]){
			dfs(i, tag);
		}
	}
}

int main(){
	freopen("/home/liang/桌面/C-small-attempt1.in", "r", stdin);
	freopen("ans1.out", "w", stdout);
	int cas = 1;
	int x1, y1, x2, y2;
	int i, j, k;
	int mx, my;
	int T;


	scanf("%d", &T);
	while (T--){
		memset(g, false, sizeof(g));
		scanf("%d", &n);
		for (i = 1; i <= n; i++){
			scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
			rec[i].x1 = min(x1, x2);
			rec[i].x2 = max(x1, x2);
			rec[i].y1 = min(y1, y2);
			rec[i].y2 = max(y1, y2);
		}
		for (k = 1; k <= n; k++){
			for (i = rec[k].x1; i <= rec[k].x2; i++){
				for (j = rec[k].y1; j <= rec[k].y2; j++){
					g[i][j] = true;
				}
			}
		}

		int ans = 0;
		while (1){
			for (i = 1; i <= 100; i++){
				for (j = 1; j <= 100; j++){
					if (g[i][j])break;
				}
				if (j <= 100)break;
			}
			if (i > 100)break;


			ans++;
			for (i = 100; i >= 1; i--){
				for (j = 100; j >= 1; j--){
					if (i != 1 && j != 1 && g[i - 1][j] && g[i][j - 1]){
						g[i][j] = true;
					}
				}
			}

			for (i = 100; i >= 1; i--){
				for (j = 100; j >= 1; j--){
					if ((i == 1 || !g[i - 1][j]) && (j == 1 || !g[i][j - 1])){
						g[i][j] = false;
					}
				}
			}
		}
		printf("Case #%d: %d\n", cas++, ans);
	}
	return 0;

}
/*











	scanf("%d", &T);
	while (T--){
		scanf("%d", &n);
		for (i = 1; i <= n; i++){
			scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
			rec[i].x1 = min(x1, x2);
			rec[i].x2 = max(x1, x2);
			rec[i].y1 = min(y1, y2);
			rec[i].y2 = max(y1, y2);
		}
		memset(g, false, sizeof(g));
		for (i = 1; i <= n; i++){
			for (j = i + 1; j <= n; j++){
				if (rec[j].x1 <= rec[i].x2 + 1 && rec[j].x2 >= rec[i].x1 - 1 && rec[j].y1 <= rec[i].y2 + 1 && rec[j].y2 >= rec[i].y1 - 1)
				{
					g[i][j] = g[j][i] = true;
				}
			}
		}
		int ans = 0;
		memset(vs, 0, sizeof(vs));
		for (i = 1; i <= n; i++){
			if (vs[i] == 0){
				dfs(i, i);

				mx = rec[i].x2;
				my = rec[i].y2;

				for (j = 1; j <= n; j++){
					if (vs[j] == i){
						mx = max(mx, rec[j].x2);
						my = max(my, rec[j].y2);
					}
				}
				for (j = 1; j <= n; j++){
					ans = max(ans, ABS(mx - rec[j].x1) + ABS(my - rec[j].y1) + 1);
				}
			}
		}
		printf("Case #%d: %d\n", cas++, ans);
	}
	return 0;
}



*/
