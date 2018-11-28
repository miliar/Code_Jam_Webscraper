#include <cstdio>
#include <cstdlib>
#include <cstring>

int cost[2][40][40];
int curr;

int moves[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

int intersections[20][20][3];

int nRows, nCols;

int dist(int sx, int sy, int dx, int dy, int time) {
  if (time == -1) {
    fprintf(stderr, "time == -1\n");
    exit(-1);
  }
  if (sx == dx) {
    if (sy > dy) {
      if (sy % 2 == 0)
        return 2;
    } else {
      if (sy % 2 == 1)
        return 2;
    }
  } else {
    if (sx > dx) {
      if (sx % 2 == 0)
        return 2;
    } else {
      if (sx % 2 == 1)
        return 2;
    }
  }
  int intx = sx / 2;
  int inty = sy / 2;
  int s = intersections[intx][inty][0];
  int w = intersections[intx][inty][1];
  int t = intersections[intx][inty][2];
  time = time % (s + w);
  if (time < t)
    t -= (s + w);
  int cycle_time = time - t;
  if (sx == dx) {
    // same row - going east west
    if (cycle_time < s)
      return 1 + s - cycle_time;
    else
      return 1;
  } else {
    // same col - going north south
    if (cycle_time < s)
      return 1;
    else
      return 1 + w - (cycle_time - s);
  }
  fprintf(stderr, "Never here!\n");
  exit(-1);
  return -1;
}

int main(void) {
  int nC, cC;

  scanf("%d", &nC);
  for (cC = 0; cC < nC; cC++) {
    scanf("%d%d", &nRows, &nCols);
    for (int i = 0; i < nRows; i++) {
      for (int j = 0; j < nCols; j++) {
        scanf("%d%d%d", &intersections[i][j][0], &intersections[i][j][1], &intersections[i][j][2]);
        intersections[i][j][2] = intersections[i][j][2] % (intersections[i][j][0] + intersections[i][j][1]);
      }
    }
    memset(cost, -1, sizeof(cost));
    cost[0][nRows * 2 - 1][0] = 0;
    //int limit = (nRows * 2 - 1) * nCols * 2 + (nCols * 2 - 1) * nRows * 2;
    int limit = (nRows * 2 - 1) * (nCols * 2 - 1);
    int changed = 0;
    int oth = 0;
    curr = 1;
    while (1) {
      for (int i = 0; i < nRows * 2; i++) {
        for (int j = 0; j < nCols * 2; j++) {
          cost[curr][i][j] = cost[oth][i][j];
          for (int k = 0; k < 4; k++) {
            int si = i + moves[k][0];
            int sj = j + moves[k][1];
            if (si < 0 || si >= nRows * 2 || sj < 0 || sj >= nCols * 2)
              continue;
            if (cost[oth][si][sj] == -1)
              continue;
            int time_needed = dist(si, sj, i, j, cost[oth][si][sj]);
            //printf("dist(%d, %d, %d, %d, %d) = %d\n", si, sj, i, j, cost[oth][si][sj], time_needed);
            if (cost[curr][i][j] == -1 || cost[curr][i][j] > cost[oth][si][sj] + time_needed) {
              cost[curr][i][j] = cost[oth][si][sj] + time_needed;
              changed = -1;
            }
          }
        }
      }
      curr++;
      curr %= 2;
      oth++;
      oth %= 2;
      if (!changed) break;
      changed = 0;
    }
    int ax = 0;
    int ay = nCols * 2 - 1;
    int ans;
    if (cost[curr][ax][ay] == -1 ) ans = cost[oth][ax][ay];
    else ans = (cost[oth][ax][ay] > cost[curr][ax][ay]) ? cost[curr][ax][ay] : cost[oth][ax][ay];
    printf("Case #%d: %d\n", cC + 1, ans);
  }
  return 0;
}
