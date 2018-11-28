/**********************************************************************
Author: littlekid@whu
Created Time:  2009-9-3 13:44:34
File Name: 
Description: 
**********************************************************************/
#include <iostream>
#include <cstring>
#include <queue>
using namespace std;

const int MAXH = 1000;
const int MAXW = 1000;

const int dx[] = {-1, 0, 0, 1};
const int dy[] = {0, -1, 1, 0};

typedef struct t_pos {
	int x, y;
};

int H, W;
int height[MAXH+2][MAXW+2];
int label[MAXH+2][MAXW+2];
bool vis[MAXH+2][MAXW+2];

bool is_sink(int row, int col)
{
	if (row > 1) {
		if (height[row-1][col] < height[row][col])
			return false;
	}
	if (row < H) {
		if (height[row+1][col] < height[row][col])
			return false;
	}
	if (col > 1) {
		if (height[row][col-1] < height[row][col])
			return false;
	}
	if (col < W) {
		if (height[row][col+1] < height[row][col])
			return false;
	}
	return true;
}

void bfs(int r, int c, int tag)
{
	
	memset(vis, false, sizeof(vis));
	queue<t_pos> q;
	t_pos now, nxt, cur;
	now.x = r, now.y = c;
	vis[r][c] = true;
	q.push(now);
	while (!q.empty()) {
		now = q.front();
		q.pop();
		label[now.x][now.y] = tag;
		bool flag = false;
		for (int ix = 0; ix < 4; ++ix) {
			nxt.x = now.x + dx[ix], nxt.y = now.y + dy[ix];
			flag = false;
			if (1 <= nxt.x && nxt.x <= H && 1 <= nxt.y && nxt.y <= W 
					&& height[nxt.x][nxt.y] > height[now.x][now.y] && !vis[nxt.x][nxt.y]) {
				flag = true;
			}
			if (!flag) continue;
			int yes = 1;
			for (int i = 0; i < 4; ++i) {
				cur.x = nxt.x + dx[i], cur.y = nxt.y + dy[i];
				if (cur.x < 1 || cur.x > H || cur.y < 1 || cur.y > W) continue;
				if (now.x == cur.x && now.y == cur.y) {
					yes = 2;
					continue;///
				}
				if (height[ cur.x ][ cur.y ] < height[ now.x ][ now.y ]) {
					flag = false;
					break;
				}
				if (yes == 1 && height[ cur.x ][ cur.y ] == height[ now.x ][ now.y ]) {
					flag = false;
					break;
				}
			}
			if (flag) {
				vis[ nxt.x ][ nxt.y ] = true;
			 	q.push(nxt);	
			}
		}	
	}
}

int main() 
{
	int T;
	freopen("F:\\ACM\\gcj2009\\QR\\b.in", "r", stdin);
	freopen("F:\\ACM\\gcj2009\\QR\\b.out", "w", stdout);
    scanf("%d", &T);
	for (int ca = 1; ca <= T; ++ca) {
		//input map
		scanf("%d %d", &H, &W);
		
		for (int row = 1; row <= H; ++row) {
			for (int col = 1; col <= W; ++col) {
				scanf("%d", &height[row][col]);	
			}
		}
		
		memset(vis, false, sizeof(vis));
		//find sink and labeled the map
		int cnt = 0;
		for (int row = 1; row <= H; ++row) {
			for (int col = 1; col <= W; ++col) {
				if (is_sink(row, col)) {
					++cnt;
//					cout << cnt << ": " << row << "," << col << " == " << height[row][col] << endl;///
					bfs(row, col, cnt);
				}
			}	
		}
		if (cnt > 26) while (1);
		
		//output label
		printf("Case #%d:\n", ca);
		int ch[cnt+2], st = 0;
		memset(ch, 0, sizeof(ch));
		for (int row = 1; row <= H; ++row) {
			for (int col = 1; col <= W; ++col) {
				if (col > 1) printf(" ");
				if (ch[ label[row][col] ] == 0) {
					++st;
					ch[ label[row][col] ] = st;
				}
				printf("%c", 'a' + ch[ label[row][col] ]-1);	
			}	
			printf("\n");
		}
	}
    return 0;
}

