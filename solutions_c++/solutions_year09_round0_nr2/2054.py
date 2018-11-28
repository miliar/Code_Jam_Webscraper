#include <cstdio>

int T;
int W, H;
int map[102][102];
int dir[102][102];
int sinkx[102][102];
int sinky[102][102];
int sinkid[102][102];

int dx[] = { 0, -1, 1, 0 };
int dy[] = { -1, 0, 0, 1 };

int nsinkid;

void getsink(int y, int x) {
  if (sinkx[y][x] != -1)
    return;
  if(dir[y][x] == -1) {
    sinkx[y][x] = x;
    sinky[y][x] = y;
    sinkid[y][x] = nsinkid;
    nsinkid++;
    return;
  }
  int ny = y + dy[dir[y][x]], nx = x + dx[dir[y][x]];
  getsink(ny, nx);
  sinkx[y][x] = sinkx[ny][nx];
  sinky[y][x] = sinky[ny][nx];
}

int main() {
  int x, y, i;
  scanf("%d", &T);
  for(int Q = 0; Q < T; Q++) {
    printf("Case #%d:\n", Q+1);
    for(y = 0; y < 102; y++)
      for(x = 0; x < 102; x++)
        map[y][x] = 20000, sinkx[y][x] = -1, sinky[y][x] = -1;
    nsinkid = 'a';
    scanf("%d %d", &H, &W);
    for(y = 1; y <= H; y++)
      for(x = 1; x <= W; x++)
        scanf("%d", &map[y][x]);
    for(y = 1; y <= H; y++) {
      for(x = 1; x <= W; x++) {
        if(map[y][x] <= map[y-1][x] && map[y][x] <= map[y+1][x] &&
            map[y][x] <= map[y][x-1] && map[y][x] <= map[y][x+1])
          dir[y][x] = -1;
        else {
          int min = 20000;
          for(i = 0; i < 4; i++) {
            if (map[y+dy[i]][x+dx[i]] < min) {
              dir[y][x] = i;
              min = map[y+dy[i]][x+dx[i]];
            }
          }
        }
      }
    }
    for(y = 1; y <= H; y++) {
      for(x = 1; x <= W; x++) {
        getsink(y, x);
        printf("%c%c", sinkid[sinky[y][x]][sinkx[y][x]], x == W ? '\n' : ' ');
      }
    }
  }
  return 0;
}

