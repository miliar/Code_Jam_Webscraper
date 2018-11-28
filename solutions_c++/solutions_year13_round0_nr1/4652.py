#include <cstdio>

using namespace std;

char m[4][8];

bool checkWin(char c) {
  // check lines
  for (int i = 0; i<4; i++) {
    bool found = false;
    for (int j = 0; j<4; j++)
      if (m[i][j] != c && m[i][j] != 'T') {
	found = true;
	break;
      }
    if (!found) 
      return true;
  }

  //check columns
  for (int i = 0; i<4; i++) {
    bool found = false;
    for (int j = 0; j<4; j++)
      if (m[j][i] != c && m[j][i] != 'T') {
	found = true;
	break;
      }
    if (!found) 
      return true;
  }
  
  //check d1
  bool found = false;
  for (int i = 0; i<4; i++)
    if (m[i][i] != c && m[i][i] != 'T') {
	found = true;
	break;
    }
  if (!found) 
    return true;
  
  //check d2
  found = false;
  for (int i = 0; i<4; i++)
    if (m[i][3-i] != c && m[i][3-i] != 'T') {
	found = true;
	break;
    }
  if (!found) 
    return true;

  return false;
}

bool draw() {
  for (int i = 0; i<4; i++)
    for (int j = 0; j<4; j++)
      if (m[i][j] == '.')
	return false;
  return true;
}

int main() {
  int tt;
  scanf("%d", &tt);
  for (int t = 1; t <= tt; t++) {
    for (int i = 0; i<4; i++)
      scanf("%s", m[i]);
    
    printf("Case #%d: ", t);
    if (checkWin('X'))
      printf("X won\n");
    else if (checkWin('O'))
      printf("O won\n");
    else if (draw())
      printf("Draw\n");
    else
      printf("Game has not completed\n");
  }
  return 0;
}

