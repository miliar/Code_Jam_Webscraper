#include <cstdio>
using namespace std;

char T[5][5];

int checkX(int i, char C) {
  bool ok = true;
  for (int j = 0; j < 4; j++) 
    if (T[i][j] != C && T[i][j] != 'T') ok = false;
  if (ok) return true;
  ok = true;
  for (int j = 0; j < 4; j++) 
    if (T[j][i] != C && T[j][i] != 'T') ok = false;
  return ok;
}

int checkD(char C) {
  bool ok = true;
  for (int i = 0; i < 4; i++) if (T[i][i] != C && T[i][i] != 'T') ok = false;
  if (ok) return true;
  ok = true;
  for (int i = 0; i < 4; i++) if (T[i][3-i] != C && T[i][3-i] != 'T') ok = false;
  return ok;
}

int result() {
  for (int i = 0; i < 4; i++) 
    if (checkX(i,'X') || checkD('X')) return 1;
    else if (checkX(i,'O') || checkD('O')) return 2;
  for (int i = 0; i < 4; i++) for (int j = 0; j < 4; j++)
    if (T[i][j] == '.') return 0;
  return 3;
}

int main() {
  int z; scanf ("%d", &z);
  for (int i = 1; i <= z; i++) {
    for (int j = 0; j < 4; j++) scanf ("%s", T[j]);
    printf ("Case #%d: ", i);
    switch (result()) {
      case 0: printf("Game has not completed\n"); break;
      case 1: printf("X won\n"); break;
      case 2: printf("O won\n"); break;
      case 3: printf("Draw\n"); break;
    }
  }

  return 0;
}

