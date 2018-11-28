#include <iostream>

using namespace std;

int main()
{
   int T , z , i , j , x , o , s , t    ;
   char table[4][4] ;
   char  d  ;

   cin >> T ;

   for ( z=1 ; z <= T ; ++z ) {
     for ( i = 0 ; i < 4 ; i++ )
       for ( j = 0 ; j < 4 ; j++ )
        cin >> table[i][j] ;

/*
     cout << endl << endl ;
     for ( i = 0 ; i < 4 ; i++)  {
        cout << endl ;
        for ( j = 0 ; j < 4 ; j++)
           cout << table [i][j] ;
     }
*/
     d = ' ' ;
     while ( true ) {
        for ( i=0 ; i < 4 ; i++ ) {
          x = 0 ; o = 0 ; s = 0 ; t = 0 ;
          for ( j=0 ; j < 4 ; j++ )
            switch ( table[i][j] ) {
              case 'X':
                ++x ;
              break ;
              case 'O':
                ++o ;
              break ;
              case 'T':
                ++t ;
              break ;
              case '.':
                ++s ;
              break ;
            }

            if ( (x + t) ==  4  ) { d = 'X' ;   break ; }
            if ( (o + t) ==  4  ) { d = 'O' ;   break ; }

        }
        if ( d != ' ')  break ;

        for ( j=0 ; j < 4 ; j++ ) {
          x = 0 ; o = 0 ;  t = 0 ;
          for ( i=0 ; i < 4 ; i++ )
            switch ( table[i][j] ) {
              case 'X':
                ++x ;
              break ;
              case 'O':
                ++o ;
              break ;
              case 'T':
                ++t ;
              break ;
            }

            if ( (x + t) ==  4  ) { d = 'X' ;   break ; }
            if ( (o + t) ==  4  ) { d = 'O' ;   break ; }

        }
        if ( d != ' ')  break ;

        x = 0 ; o = 0 ;  t = 0 ;
        for ( i=0 ; i < 4 ; i++ )
            switch ( table[i][i] ) {
              case 'X':
                ++x ;
              break ;
              case 'O':
                ++o ;
              break ;
              case 'T':
                ++t ;
              break ;
            }

            if ( (x + t) ==  4  ) { d = 'X' ;   break ; }
            if ( (o + t) ==  4  ) { d = 'O' ;   break ; }

        x = 0 ; o = 0 ;  t = 0 ;
        for ( i=0 ; i < 4 ; i++ )
            switch ( table[i][3-i] ) {
              case 'X':
                ++x ;
              break ;
              case 'O':
                ++o ;
              break ;
              case 'T':
                ++t ;
              break ;
            }

            if ( (x + t) ==  4  ) { d = 'X' ;   break ; }
            if ( (o + t) ==  4  ) { d = 'O' ;   break ; }


            break ;


     }  // end of while


      if ( d == 'X')  { cout << "Case #" << z << ": " <<  "X won" << endl ;  continue ; }
      if ( d == 'O')  { cout << "Case #" << z << ": " <<  "O won" << endl ;  continue ; }
      if ( s == 0 )  cout << "Case #" << z << ": " <<  "Draw" << endl ;
      else cout << "Case #" << z << ": " <<  "Game has not completed"  << endl ;



   }
     return 0;
}
