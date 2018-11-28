#include <cstdio>

char grid[5][5];
int x = 0;
int o = 0;
int cases = 1;
bool ok = 0;

void f1( int k ){
     x = 0;
     o = 0;
     for( int i = 0; i < 4; ++i ){
      if( grid[k][i] == 'X' || grid[k][i] == 'T' ) ++x;
      if( x == 4 ){ printf( "Case #%d: X won\n", cases ); ++cases; ok = 1;  return; }
     }
     for( int i = 0; i < 4; ++i ){
      if( grid[k][i] == 'O' || grid[k][i] == 'T' ) ++o;
      if( o == 4 ){ printf( "Case #%d: O won\n", cases ); ++cases; ok = 1; return; }
     }
}
void f2( int k ){
     x = 0;
     o = 0;
     for( int i = 0; i < 4; ++i ){
      if( grid[i][k] == 'X' || grid[i][k] == 'T' ) ++x;
      if( x == 4 ){ printf( "Case #%d: X won\n", cases ); ++cases;ok = 1; return; }
     }
     for( int i = 0; i < 4; ++i ){
      if( grid[i][k] == 'O' || grid[i][k] == 'T' ) ++o;
      if( o == 4 ){ printf( "Case #%d: O won\n", cases ); ++cases;ok = 1; return; }
     }
}
void f3(){
     x = o = 0;
     for( int i = 0; i < 4; ++i ){
      if( grid[i][i] == 'X' || grid[i][i] == 'T' ) ++x;
      if( x == 4 ){ printf( "Case #%d: X won\n", cases ); ++cases; ok = 1;return; }
     }
     for( int i = 0; i < 4; ++i ){
      if( grid[i][i] == 'O' || grid[i][i] == 'T' ) ++o;
      if( o == 4 ){ printf( "Case #%d: O won\n", cases ); ++cases;ok = 1; return; }
     }
}
void f4(){
      x = o = 0;
     for( int i = 3; i >= 0; --i ){
      if( grid[4-i-1][i] == 'X' || grid[4-i-1][i] == 'T' ) ++x;
      if( x == 4 ){ printf( "Case #%d: X won\n", cases ); ++cases;ok = 1; return; }
     }
     for( int i = 3; i >= 0; --i ){
      if( grid[4-i-1][i] == 'O' || grid[4-i-1][i] == 'T' ) ++o;
      if( o == 4 ){ printf( "Case #%d: O won\n", cases ); ++cases;ok = 1; return; }
     }
}


int main (){
    int t; scanf ( "%d", &t );
    for( ; t; --t ){
      x = o = 0;
      ok = 0;
      int tocka = 0;
      for( int i = 0; i < 4; ++i ){
        scanf( "%s", grid[i] );
        for( int j = 0; j < 4; ++j ){
          if( grid[i][j] == '.' ) tocka = 1;
        }
      }
      
      for( int i = 0; i < 4; ++i ){
       f1(i);
       if(ok) break;   
       f2(i);     
       if(ok) break;
      }
      f3();
      f4();
      
      if( !tocka && !ok ){ printf( "Case #%d: Draw\n", cases ); ++cases; continue; }
      if( tocka && !ok ) { printf( "Case #%d: Game has not completed\n", cases ); ++cases; continue; }
      
     }

     return 0;
}
