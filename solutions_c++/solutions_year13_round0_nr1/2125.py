#include <cstdio>
#include <algorithm>
#include <string>
#include <map>
#include <vector>

using namespace std;

char t[10][10];
int has_ended() {
  for (int i = 0; i < 4; i++)
    for (int j = 0; j < 4; j++)
      if (t[i][j] == '.') return false;
  return true;
}

int has_won(char c) {
  for (int i = 0; i< 4; i++) {
    if (t[i][0] == c || t[i][0] == 'T') {
      int ok = 1;
      for (int j = 0; j < 4 && ok; j++) {
	if (t[i][j] != c && t[i][j] != 'T') {
	  ok = 0;
	}
      }
      if (ok) return true;
    }
    
    if (t[0][i] == c || t[0][i] == 'T') { 
      int ok = 1;
      for (int j = 0; j < 4 && ok; j++) {
	if (t[j][i] != c && t[j][i] != 'T') {
	  ok = 0;
	}
      }
      if (ok) return true;
    }
  }
  if (t[0][0] == c || t[0][0] == 'T') {
    int ok = 1;
    for (int i = 0; i < 4 && ok; i++) {
      if (t[i][i] != c && t[i][i] != 'T') {
	ok = 0;
      }
    }
    if (ok) return true;
  }
  if (t[0][3] == c || t[0][3] == 'T') {
    int ok = 1;
    for (int i = 0; i < 4 && ok; i++) {
      if (t[i][3-i] != c && t[i][3-i] != 'T') {
	ok = 0;
      }
    }
    if (ok) return true;
  }
  return false;
}

int main() {
  int T;
  scanf("%d", &T);
  int c = 1;
  while (T--) {
    for (int i = 0; i < 4; i++) scanf("%s", t[i]);
    printf("Case #%d: ", c++);
    if (has_won('O')) {
      printf("O won\n");
    } else if (has_won('X')) {
      printf("X won\n");
    } else if (!has_ended()) {
      printf("Game has not completed\n");
    } else printf("Draw\n");
  }
  return 0;
}
