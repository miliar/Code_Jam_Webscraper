#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
using namespace std;

void printGrid(char g[64][64], int n) {
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < n; ++j) {
      printf("%c", g[i][j]);
    }
    printf("\n");
  }
}

int main() {
  int cases;
  scanf("%d\n", &cases);
  for (int case_i = 1; case_i <= cases; ++case_i) {
    char grid[64][64], gridr[64][64];
    int n, k;
    scanf("%d%d\n", &n, &k);
    for (int row = 0; row < n; ++row) {
      for (int col = 0; col < n; ++col) {
        scanf("%c", &grid[col][n - row - 1]);
      }
      scanf("\n");
    }
    for (int col = 0; col < n; ++col) {
      int x = n - 1;
      for (int row = n - 1; row >= 0; --row) {
        if (grid[row][col] != '.') {
          grid[x][col] = grid[row][col];
          --x;
        }
      }
      for (int row = x; row >= 0; --row)
        grid[row][col] = '.';
    }
    //printf("%d %d\n", n, k);
    //printGrid(grid, n);
    int sr = 0, sb = 0;
    for (int row = 0; row < n; ++row) {
      int r = 0, b = 0;
      if (grid[row][0] == 'B') b = 1;
      if (grid[row][0] == 'R') r = 1;
      //printf("init b r, row %d: %d %d\n", row, b, r);
      sr = max(r, sr);
      sb = max(b, sb);
      for (int i = 1; i < n; ++i) {
        switch (grid[row][i]) {
          case 'R': ++r; b = 0; break;
          case 'B': ++b; r = 0; break;
          default: r = 0; b = 0;
        }
        sr = max(r, sr);
        sb = max(b, sb);
        //printf("next b r, row %d/col %d: %d %d\n", row, i, b, r);
      }
    }

    for (int col = 0; col < n; ++col) {
      int r = 0, b = 0;
      if (grid[0][col] == 'B') b = 1;
      if (grid[0][col] == 'R') r = 1;
      //printf("init b r, row %d: %d %d\n", row, b, r);
      sr = max(r, sr);
      sb = max(b, sb);
      for (int i = 1; i < n; ++i) {
        switch (grid[i][col]) {
          case 'R': ++r; b = 0; break;
          case 'B': ++b; r = 0; break;
          default: r = 0; b = 0;
        }
        sr = max(r, sr);
        sb = max(b, sb);
        //printf("next b r, row %d/col %d: %d %d\n", row, i, b, r);
      }
    }

    for (int col = 0; col < n; ++col) {
      int r = 0, b = 0;
      if (grid[0][col] == 'B') b = 1;
      if (grid[0][col] == 'R') r = 1;
      //printf("init b r, row %d: %d %d\n", row, b, r);
      sr = max(r, sr);
      sb = max(b, sb);
      for (int i = 1; (col + i) < n; ++i) {
        switch (grid[i][col + i]) {
          case 'R': ++r; b = 0; break;
          case 'B': ++b; r = 0; break;
          default: r = 0; b = 0;
        }
        sr = max(r, sr);
        sb = max(b, sb);
        //printf("next b r, row %d/col %d: %d %d\n", row, i, b, r);
      }
    }

    for (int row = 0; row < n; ++row) {
      int r = 0, b = 0;
      if (grid[row][0] == 'B') b = 1;
      if (grid[row][0] == 'R') r = 1;
      //printf("init b r, row %d: %d %d\n", row, b, r);
      sr = max(r, sr);
      sb = max(b, sb);
      for (int i = 1; (row + i) < n; ++i) {
        switch (grid[row + i][i]) {
          case 'R': ++r; b = 0; break;
          case 'B': ++b; r = 0; break;
          default: r = 0; b = 0;
        }
        sr = max(r, sr);
        sb = max(b, sb);
        //printf("next b r, row %d/col %d: %d %d\n", row, i, b, r);
      }
    }

    for (int col = 0; col < n; ++col) {
      int r = 0, b = 0;
      if (grid[0][col] == 'B') b = 1;
      if (grid[0][col] == 'R') r = 1;
      //printf("init b r, row %d: %d %d\n", row, b, r);
      sr = max(r, sr);
      sb = max(b, sb);
      for (int i = 1; (col - i) >= 0; ++i) {
        switch (grid[i][col - i]) {
          case 'R': ++r; b = 0; break;
          case 'B': ++b; r = 0; break;
          default: r = 0; b = 0;
        }
        sr = max(r, sr);
        sb = max(b, sb);
        //printf("next b r, row %d/col %d: %d %d\n", row, i, b, r);
      }
    }

    for (int row = 0; row < n; ++row) {
      int r = 0, b = 0;
      if (grid[row][0] == 'B') b = 1;
      if (grid[row][0] == 'R') r = 1;
      //printf("init b r, row %d: %d %d\n", row, b, r);
      sr = max(r, sr);
      sb = max(b, sb);
      for (int i = 1; (row - i) >= 0; ++i) {
        switch (grid[row - i][i]) {
          case 'R': ++r; b = 0; break;
          case 'B': ++b; r = 0; break;
          default: r = 0; b = 0;
        }
        sr = max(r, sr);
        sb = max(b, sb);
        //printf("next b r, row %d/col %d: %d %d\n", row, i, b, r);
      }
    }

    string answer;
    if (sb >= k and sr >= k) {
      answer = "Both";
    } else if (sb >= k) {
      answer = "Blue";
    } else if (sr >= k) {
      answer = "Red";
    } else {
      answer = "Neither";
    }
    printf("Case #%d: %s\n", case_i, answer.c_str());
  }
  return 0;
}
