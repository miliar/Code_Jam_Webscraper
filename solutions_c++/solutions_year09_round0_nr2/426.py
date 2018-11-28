#include <stdio.h>

int a[110][110];
char b[110][110];

bool isSink(int i, int j) {
  int tmp = a[i][j];
  if (a[i-1][j] < tmp ||
      a[i+1][j] < tmp ||
      a[i][j-1] < tmp ||
      a[i][j+1] < tmp) {
    return false;
  }
  return true;
}

char getDirection(int i, int j) {
  int min = 20000;
  char direction;
  if (a[i-1][j] < min) {
    min = a[i-1][j];
    direction = 'N';
  }
  if (a[i][j-1] < min) {
    min = a[i][j-1];
    direction = 'W';
  }
  if (a[i][j+1] < min) {
    min = a[i][j+1];
    direction = 'E';
  }
  if (a[i+1][j] < min) {
    min = a[i+1][j];
    direction = 'S';
  }
  if (min < a[i][j]) return direction;
  return 'X';
}

void setnode(int i, int j, char g, int height, int width) {
  if (i <= 0 || i > height) return;
  if (j <= 0 || j > width) return;
  b[i][j] = g;
  if (i > 1 && getDirection(i-1, j) == 'S') {
    setnode(i-1, j, g, height, width);
  }
  if (i < height && getDirection(i+1, j) == 'N') {
    setnode(i+1, j, g, height, width);
  }
  if (j > 1 && getDirection(i, j-1) == 'E') {
    setnode(i, j-1, g, height, width);
  }
  if (j < width && getDirection(i, j+1) == 'W') {
    setnode(i, j+1, g, height, width);
  }
}

int main()
{
  FILE *in = fopen("in.txt", "r");
  FILE *out = fopen("out.txt", "w");
  int T, H, W;
  int i, j, k;
  fscanf(in, "%d", &T);
  for (i = 0 ; i < T; i++) {
    fscanf(in, "%d %d", &H, &W);
    for (j = 0; j < 110; j++) {
      for (k = 0; k < 110; k++) {
        a[j][k] = 20000;
        b[j][k] = 'a';
      }
    }
    for (j = 1; j <= H; j++) {
      for (k = 1; k <= W; k++) {
        int n;
        fscanf(in, "%d", &n);
        a[j][k] = n;
      }
    }
    char groupid = 'A';
    for (j = 1; j <= H; j++) {
      for (k = 1; k <= W; k++) {
        if (isSink(j, k)) {
          setnode(j, k, groupid, H, W);
          groupid++;
        }
      }
    }

    if (groupid > 'Z' + 1) printf("too many groups!\n");
    char map[26];
    for (j = 0; j < 26; j++) map[j] = '0';
    char c = 'a';
    for (j = 1; j <= H; j++) {
      for (k = 1; k <= W; k++) {
        if (b[j][k] < 'A' || b[j][k] > 'Z') {
          printf("invalid value at %d,%d\n", j, k);
        }
        int g = b[j][k] - 'A';
        if (map[g] == '0') {
          b[j][k] = c;
          map[g] = c;
          c++;
        } else {
          b[j][k] = map[g];
        }
      }
    }
    fprintf(out, "Case #%d:\n", i + 1);
    for (j = 1; j <= H; j++) {
      for (k = 1; k <= W; k++) {
        fprintf(out, "%c", b[j][k]);
        if (k == W) {
          fprintf(out, "\n");
        } else {
          fprintf(out, " ");
        }
      }
    }
  }
  fclose(in);
  fclose(out);
  return 0;
}
