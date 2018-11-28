#include <iostream>
using namespace std;

#define MAX 50

char grid[MAX][MAX];

int main()
{
  int T;

  cin >> T;

 for( int ti = 0; ti < T; ++ti)
  {
   int R, C;
   char c;
   cin >> R >> C;

   for(int i = 0; i < R; ++i)
     for(int j =0; j < C; ++j)
       cin >> grid[i][j];

   bool possible = true;

   for(int i = 0; i < R; ++i)
     for(int j = 0; j < C; ++j)
      {
       char & item = grid[i][j];

        if( item == '.' || item == '/' || item == '\\' )
            continue;

         if( i == R - 1 || j == C - 1)
          {
           possible = false;
           goto RESULTS;
          }

         // grid[i][j] == '#'

         if( grid[i][j+1] == '#' && grid[i+1][j] == '#' && grid[i+1][j+1] == '#' )
            {
               grid[i][j]   = '/' ; grid[i][j+1]   = '\\';
               grid[i+1][j] = '\\'; grid[i+1][j+1] = '/';
               continue;
            }

         possible = false;
         goto RESULTS;
      }

  RESULTS:

    cout << "Case #" << (ti+1) << ":" << endl;
    if( !possible )
      cout << "Impossible" << endl;
    else
     for(int i = 0; i < R; ++i)
     {
       for(int j =0; j < C; ++j)
         cout << grid[i][j];
       cout << endl;
     }
  }

 return 0;
}
