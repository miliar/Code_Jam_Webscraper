#include <stdio.h>
#include <string.h>
#include <string.h>
#include <math.h>

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

const int MAXN = 4;
const int INF = 0x3f3f3f3f;

char board[MAXN+1][MAXN+1];
string output[MAXN] = {"O won", "X won", "Draw", "Game has not completed"};

// 0 for O, 1 for X, 2 for draw, 3 for not finished
int answer() {
  int b[MAXN][MAXN];
  int winning[2][2] = { {8,7}, {-8,-5}};
  memset(b, 0, sizeof(b));
  int empty = 0;
  for(int i=0; i<MAXN; ++i) for(int j=0; j<MAXN; ++j) {
    if(board[i][j] == 'O') b[i][j] = 2;
    if(board[i][j] == 'X') b[i][j] = -2;
    if(board[i][j] == 'T') b[i][j] = 1;
    if(board[i][j] == '.') empty++;
  }
  for(int i=0; i<MAXN; ++i) {
    int sumrow = 0;
    for(int j=0; j<MAXN; ++j) {
      sumrow += b[i][j];
    }
    for(int k=0; k<2; ++k) {
      if(sumrow == winning[k][0] || sumrow == winning[k][1]) return k;
    }
  }

  for(int j=0; j<MAXN; ++j) {
    int sumcol = 0;
    for(int i=0; i<MAXN; ++i) {
      sumcol += b[i][j];
    }
    for(int k=0; k<2; ++k)
      if(sumcol == winning[k][0] || sumcol == winning[k][1]) return k;
  }

  int sumdiag = 0;
  for(int i=0; i<MAXN; ++i) sumdiag += b[i][i];    
  for(int k=0; k<2; ++k)
    if(sumdiag == winning[k][0] || sumdiag == winning[k][1]) return k;
  
  sumdiag = 0;
  for(int i=0; i<MAXN; ++i) sumdiag += b[i][MAXN-i-1];
  for(int k=0; k<2; ++k)
    if(sumdiag == winning[k][0] || sumdiag == winning[k][1]) return k;

  if(empty == 0) return 2;
  return 3;
}

int main() {
  //freopen("A.in", "r", stdin);

  int T; scanf("%d", &T);
  for(int ic=1; ic<=T; ++ic) {
    for(int i=0; i<MAXN; ++i) scanf("%s", &board[i]);//, printf("%s\n", board[i]);
    int res = answer();
    printf("Case #%d: %s\n", ic, output[res].c_str());
  }
  return 0;
}
