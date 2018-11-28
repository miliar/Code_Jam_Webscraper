#include<iostream>
#include<vector>
#include<string>
#define rep(x,n) for (int x = 0; x < n; x++)
#define pb push_back
using namespace std;
int main()
{
 int tt; cin >> tt;
 string a; vector <string> V;
 int poziomX, poziomY,diagonalX,diagonalY,dx1,dy1;
 vector < int > pionX, pionY;
 bool empty,pp;
 rep(t,tt)
 {
  diagonalX = 0; diagonalY = 0; dx1 = 0; dy1= 0;
  poziomX = 0; poziomY = 0;
  pionX.clear(); pionY.clear();
  pionX.resize(4); pionY.resize(4);
  V.clear();
  empty = false; pp = false;
  rep(y,4)
  {
   cin >> a; cin.get(); V.pb(a);
  }

  rep(y,4)
  {
   poziomX = 0; poziomY = 0;
    rep(z,4)
    {
     if (V[y][z] == 'X')
     {
      ++poziomX;
      ++pionX[z];
      if (y == z)
        {
         ++diagonalX;
        }
      if (y + z == 3)
      {
        ++dx1;
      }
     } else if (V[y][z] == 'O')
     {
      ++poziomY;
      ++pionY[z];
       if (y == z)
        {
         ++diagonalY;
        }
        if (y + z == 3) ++dy1;
     } else if (V[y][z] == 'T')
     {
      ++poziomX;
      ++pionX[z];
      ++poziomY;
      ++pionY[z];
       if (y == z)
        {
         ++diagonalX;
         ++diagonalY;
        }
        if (y + z == 3) { ++dx1; ++ dy1;}
     } else empty = true;
     if (poziomX >= 4)
     {
      cout << "Case #" << t+1 << ": X won\n";
      break;
     }
     if(poziomY >= 4)
     {
      cout << "Case #" << t+1 << ": O won\n";
      break;
     }

    }
   if (poziomX >= 4 || poziomY >= 4) break;
  }

  if (poziomX < 4 && poziomY < 4)
  {
    rep(y,4)
    {
     if (pionX[y] >= 4)
     {
        cout << "Case #" << t+1 << ": X won\n";
        pp =true;
        break;
     }
     if (pionY[y] >= 4)
     {
         cout << "Case #" << t+1 << ": O won\n";
         pp =true;
         break;
     }
    }
      if (diagonalX >= 4 || dx1 >= 4)
     {
      cout << "Case #" << t+1 << ": X won\n";
        pp =true;
     }
     if (diagonalY >= 4 || dy1 >= 4)
     {
      cout << "Case #" << t+1 << ": O won\n";
        pp =true;
     }
    if (!pp)
    {
     if (empty) cout << "Case #" << t+1 << ": Game has not completed\n";
     else cout << "Case #" << t+1 << ": Draw\n";
    }

  }

 }
 return 0;
}
