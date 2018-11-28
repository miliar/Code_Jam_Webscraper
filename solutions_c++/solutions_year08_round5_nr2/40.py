#include<string.h>
#include<stdio.h>
#include<stdlib.h>

int T;

#define INF 10000000
#define MAXN 17
#define QLENGTH INF

int min(int a, int b){
  return a < b ? a : b;
}

int grid[MAXN][MAXN];

int r, c;
int ex, ey;
int sx, sy;
char visited[MAXN][MAXN][MAXN][MAXN][MAXN][MAXN];
int shortest[MAXN][MAXN][MAXN][MAXN][MAXN][MAXN];
int dx[] = {1, 0,-1, 0};
int dy[] = {0,-1, 0, 1};
int ans;

int q[2][QLENGTH][6];
int startq[2], endq[2];

void addq(int d, int px, int py, int bx, int by, int yx, int yy, int dist) {
  if (shortest[px][py][bx][by][yx][yy] && shortest[px][py][bx][by][yx][yy] <= dist)
    return;
  q[d][endq[d]][0] = px;
  q[d][endq[d]][1] = py;
  q[d][endq[d]][2] = bx;
  q[d][endq[d]][3] = by;
  q[d][endq[d]][4] = yx;
  q[d][endq[d]][5] = yy;
  endq[d]++;
  shortest[px][py][bx][by][yx][yy] = dist;
}

int getd(){
  if (startq[0] == endq[0])
    return 1;
  if (startq[1] == endq[1])
    return 0;
  return (shortest[q[1][startq[1]][0]]
	  [q[1][startq[1]][1]]
	  [q[1][startq[1]][2]]
	  [q[1][startq[1]][3]]
	  [q[1][startq[1]][4]]
	  [q[1][startq[1]][5]] < 
	  shortest[q[0][startq[0]][0]]
	  [q[0][startq[0]][1]]
	  [q[0][startq[0]][2]]
	  [q[0][startq[0]][3]]
	  [q[0][startq[0]][4]]
	  [q[0][startq[0]][5]]);
}

void search(int px, int py, int bx, int by, int yx, int yy, int dist) {
  startq[0] = endq[0] = startq[1] = endq[1] = 0;
  addq(0, px, py, bx, by, yx, yy, dist);
  while(startq[0] < endq[0] || startq[1] < endq[1]){
    int d = getd();
    px = q[d][startq[d]][0];
    py = q[d][startq[d]][1];
    bx = q[d][startq[d]][2];
    by = q[d][startq[d]][3];
    yx = q[d][startq[d]][4];
    yy = q[d][startq[d]][5];
    startq[d]++;
    if (visited[px][py][bx][by][yx][yy])
      continue;
    visited[px][py][bx][by][yx][yy] = 1;
    dist = shortest[px][py][bx][by][yx][yy];
    //printf("%d %d %d %d %d %d %d\n", px, py, bx, by, yx, yy, dist);
    if (px == ex && py == ey)
      ans = min(ans, dist);
    for(int i = 0; i < 4; i++){
      int j;
      for (j = 0; !grid[px+j*dx[i]][py+j*dy[i]]; j++);
      j--;
      addq(0, px, py, px+j*dx[i], py+j*dy[i], yx, yy, dist);
      addq(0, px, py, bx, by, px+j*dx[i], py+j*dy[i], dist);
    }
    if (bx > 0 && yx > 0){
      if (px == bx && py == by)
	addq(1, yx, yy, bx, by, yx, yy, dist+1);
      if (px == yx && py == yy)
	addq(1, bx, by, bx, by, yx, yy, dist+1);
    }
    for(int i = 0; i < 4; i++){
      if (!grid[px+dx[i]][py+dy[i]])
	addq(1, px+dx[i], py+dy[i], bx, by, yx, yy, dist+1);
    }
  }
}

int main(){
  int i;
  char ch;
  scanf("%d", &T);
  for(int nc = 0; nc < T; nc++){
    printf("Case #%d: ", nc+1);
    memset(visited, 0, sizeof(shortest));
    memset(shortest, 0, sizeof(shortest));
    memset(grid, 1, sizeof(grid));
    scanf("%d %d\n", &r, &c);
    for(int x = 1; x <= r; x++){
      for(int y = 1; y <= c; y++){
	scanf("%c", &ch);
	if (ch == '.' || ch == 'O' || ch == 'X')
	  grid[x][y] = 0;
	if (ch == 'O'){
	  sx = x; sy = y;
	}
	if (ch == 'X'){
	  ex = x; ey = y;
	}
      }
      scanf("\n");
    }
    ans = INF;
    search(sx, sy, 0, 0, 0, 0, 1);
    if (ans == INF)
      printf("THE CAKE IS A LIE\n");
    else
      printf("%d\n", ans-1);
    fflush(stdout);
  }
}
