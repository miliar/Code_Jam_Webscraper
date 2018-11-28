#include <fstream>
#include <iostream>
#include <stdio.h>
#include <math.h>

using namespace std;

int t, r, c;
char a[100][100];

struct pereche {
  int x, y;

  pereche(int xx, int yy) {
    x = xx;
    y = yy;
  }
};

struct pereche* pivot(struct pereche *prev) {
  for (int i = prev->y; i < c; i++) {
    if (a[prev->x][i] == '#') {
      return new pereche(prev->x, i);
    }    
  }
  for (int i = prev->x + 1; i < r; i++) {
    for (int j = 0; j < c; j++) {
      if (a[i][j] == '#') {
        return new pereche(i, j);
      }
    }
  }
  return NULL;
}

bool solve() {
  pereche *prev = new pereche(0, 0);
  bool possible = true;

  while (possible) {
    pereche* piv = pivot(prev);

    if (piv == NULL) return true;

    if ((piv->x == r - 1) || (piv->y == c - 1)) {
      possible = false;
      break;
    }

    if ((a[piv->x + 1][piv->y] != '#') || (a[piv->x][piv->y + 1] != '#') ||
        (a[piv->x + 1][piv->y + 1] != '#')) {
      possible = false;
      break;
    }
    a[piv->x][piv->y] = 33;
    a[piv->x][piv->y + 1] = 34;
    a[piv->x+1][piv->y] = 34;
    a[piv->x+1][piv->y+1] = 33;
    prev = new pereche(piv->x, piv->y);
  }
  return possible;
}

int main() {
  ifstream f("a.in");  
  ofstream g("aa.out");
  
  f >> t;

  for (int i = 0; i < t; i++) {
    f >> r >> c;

    for (int j = 0; j < r; j++) {
      for (int k = 0; k < c; k++) {

        f >> a[j][k];
  
      }
    
    }

    bool possible = solve();

    if (!possible) {
      g << "Case #" << i + 1 << ":\nImpossible\n";
    } else {
      g << "Case #" << i + 1 << ":\n";
      for (int j = 0; j < r; j ++) {
        for (int k = 0; k < c; k++) {
          if (a[j][k] == 33) g << "/"; else
          if (a[j][k] == 34) g << "\\"; else
              g << a[j][k];
        }
        g << "\n";
      }
    }
  }
  f.close();
  g.close();
  return 0;
}

