#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;
#define For(i, x) for (int i=0; i<(int)(x); i++)
#define pr(a) cout << (a)
#define nl putchar('\n')

typedef vector<int> vi;

const int N = 60;

void rotate90(int n, char g[][N]) {
  char a[N][N];
  for (int r = 0; r < n; r++)
    for (int c = 0; c < n; c++) {
      int row = c;
      int col = n - r - 1;
      a[row][col] = g[r][c];
    }

  for (int i = 0; i < n; i++)
    for (int j = 0; j < n; j++)
      g[i][j] = a[i][j];
}

void disp(int n, char g[][N]) {
  For(i, n) {
    For(j, n) putchar(g[i][j]);
    nl;
  }
  nl;
}

void falldown(int n, char g[][N]) {
  For(c, n) {
    vi v;
    For(r, n)
      if (g[r][c] != '.') {
        v.push_back(g[r][c]);
        g[r][c] = '.';
      }

    for (int r = n-1; r >= 0; r--) {
      if (v.empty()) break;
      g[r][c] = v.back();
      v.pop_back();
    }
  }
}

bool joink(char color, int k, int n, char g[][N]) {
  int sum[N][N][4] = {};
  For(r, n) For(c, n) {
    if (g[r][c] != color) continue;
    int d[][2] = { { 0, -1 }, { -1, 0 }, { -1, -1 }, { -1, 1 } };
    For(i, 4) {
      int pr = r + d[i][0];
      int pc = c + d[i][1];
      if (0 <= pr && pr < n && 0 <= pc && pc < n) {
        sum[r][c][i] = 1 + sum[pr][pc][i];
        if (sum[r][c][i] == k)
          return true;
      }
      else
        sum[r][c][i] = 1;
    }
  }
  return false;
}

char* calc(int k, int n, char g[][N]) {
  rotate90(n, g);
  falldown(n, g);

  bool bluewin = joink('B', k, n, g);
  bool redwin  = joink('R', k, n, g);

  if (bluewin && redwin)
    return "Both";
  else if (bluewin)
    return "Blue";
  else if (redwin)
    return "Red";
  else
    return "Neither";
}

int main() {
  int ncases;
  scanf("%d", &ncases);
  For(cc, ncases) {
    int n, k;
    scanf("%d %d", &n, &k);
    char g[N][N];
    For(i, n) scanf("%s", &g[i][0]);

    printf("Case #%d: %s\n", cc+1, calc(k, n, g));
  }
}

