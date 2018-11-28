#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
#define INF 1000000
int dx[4] = {-1, 0, 0 ,1},
	dy[4] = {0, -1, 1, 0},
	hei[4];
int a[110][110], pre[110][110];
int H, W, cnt, tot;
struct node {
	int x, y, z;
	bool operator <(const node &aa)const{
		return (z < aa.z); 
	}
} Q[11000];
int col[11000];
bool check(int x, int y, int d){
	int px, py;
	for (int i = 0; i < 4; i++) {
		px = x + dx[i];
		py = y + dy[i];
	
		if (px < 0 || py < 0 || px >= H || py >= W) 
			hei[i] = INF;
		else hei[i] = a[px][py];
	}
	for (int i = 0; i < d; i++)
		if (hei[i] <= hei[d]) return false;
	for (int i = d+1; i < 4; i++)
		if (hei[i] < hei[d]) return false;
	return true;
}
void dfs(int x, int y, int flag){
	pre[x][y] = flag;
	int px, py;
	
	for (int i = 3; i >= 0; i--) {
		px = x + dx[i];
		py = y + dy[i];
		if (px < 0 || py < 0 || px >= H || py >= W)  continue;
		
		if (a[px][py] > a[x][y])
		if (pre[px][py] == -1)
		if (check(px, py, 3- i)){
			dfs(px, py, flag);
		} 
	}
}
void solve(){
	int i, j, k;
	tot = 0;
	for (i = 0; i < H; i++)
	for (j = 0; j < W; j++){ 
		scanf("%d", &a[i][j]);
		pre[i][j] = -1;
		Q[tot].x = i;
		Q[tot].y = j;
		Q[tot].z = a[i][j];
		tot ++;
	}
	sort(Q, Q+tot);
	cnt = 0;
	for (k = 0; k < tot; k++){
		i = Q[k].x;
		j = Q[k].y;
		if (pre[i][j] == -1) {
			dfs(i, j, cnt);
			col[cnt] = -1;
			cnt ++;
		}
	}
//	printf("\n");
	int COL = 0;
	for (i = 0; i < H; i++)
	for (j = 0; j < W; j++)
	if (col[pre[i][j]] == -1) {
		col[pre[i][j]] = COL;
		COL ++;
	}
	
	for (i = 0; i < H; i++){
		printf("%c", col[pre[i][0]] + 'a');
		for (j = 1; j < W; j++)
			printf(" %c", col[pre[i][j]] + 'a');
		printf("\n");
	}
}
int main(){
	//freopen("B-large.in", "r", stdin);
//	freopen("B-large.out", "w", stdout);
	int Case;
	scanf("%d", &Case);
	for (int ca = 1; ca <= Case; ca++) {
		printf("Case #%d:\n", ca);
		scanf("%d %d", &H, &W);
		solve();
	}
	//while (1);
	return 0;
}
