#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>
#include <map>
#include <set>

using namespace std;

const int SIZE = 4;
const int ALL_POSS = 10;

char board[SIZE][SIZE];

#define E 3
#define O 141
#define X 809
#define T 3251

int get(int x, int y)   {
   if(board[x][y] == '.')
      return E;
   if(board[x][y] == 'O')
      return O;
   if(board[x][y] == 'X')
      return X;
   if(board[x][y] == 'T')
      return T;
}

void findSol(int c) {
   int i,j;
   int all[ALL_POSS];
   int tmp;
   bool fin = true;

   for(i=0; i < ALL_POSS; i++) {
      all[i] = 0;
   }

   for(i = 0; i < SIZE; i++)  {
      for(j=0; j < SIZE; j++)  {
         tmp = get(i,j);
         if(tmp == E)
            fin = false;
         all[i] += tmp;
         tmp = get(j,i);
         if(tmp == E)
            fin = false;
         all[i+SIZE] += tmp;
      }
      all[8] += get(i,i);
   }
   all[9] += get(0,3);
   all[9] += get(1,2);
   all[9] += get(2,1);
   all[9] += get(3,0);

   cout <<"Case #" << c <<": ";
   bool written = false;
   for(i=0; i < ALL_POSS; i++) {
      if(all[i] == (O*4) || (all[i] == ((O*3) + T))) {
         cout <<"O won\n";
         written = true;
         break;
      }
      else if(all[i] == (X*4) || (all[i] == ((X*3) + T)))  {
         cout <<"X won\n";
         written = true;
         break;
      }
   }
   if(!written)   {
      if(fin)
         cout <<"Draw\n";
      else
         cout <<"Game has not completed\n";
   }
}

int main(int argc, char* argv[]) {
   int tests;
   int i, j, k, l, m;

   cin >> tests;
   for(i=0; i < tests; i++) {
      for(j=0; j < SIZE; j++)  {
         cin >> board[j];
      }
      findSol(i+1);
   }
   return 0;
}
