#include <iostream>
#include <vector>
#include <deque>
#include <string>
#include <sstream>
#include <cmath>
#include <fstream>
#include <algorithm>
#include <functional>
using namespace std;

void redirectIO(string fileName)
{
   static ofstream fout ((fileName + ".out").c_str());
   static ifstream fin ((fileName + ".in").c_str());
   cin.rdbuf(fin.rdbuf());
   cout.rdbuf(fout.rdbuf());
}
bool isX(char a)
{
   return (a == 'X' || a == 'T');
}

bool isO(char a)
{
   return (a == 'O' || a == 'T');
}

bool isEqual(char a, char b)
{
   if (a == '.' || b == '.')
      return false;

   return (a == 'T' || b == 'T' || a == b );
}

char XorO(char game[4][4])
{
   bool diagonal = true;
   if (game[0][0] != '.')
   for (int i = 0; i < 4; ++i)
   {
      if (!isEqual(game[i][i], game[0][0]))
      {
         diagonal = false;
         break;
      }
   }
   if (diagonal)
   {
      return game[0][0];
   }

   diagonal = true;
   if (game[0][3] != '.')
   for (int i = 0; i < 4; ++i)
   {
         if (!isEqual(game[i][3-i], game[0][3]))
         {
            diagonal = false;
            break;
         }
    }
   if (diagonal)
   {
      return game[0][3];
   }

   bool solution1, solution2;
   for (int i = 0; i < 4; ++i)
   {
      for (int j = 0; j < 4; ++j)
      {
         if (game[i][j] == '.')
            continue;
         solution1 = solution2 = true;
         for (int u = 0; u < 4; ++u)
         {
            if ( !isEqual(game[i][u], game[i][j]) )
            {
               solution1 = false;
            }

            if ( !isEqual(game[u][j], game[i][j]) )
            {
               solution2 = false;
            }
         }
         if (solution1 || solution2)
         {
            return game[i][j];
         }
      }
   }
   return 'Z';
}

int main()
{
   redirectIO("test");
   unsigned short T;
   cin >> T;
   short res;

   char game[4][4];
   bool potentialNotFinished;
   for (unsigned t = 0; t < T; ++t)
   {
      // input
      potentialNotFinished = false;
      for (int i = 0; i < 4; ++i)
      {
         for (int j = 0; j < 4; ++j)
         {
            cin >> game[i][j];
            if (game[i][j] == '.')
               potentialNotFinished = true;
         }
      }
      if (potentialNotFinished)
      {
         res = 3;
      }
      else
      {
         res = 0;
      }

      // processing
      int ll = XorO(game) ;
      if (ll == 'X')
         res = 1;
      if (ll == 'O')
         res = 2;

      // output
      string str;
      if (res == 0)
      {
         str = "Draw";
      }
      else if (res == 1)
      {
         str = "X won";
      }
      else if (res == 2)
      {
         str = "O won";
      }
      else
      {
         str = "Game has not completed";
      }
      cout << "Case #"<<t+1<< ": "<<str<<endl;
   }
 
   return 0;
}