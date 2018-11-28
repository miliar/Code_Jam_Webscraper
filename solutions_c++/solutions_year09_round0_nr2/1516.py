#include <stdio.h>

const int dirs[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
int H, W;
int map[128][128];
char basin[128][128];

char floodfill(int h, int w, char tag) {
  if (basin[h][w] != '.') return basin[h][w];

  int best_d = -1;
  int lowest_altitude = map[h][w];

  for (int d = 0; d < 4; d++) {
    int h2 = h + dirs[d][0];
    int w2 = w + dirs[d][1];
    if (h2 < 0 || h2 >= H || w2 < 0 || w2 >= W) continue;
    if (map[h2][w2] < lowest_altitude) {
      best_d = d;
      lowest_altitude = map[h2][w2];
    }
  }

  if (best_d != -1) {
    int h2 = h + dirs[best_d][0];
    int w2 = w + dirs[best_d][1];
    basin[h][w] = floodfill(h2, w2, tag);
  }

  if (tag != '?') basin[h][w] = tag;    
  
  return basin[h][w];
}

void test() {
  scanf("%d %d", &H, &W);
  for (int h = 0; h < H; h++) {
    for (int w = 0; w < W; w++) {
      scanf("%d", &map[h][w]);
      basin[h][w] = '.';
    }
  }

  char next = 'a';
  for (int h = 0; h < H; h++) {
    for (int w = 0; w < W; w++) {
      if (basin[h][w] == '.') {
	if (floodfill(h, w, '?') == '.')
	  floodfill(h, w, next++);
      }
    }
  }

  for (int h = 0; h < H; h++) {
    for (int w = 0; w < W; w++) {
      printf("%s%c", w ? " " : "", basin[h][w]);
    }
    printf("\n");
  }
}

int main(void) {
  int T;
  scanf("%d", &T);
  for (int t = 0; t < T; t++) {
    printf("Case #%d:\n", t + 1);
    test();
  }
  return 0;
}
