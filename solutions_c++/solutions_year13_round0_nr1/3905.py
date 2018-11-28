#include <cstdio>
#include <algorithm>

using namespace std;

int T;
char board[4][5];

const int X = 0, O = 1, NONE = 2;

int won(int i1, int j1, int di, int dj)
{
   int nbO = 0, nbX = 0;
   for(int i=i1, j=j1; i < 4 && j < 4; i += di, j += dj)
   {
      nbX += (board[i][j] == 'X') + (board[i][j] == 'T');
      nbO += (board[i][j] == 'O') + (board[i][j] == 'T');
   }
   if(nbX == 4) return X;
   if(nbO == 4) return O;
   return NONE;
}

void f(int test)
{
   bool full = true;
   for(int i=0; i<4; i++)
   {
      scanf("%s", board[i]);
      for(int j=0; j<4; j++)
         if(board[i][j] == '.')
            full = false;
   }
   for(int d=0; d<4; d++)
   {
      int r[4] = {won(0, d, 1, 0), won(d, 0, 0, 1), won(0, 0, 1, 1), won(3, 0, -1, 1)};
      for(int i=0; i<4; i++)
      {
         if(r[i] == X) {
            printf("Case #%d: X won\n", test);
            return;
         }
         if(r[i] == O) {
            printf("Case #%d: O won\n", test);
            return;
         }
      }
   }
   if(full) printf("Case #%d: Draw\n", test);
   else printf("Case #%d: Game has not completed\n", test);
}

int main()
{
   scanf("%d", &T);
   for(int test=0; test<T; test++)
      f(test + 1);
   return 0;
}
