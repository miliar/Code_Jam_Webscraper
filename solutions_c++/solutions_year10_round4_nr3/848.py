#include <iostream>

using namespace std;

typedef long long int llint;

#define L 305
int board[L+2][L+2];


void solveCase(unsigned int caseNum)
{
  int i, j, r, x1, x2, y1, y2, tmp, aux;
  
  for(i=0;i<L;i++)
  for(j=0;j<L;j++)
    board[i][j] = 0;

  cin >> r;
  for(tmp = 0; tmp < r; tmp++)
  {
    cin >> x1 >> y1 >> x2 >> y2;
    //x1--;x2--;y1--;y2--;
    if(x2<x1)
    {
      aux = x1; x1=x2;x2=aux;
    }
    if(y2<y1)
    {
      aux = y1; y1=y2;y2=aux;
    }
    for(i=x1;i<=x2;i++)
    for(j=y1;j<=y2;j++)
      board[i][j] = 1;
  }

  int s = 0;
  bool life = true;
  while(life)
  {
    life = false;
    for(i=L;i>0;i--)
    {
    for(j=L;j>0;j--)
    {
      if(board[i-1][j] == 0 && board[i][j-1] == 0)
        board[i][j] = 0;
      if(board[i-1][j] == 1 && board[i][j-1] == 1)
        board[i][j] = 1;

      if(board[i][j] != 0)
        life = true;
  //    cout << board[i][j] << " ";
    }
//    cout << endl;
    }

    bool move = true;
    for(i=L;i>0;i--)
    {
      if(board[0][i-1] == 0)
        board[0][i] = 0;
      if(board[i-1][0] == 0)
        board[i][0] = 0;
      if(board[i][0] == 1 || board[0][i] == 1)
      {
        life = true;
        move = false;
      }
    }
    board[0][0] = 0;
    
    if(move) {
      for(i=0;i<L;i++)
      for(j=0;j<L;j++)
        board[i][j] = board[i+1][j+1];
    }
    s++;
  }

	cout << "Case #" << caseNum << ": " << s << endl;
}

int main()
{
  unsigned int t, i;
  
  cin >> t;
  for(i=1; i<=t; i++)
    solveCase(i);

  return 0;
}
