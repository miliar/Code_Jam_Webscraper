#include <cstdio>
#include <iostream>
#include <map>
#include <set>
#include <vector>
using namespace std;

typedef vector<int> vi;

void ln() {
  putchar('\n');
}

const int N = 100;

const int d[][2] = {
  { -1, 0 }, { 0, -1 }, { 0, 1 }, { 1, 0 }
};
const int d_sz = sizeof(d) / sizeof(d[0]);

/*
bool falldown(int row, int col, int rows, int cols, int g[][N]) {
  for (int i = 0; i < d_sz; i++) {
    int r = row + d[i][0];
    int c = col + d[i][1];
    if (0 <= r && r < rows && 0 <= c && c < cols) {
      if (g[row][col] > g[r][c])
        return true;
    }
  }
  return false;
}*/

struct Flow {
  int r;
  int c;
  int altitude;
  Flow(int r, int c, int altitude) : r(r), c(c), altitude(altitude) {}
};

int calc_1(int id, int row, int col, int rows, int cols, int g[][N], int used[][N], int tab[][N]) {
  int nr;
  int nc;
  int a = INT_MAX;

  for (int i = 0; i < d_sz; i++) {
    int r = row + d[i][0];
    int c = col + d[i][1];
    if (0 <= r && r < rows && 0 <= c && c < cols) {
      if (g[r][c] < g[row][col] && g[r][c] < a) {
        nr = r;
        nc = c;
        a = g[r][c];
      }
    }
  }

  if (a == INT_MAX)
    return tab[row][col] = id;
  else {
    if (used[nr][nc])
      return tab[row][col] = tab[nr][nc];

    id = calc_1(id, nr, nc, rows, cols, g, used, tab);
    tab[row][col] = id;
    used[nr][nc] = true;
  }
  return id;
}

void display(int rows, int cols, int tab[][N]) {
  puts("--");
  for (int i = 0; i < rows; i++) {
    for (int j = 0; j < cols; j++)
      printf("%d", tab[i][j]);
    ln();
  }

}

void calc(int rows, int cols, int g[][N]) {
  map<int, vi> m;
  set<int> st;
  for (int i = 0; i < rows; i++)
    for (int j = 0; j < cols; j++) {
      st.insert(g[i][j]);
      m[g[i][j]].push_back((i<<8)|j);
    }

  vi v(st.begin(), st.end());

  int used[N][N] = {};
  int tab[N][N] = {};
  int id = 1;
  for (int i = v.size()-1; i >= 0; i--) {
    const vi& w = m[v[i]];
    for (int j = 0; j < (int)w.size(); j++) {
      int r = w[j] >> 8;
      int c = w[j] & ((1<<8)-1);

      if (used[r][c]) continue;
      tab[r][c] = calc_1(id, r, c, rows, cols, g, used, tab);
      ++id;
      // display(rows, cols, tab);
    }
  }

  map<int, int> charmap;
  char c = 'a';
  for (int i = 0; i < rows; i++) {
    for (int j = 0; j < cols; j++) {
      if (j > 0) putchar(' ');

      char x = charmap[tab[i][j]];
      if (x == 0)
        x = charmap[tab[i][j]] = c++;

      printf("%c", x);
    }
    ln();
  }
}

int main() {
  int ncases;
  scanf("%d", &ncases);
  for (int cc = 0; cc < ncases; cc++) {
    int rows, cols;
    scanf("%d %d", &rows, &cols);

    int g[N][N];
    for (int i = 0; i < rows; i++)
      for (int j = 0; j < cols; j++)
        scanf("%d", &g[i][j]);

    printf("Case #%d:\n", cc+1);
    calc(rows, cols, g);
  }
}

