#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>

using namespace std;

char map[4][5];
int T, spaces;

bool check_row( int i, char what ) {

     return ( ( map[i][0] == what || map[i][0] == 'T' ) && ( map[i][1] == what || map[i][1] == 'T' ) && ( map[i][2] == what || map[i][2] == 'T' ) && ( map[i][3] == what || map[i][3] == 'T' ) );
     
}

bool check_col( int i, char what ) {

     return ( ( map[0][i] == what || map[0][i] == 'T' ) && ( map[1][i] == what || map[1][i] == 'T' ) && ( map[2][i] == what || map[2][i] == 'T' ) && ( map[3][i] == what || map[3][i] == 'T' ) );
     
}

bool check_diag_main( char what ) {

     return ( ( map[0][0] == what || map[0][0] == 'T' ) && ( map[1][1] == what || map[1][1] == 'T' ) && ( map[2][2] == what || map[2][2] == 'T' ) && ( map[3][3] == what || map[3][3] == 'T' ) );
     
}

bool check_diag_second( char what ) {

     return ( ( map[3][0] == what || map[3][0] == 'T' ) && ( map[2][1] == what || map[2][1] == 'T' ) && ( map[1][2] == what || map[1][2] == 'T' ) && ( map[0][3] == what || map[0][3] == 'T' ) );
     
}

int main( ) {

    freopen("in.txt","r",stdin);
    
    
    freopen("out.txt","w",stdout);
    
    
    scanf ( "%d", &T );
    
    //printf ( "%d\n", T );
    
    for ( int t = 1; t <= T; ++t ) {
    
          for ( int i = 0; i < 4; ++i )
              scanf ( " %s", map[i] );
          
          spaces  = 0;
          
          for ( int i = 0; i < 4; ++i )
              for ( int j = 0; j < 4; ++j )
                  spaces = ( map[i][j] == '.' ) ? ( spaces+1 ) : spaces;

          //printf ( "There are %d spaces\n", spaces );
          
          bool Xwon = false;
          bool Owon = false;
          
          for ( int i = 0; i < 4; ++i ) {
          
              //for every row i
              if ( check_row( i, 'X' ) ) {
                 Xwon = true;
              }
              
              if ( check_row( i, 'O' ) ) {
                 Owon = true;
              }
              
              //for every col i
             if ( check_col( i, 'X' ) ) {
                Xwon = true;
             }
             
             if ( check_col( i, 'O' ) ) {
                Owon = true;
             }
          
             //printf ( "%s\n", map[i] );
          
          }
          
          //check diagonals
          
          if ( check_diag_main( 'O' ) || check_diag_second( 'O' ) ) {
               Owon = true;
          }
          
          if ( check_diag_main( 'X' ) || check_diag_second( 'X' ) ) {
               Xwon = true;
          }
          
          if ( !Xwon && !Owon && spaces == 0 ) {
             printf ( "Case #%d: Draw\n", t );     
          }else if ( Xwon ) {
             printf ( "Case #%d: X won\n", t );      
          }else if ( Owon ) {
             printf ( "Case #%d: O won\n", t );      
          }else {
             printf ( "Case #%d: Game has not completed\n", t );      
          }
          
    }

    return 0;
   
}
