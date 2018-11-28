#include <iostream>
#include <cmath>
#include <fstream>
#include <sstream>
#include <map>
#include <vector>

int solve()
{
  int n = 4;
  std::vector<std::string> board(4);
  for (int i=0; i<n; ++i)
    std::cin >> board[i];

  int cnt_t(0), cnt_x(0), cnt_o(0);
  
  for (int i=0; i<n; ++i) {
    cnt_t = cnt_x = cnt_o = 0;
    for (int j=0; j<n; ++j) {
      if (board[i][j] == 'T') ++cnt_t;
      if (board[i][j] == 'X') ++cnt_x;
      if (board[i][j] == 'O') ++cnt_o;
    }
    if (cnt_x==4 || (cnt_t==1 && cnt_x==3)) return 0;
    if (cnt_o==4 || (cnt_t==1 && cnt_o==3)) return 1;
  }

  for (int i=0; i<n; ++i) {
    cnt_t = cnt_x = cnt_o = 0;    
    for (int j=0; j<n; ++j) {
      if (board[j][i] == 'T') ++cnt_t;
      if (board[j][i] == 'X') ++cnt_x;
      if (board[j][i] == 'O') ++cnt_o;
    }
    if (cnt_x==4 || (cnt_t==1 && cnt_x==3)) return 0;
    if (cnt_o==4 || (cnt_t==1 && cnt_o==3)) return 1;
  }

  cnt_t = cnt_x = cnt_o = 0;  
  for (int i=0; i<4; ++i) {
    if (board[i][i] == 'T') ++cnt_t;
    if (board[i][i] == 'X') ++cnt_x;
    if (board[i][i] == 'O') ++cnt_o;
  }
  if (cnt_x==4 || (cnt_t==1 && cnt_x==3)) return 0;
  if (cnt_o==4 || (cnt_t==1 && cnt_o==3)) return 1;

  cnt_t = cnt_x = cnt_o = 0;  
  for (int i=0; i<4; ++i) {
    if (board[i][3-i] == 'T') ++cnt_t;
    if (board[i][3-i] == 'X') ++cnt_x;
    if (board[i][3-i] == 'O') ++cnt_o;
  }
  if (cnt_x==4 || (cnt_t==1 && cnt_x==3)) return 0;
  if (cnt_o==4 || (cnt_t==1 && cnt_o==3)) return 1;
  
  cnt_t = 0;
  for (int i=0; i<n; ++i) {
    for (int j=0; j<n; ++j)
      if (board[i][j]=='.') ++cnt_t;
  }

  if (cnt_t == 0) return 2;

  return 3;
}

int main()
{
  freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w", stdout);

  int n=0;
  scanf("%d", &n);

  for (int i=1; i<=n; ++i) {
    switch(solve()) {
      case 0:
        printf("Case #%d: X won\n", i); break;;
      case 1:
        printf("Case #%d: O won\n", i); break;
      case 2:
        printf("Case #%d: Draw\n", i); break;
      case 3:
        printf("Case #%d: Game has not completed\n", i);
        break;
      default: break;
    }
  }

  fclose(stdin);
  fclose(stdout);
  
  return 0;
}
