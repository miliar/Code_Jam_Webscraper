#include <iostream>
#include <stdio.h>
#include <queue>
#include <algorithm>
#include <vector>
#include <list>
#include <set>
#include <math.h>
using namespace std;

//trocar para 0 para desabilitar output
#if 1
#define DEBUG(x) cout << x << endl
#define PAUSE() cin.get(); cin.get()
#else
#define DEBUG(x)
#define PAUSE()
#endif

#define TRACE(x) DEBUG(#x << " = " << x)
#define DEBUGS() DEBUG("***************************")
#define MAX 4

char game[MAX][MAX];

bool win(char c){
  bool ok1 = true, ok2 = true;
  for (int i = 0; i < MAX; ++i){
    ok1 = true, ok2 = true;
    for (int j = 0; j < MAX; ++j){
      if (game[i][j] != 'T' && game[i][j] != c) ok1 = false;
      if (game[j][i] != 'T' && game[j][i] != c) ok2 = false;
    }
    if (ok1 || ok2) return true;
  }
  ok1 = true, ok2 = true;
  for (int i = 0; i < MAX; ++i){
    if (game[i][i] != 'T' && game[i][i] != c) ok1 = false;
    if (game[MAX-i-1][i] != 'T' && game[MAX-i-1][i] != c) ok2 = false;
  }
  return ok1 || ok2;
}

int dots(){
  int d = 0;
  for (int i = 0; i < MAX; ++i)
    for (int j = 0; j < MAX; ++j)
      if (game[i][j] == '.') ++d;
  return d;
}

int main(){
  int t, p = 0;
  cin >> t;
  while (t--){
    for (int i = 0; i < MAX; ++i)
      cin >> game[i];
    printf("Case #%d: ", ++p);
    if (win('X')) puts("X won");
    else if (win('O')) puts("O won");
    else if (dots() == 0) puts("Draw");
    else puts("Game has not completed");
  }
  return 0;
}
