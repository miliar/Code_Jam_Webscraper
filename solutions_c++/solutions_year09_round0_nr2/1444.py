#include <algorithm>
#include <cstdio>
#include <vector>

#define infinity 1000000

int T,H,W;
int h[100][100], x[100][100], y[100][100];
char result[100][100];

void mark(int i, int j, char sym) {
  h[i][j] = infinity;
  result[i][j] = sym;
  if (i > 0 && x[i - 1][j] == i && y[i - 1][j] == j && h[i - 1][j] != infinity) {
    mark(i - 1, j, sym);
  }
  if (i < H - 1 && x[i + 1][j] == i && y[i + 1][j] == j && h[i + 1][j] != infinity) {
    mark(i + 1, j, sym);
  }
  if (j > 0 && x[i][j - 1] == i && y[i][j - 1] == j && h[i][j - 1] != infinity) {
    mark(i, j - 1, sym);
  }
  if (j < W - 1 && x[i][j + 1] == i && y[i][j + 1] == j && h[i][j + 1] != infinity) {
    mark(i, j + 1, sym);
  }
  if (x[i][j] == -1) {
    return;
  }
  mark(x[i][j], y[i][j], sym);
}

int main() {
  scanf("%d", &T);
  for(int i = 0; i < T; ++i) {
    scanf("%d %d", &H, &W);
    for(int j = 0; j < H; ++j) {
      for(int k = 0; k < W; ++k) {
        scanf("%d", &(h[j][k]));
      }
    }
    for(int j = 0; j < H; ++j) {
      for(int k = 0; k < W; ++k) {
				int m = infinity;
				x[j][k] = -1;
				y[j][k] = -1;
				if (j > 0) {
				  m = std::min(m, h[j - 1][k]);
				}
				if (j < H - 1) {
				  m = std::min(m, h[j + 1][k]);
				}
				if (k > 0) {
				  m = std::min(m, h[j][k - 1]);
				}
				if (k < W - 1) {
				  m = std::min(m, h[j][k + 1]);
				}
				if (m >= h[j][k]) {
				  continue;
				}
				if (j > 0 && h[j - 1][k] == m) {
				  x[j][k] = j - 1;
				  y[j][k] = k;
				  continue;
				}
				if (k > 0 && h[j][k - 1] == m) {
				  x[j][k] = j;
				  y[j][k] = k - 1;
				  continue;
				}
				if (k < W - 1 && h[j][k + 1] == m) {
				  x[j][k] = j;
				  y[j][k] = k + 1;
				  continue;
				}
				if (j < H - 1 && h[j + 1][k] == m) {
				  x[j][k] = j + 1;
				  y[j][k] = k;
				  continue;
				}
      }
    }
    char sym = 'a';
    for(int j = 0; j < H; ++j) {
      for(int k = 0; k < W; ++k) {
        if (h[j][k] != infinity) {
          mark(j, k, sym++);
        }
      }
    }
   	printf("Case #%d:\r\n", i + 1);
    for(int j = 0; j < H; ++j) {
      for(int k = 0; k < W; ++k) {
        printf("%c ", result[j][k]);
      }
      printf("\r\n");
    }
  }
  return 0;
}