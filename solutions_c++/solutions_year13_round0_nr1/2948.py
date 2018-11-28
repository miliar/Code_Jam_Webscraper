#include <iostream>
using namespace std;

int winnerCheck( int &o, int &x, int &t)
{
  //cout << o  << " " << x << " " << t <<endl;;
  if (o == 4 )  return 1;
  if (x ==4) return 2;
  else if ((o==3) && (t==1)) return 1;
  else if ((x==3) && (t==1) ) return 2;
  o=x=t=0;
  return 0;
}


int main()
{
  char chess[4][4];
  int n=0;
  cin >> n;
  int cnt=0;
  bool gameCompleted = false;
  
  for (int k=0;k<n;++k)
  {
    cnt=0;
    gameCompleted = false;
  for (int i=0;i<4;++i)
  {
     for (int j=0;j<4;++j)
     {
        cin >> chess[i][j];
        if (chess[i][j] !='.') 
          ++cnt;
     }
  }
  if (cnt == 16) gameCompleted = true;
//  check |
  int winner = 0;
  for (int i=0;i<4;++i)
  {
     int o = 0;
     int x = 0;
     int t = 0;
     for (int j=0;j<4;++j)
     {
       if (chess[i][j] == 'X') ++x;
       if (chess[i][j] == 'O') ++o;
       if (chess[i][j] == 'T') ++t;
     }
     if ((winner = winnerCheck(o,x,t)) !=0) 
        break;
     for (int j=0;j<4;++j)
     {
       if (chess[j][i] == 'X') ++x;
       if (chess[j][i] == 'O') ++o;
       if (chess[j][i] == 'T') ++t;
     }
     if ((winner = winnerCheck(o,x,t)) !=0)
       break;
     if (i==0)
     for (int j=0;j<4;++j)
     {
       if (chess[j][j] == 'X') ++x;
       if (chess[j][j] == 'O') ++o;
       if (chess[j][j] == 'T') ++t;
     }
     if ((winner = winnerCheck(o,x,t)) !=0)
       break;
     if (i == 3)
     for (int j=0;j<4;++j)
     {
       if (chess[i-j][j] == 'X') ++x;
       if (chess[i-j][j] == 'O') ++o;
       if (chess[i-j][j] == 'T') ++t;
     }
     if ((winner = winnerCheck(o,x,t)) !=0)
    break;

  }  
  cout << "Case #" << k+1 <<": ";
  if (winner == 0 && !gameCompleted) cout << "Game has not completed";
  else if (winner == 0) cout << "Draw";
  else if (winner == 1) cout << "O won";
  else if (winner == 2) cout << "X won";
  cout << "\n";
  }
  return 0;
}


