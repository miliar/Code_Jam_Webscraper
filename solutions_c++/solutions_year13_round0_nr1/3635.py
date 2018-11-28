#include <iostream>
using namespace std;

void checkGame( char a[ 4 ][ 4 ], bool inComplete, int currCase ) {
   // check the columns
   char curr;
   for( int i = 0; i < 4; i++ ) {
      int j = 1;
      curr = a[ 0 ][ i ];
      if( curr == 'T' ) {
         curr = a[ 1 ][ i ];
         j = 2;
      }
      if( curr == '.' )
         continue;
      for( ; j < 4; j++ ) {
         if( a[ j ][ i ] != curr && a[ j ][ i ] != 'T' )
            break;
      }
      if( j == 4 ) {
         cout << "Case #" << currCase << ": " << curr << " won" << endl;
         return;
      }
   }
   // check diagonals
   curr = a[ 0 ][ 0 ];
   int i = 1;
   if( curr == 'T' ) {
      curr = a[ 1 ][ 1 ];
      i = 2;
   }
   if( curr != '.' ) {
      for( ; i < 4; i++ ) {
         if( a[ i ][ i ] != curr && a[ i ][ i ] != 'T' )
            break;
      }
      if( i == 4 ) {
         cout << "Case #" << currCase << ": " << curr << " won" << endl;
         return;
      }
   }
   curr = a[ 0 ][ 3 ];
   i = 1;
   if( curr == 'T' ) {
      curr = a[ 1 ][ 2 ];
      i = 2;
   }
   if( curr != '.' ) {
      for( ; i < 4; i++ ) {
         if( a[ i ][ 3-i ] != curr && a[ i ][ 3-i ] != 'T' )
            break;
      }
      if( i == 4 ) {
         cout << "Case #" << currCase << ": " << curr << " won" << endl;
         return;
      }
   }
   if( inComplete )
      cout << "Case #" << currCase << ": Game has not completed" << endl;
   else
      cout << "Case #" << currCase << ": Draw" << endl;
}

int main() {
   int TestCases;
   cin >> TestCases;
   int currCase = 1;
   while( currCase <= TestCases ) {
      char a[4][4];
      bool result = false;
      bool inComplete = false;
      // checking rows while extracting input itself
      for( int i = 0; i < 4; i++ ) {
         char curr;
         bool win = true;
         cin >> curr;
         a[ i ][ 0 ] = curr;
         int j = 1;
         if( curr == 'T' ) {
            cin >> curr;
            a[ i ][ 1 ] = curr;
            j = 2;
         }
         if( curr == '.' ) {
            inComplete = true;
            win = false;
         }
         for( ; j < 4; j++ ) {
            cin >> a[ i ][ j ];
            if( a[ i ][ j ] == '.' ) {
               inComplete = true;
               win = false;
            }
            else {
               if( win && ( a[ i ][ j ] != curr && a[ i ][ j ] != 'T' ) ) 
                  win = false;
            }
         }
         if( win && !result ) {
            cout << "Case #" << currCase << ": " << curr << " won" << endl;
            result = true;  
         }
      }
      if( !result )    // conitnue checking only if we couldn't find a winner with rows
         checkGame( a, inComplete, currCase );
      currCase++;
   }
   return 0;
}
