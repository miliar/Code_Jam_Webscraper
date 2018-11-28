#include <stdio.h>

int T;
char f[4][5];
int i;

bool checkRow(int r, char c)
{
  int j;
  for (j = 0; j < 4; j++)
    if (f[r][j] != c && f[r][j] != 'T') return false;
    
  return true;  
}

bool checkCol(int col, char c)
{
  int i;
  for (i = 0; i < 4; i++)
    if (f[i][col] != c && f[i][col] != 'T') return false;
    
  return true;  
}

bool checkDiag1(char c)
{
  int i;
  for (i = 0; i < 4; i++)
    if (f[i][i] != c && f[i][i] != 'T') return false;
    
  return true;  
}

bool checkDiag2(char c)
{
  int i;
  for (i = 0; i < 4; i++)
    if (f[i][4-i-1] != c && f[i][4-i-1] != 'T') return false;
    
  return true;  
}

bool isComplete()
{
  int i, j;
  for (i = 0; i < 4; i++)
    for (j = 0; j < 4; j++)
      if (f[i][j] == '.') return false;
      
  return true;    
}

int main() {

  scanf("%d", &T);
  
  int cs = 0;
  while (T--) {
    cs++;
    
    for (i = 0; i < 4; i++)
      scanf("%s", f[i]);

    bool win = false;
    for (i = 0; i < 4; i++) {
      if (checkRow(i, 'X')) {
        win = true;
        break;
      }
    }
    if (win) {
      printf("Case #%d: X won\n", cs);
      continue;
    }

    win = false;
    for (i = 0; i < 4; i++) {
      if (checkCol(i, 'X')) {
        win = true;
        break;
      }
    }
    if (win) {
      printf("Case #%d: X won\n", cs);
      continue;
    }
    
    if (checkDiag1('X')) {
      printf("Case #%d: X won\n", cs);
      continue;      
    }
    if (checkDiag2('X')) {
      printf("Case #%d: X won\n", cs);
      continue;      
    }

    win = false;
    for (i = 0; i < 4; i++) {
      if (checkRow(i, 'O')) {
        win = true;
        break;
      }
    }
    if (win) {
      printf("Case #%d: O won\n", cs);
      continue;
    }

    win = false;
    for (i = 0; i < 4; i++) {
      if (checkCol(i, 'O')) {
        win = true;
        break;
      }
    }
    if (win) {
      printf("Case #%d: O won\n", cs);
      continue;
    }
    
    if (checkDiag1('O')) {
      printf("Case #%d: O won\n", cs);
      continue;      
    }
    if (checkDiag2('O')) {
      printf("Case #%d: O won\n", cs);
      continue;      
    }
    
    if (isComplete()) {
      printf("Case #%d: Draw\n", cs);
      continue;            
    }
  
      
    printf("Case #%d: Game has not completed\n", cs);
  }
  
  return 0;
}