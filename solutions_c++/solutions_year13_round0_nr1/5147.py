
#include<cstdio>
#include<cassert>
#include<cstring>
#include<iostream>
#include<cstdlib>
#include<vector>
#include<algorithm>

//int findCombo( int n, 

int main() {
   char mat[4][4];
   int sump[50]= {-1};
   int xwinsum1='X'*4,xwinsum2='X'*3+'T';
   int owinsum1='O'*4,owinsum2='O'*3+'T';
   memset( sump, 0, sizeof( sump ) );
   sump[xwinsum1-4*'O']=1;
   sump[xwinsum2-4*'O']=1;
   sump[owinsum1-4*'O']=1;
   sump[owinsum2-4*'O']=1;
   /*for( int i = 0 ; i <= 4; i++ ) {
      int index = 'O' * i + 'X'*(4-i)  - 4*'O';
      printf( "Sum : %d X %d times, O %d times\n", index, 4-i, i );
      assert ( index < 50 );
      assert( sump[index] == -1 );
      sump[index]=1;
      if( i <= 3 ) {
         int index = 'O' * i + 'X'*(3-i) + 'T' - 4*'O';
         printf( "Sum : %d X %d times, O %d times T once\n", index, 3-i, i );
         assert ( index < 50 );
         assert( sump[index] == -1 );
         sump[index]=1;
      }
      }*/


   int num;
   scanf( "%d", &num );
   for( int i = 0; i < num; i++ ) {
      int sum = 0, found = 0, dotFound = 0;
      //printf( "New case\n" );
      for( int j = 0; j < 4; j++ ) {
         scanf( "%s", mat[j] );
         //printf( "%s\n", mat[j] );
      }
      scanf( "\n" );
      for( int j = 0; j < 4; j++ ) {
         sum = 0;
         for( int k = 0; k < 4; k++ ) {
            if( mat[j][k] == '.' ) { dotFound=1;sum=-1;break; }
            sum += mat[j][k];
         }
         if( sum != -1 && sump[sum-4*'O'] ) {
            printf( "Case #%d: %c won\n", i+1, mat[j][0] == 'T' ? mat[j][1] : mat[j][0] );
            found = 1;
            break;
         }
      }
      if( found ) {
         continue;
      }
      // Now columns.
      for( int j = 0; j < 4; j++ ) {
         sum = 0;
         for( int k = 0; k < 4; k++ ) {
            if( mat[k][j] == '.' ) { dotFound=1;sum=-1;break; }
            sum += mat[k][j];
         }
         if( sum != -1 && sump[sum-4*'O'] ) {
            printf( "Case #%d: %c won\n", i+1, mat[0][j] == 'T' ? mat[1][j] : mat[0][j] );
            // printf( "sum : %d\n ", sum );
            found = 1;
            break;
         }
      }
      if( found ) {
         continue;
      }
      // Now diagonal
      int col=0, inc=1;
      for( int j = 0; j < 2; j++,inc=-1,col=3  ) {
         sum = 0;
         for( int k = 0; k < 4; k++ ) {
            if( mat[k][col+inc*k] == '.' ) { dotFound=1;sum=-1;break; }
            sum += mat[k][col+inc*k];
         }
         if( sum != -1 && sump[sum-4*'O'] ) {
            printf( "Case #%d: %c won\n", i+1, mat[0][col] == 'T' ? mat[1][col+inc] : mat[0][col] );
            found = 1;
            break;
         }
      }
      if( !found ) {
         if( dotFound ) {
            printf( "Case #%d: Game has not completed\n", i+1  );
         } else {
            printf( "Case #%d: Draw\n", i+1 );
         }
      }
   }
   return 0;
}


