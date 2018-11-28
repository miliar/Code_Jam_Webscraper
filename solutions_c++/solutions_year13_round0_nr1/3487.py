#include<iostream>
#include<cstdio>

using namespace std;

int main() {
  int probs;
  cin >> probs;

  char map[4][4];

  for (int p = 1; p <= probs; p++) {
    int played = 0;
    char tmp;
    for (int x = 0; x < 4; x++) {
      for (int y = 0; y < 4; y++) {

        cin >> tmp;
        while (!isalpha(tmp) && tmp != '.') cin >> tmp;
        map[x][y] = tmp;
        //cout << tmp;

        if (map[x][y] != '.') played++;
      }
      //cout << endl;
    }

    bool xWin, oWin;
    xWin = false;
    oWin = false;

    for (int x = 0; x < 4; x++) {
      char first = map[x][0];
    if (first == '.' || first == 'T') continue;
      //printf("Checking row %i\n", x);
      //printf("First is %c\n", first);
      bool won = true;
      for (int y = 1; y < 4; y++) {
        if (map[x][y] == '.' || (map[x][y] != first && map[x][y] != 'T')) {
          //printf("%c has no row\n", first);
          won = false;
          break;
        }
      }

      if (won) {
        //printf("%c won!\n", first);
        if (first == 'X')
          xWin = true;
        if (first == 'O')
          oWin = true;
      }
    }

    for (int x = 0; x < 4; x++) {
      int y;
      char first = map[0][x];
    if (first == '.' || first == 'T') continue;
      bool won = true;
      for (y = 1; y < 4; y++) {
        if (map[y][x] == '.' || (map[y][x] != first && map[y][x] != 'T')) {
          //printf("%c has no column\n", first);
          won = false;
          break;
        }
      }

      if (won) {
        if (first == 'X') {
          //printf("%c won!\n", first);
          xWin = true;
        }
        if (first == 'O')
          oWin = true;
      }
    }

    char first = map[0][0];
    bool won = (first != 'T');
    for (int x = 1; x < 4; x++) {
      if (map[x][x] == '.' || (map[x][x] != first && map[x][x] != 'T')) {
        won = false;
        break;
      }

    }

    if (won) {
        //printf("%c won!\n", first);
      if (first == 'X')
        xWin = true;
      if (first == 'O')
        oWin = true;
    }

    first = map[0][3];
    won = (first != 'T'); 
    for (int x = 1; x < 4; x++) {
      if (map[x][3-x] == '.' || (map[x][3-x] != first && map[x][3-x] != 'T')) {
        won = false;
        break;
      }

    }

    if (won) {
        //printf("%c won!\n", first);
      if (first == 'X')
        xWin = true;
      if (first == 'O')
        oWin = true;
    }
    
    printf("Case #%i: ", p);
    if (oWin && xWin)
      printf("Draw");
    else {
      if (oWin)
        printf("O won");
      if (xWin)
        printf("X won");

      if (!oWin && !xWin) {
        if (played == 16)
          printf("Draw");
        else
          printf("Game has not completed");
      }
    }
    printf("\n");
  }
  return 0;
}
