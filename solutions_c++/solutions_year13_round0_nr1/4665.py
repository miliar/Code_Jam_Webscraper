//
#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <queue>
#include <stack>
#include <fstream>
#include <sstream>

using namespace std;

int main() {
  char T[4][5];
  int nT, iT = 1;
  scanf("%d", &nT);
  scanf("\n");
  while (nT--) {
    for (int i = 0; i < 4; i++)
      scanf ("%s\n", T[i]);
    scanf ("\n");
    int cont = 0;
    for (int i = 0; i < 4; i++)
      for (int j = 0; j < 4; j++)
        if (T[i][j] == '.') cont++;
    bool wonX = true, wonO = true;
    for (int i = 0; i < 4; i++) {
      wonX &= (T[i][i] != 'O' && T[i][i] != '.');
      wonO &= (T[i][i] != 'X' && T[i][i] != '.');
    }
    if (wonX || wonO) goto ans;
    wonX = wonO = true;
    for (int i = 0; i < 4; i++) {
      wonX &= (T[i][3 - i] != 'O' && T[i][3 - i] != '.');
      wonO &= (T[i][3 - i] != 'X' && T[i][3 - i] != '.');
    }
    if (wonX || wonO) goto ans;
    for (int i = 0; i < 4; i++) {
      wonX = wonO = true;
      for (int j = 0; j < 4; j++) {
        wonX &= (T[i][j] != 'O' && T[i][j] != '.');
        wonO &= (T[i][j] != 'X' && T[i][j] != '.');
      }
      if (wonX or wonO) goto ans;
    }
    for (int j = 0; j < 4; j++){
      wonX = wonO = true;
      for (int i = 0; i < 4; i++) {
        wonX &= (T[i][j] != 'O' && T[i][j] != '.');
        wonO &= (T[i][j] != 'X' && T[i][j] != '.');
      }
      if (wonX or wonO) goto ans;
    }
    ans:
    printf("Case #%d: ", iT++);
    if (!wonX && !wonO) {
      if (cont > 0) printf("Game has not completed\n");
      else printf("Draw\n");
    } else {
      if (wonX) printf("X won\n");
      else printf("O won\n");
    }
  }
  return 0;
}
