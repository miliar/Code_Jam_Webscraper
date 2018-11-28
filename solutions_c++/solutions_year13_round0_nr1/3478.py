#include <iostream>
#include <string>

using namespace std;

bool is_X( char c ) { return c == 'X' || c == 'T'; }
bool is_O( char c ) { return c == 'O' || c == 'T'; }

int main( ) {
  freopen( "input.txt", "r", stdin );
  freopen( "output.txt", "w", stdout );
  
  int T, dots;
  string board[ 4 ];
  cin >> T;
  
  for( int cs = 1; cs <= T; ++cs ) {
    dots = 0;
    
    for( int i = 0; i < 4; ++i ) {
      cin >> board[ i ];
      if( board[ i ].find( '.' ) != string::npos ) dots = 1;
    }
    
    bool x_won = false;
    for( int i = 0; i < 4; ++i ) {
      bool row_won = true;
      bool col_won = true;
      
      for( int j = 0; j < 4; ++j ) {
        if( !is_X( board[ i ][ j ] ) ) col_won = false;
        if( !is_X( board[ j ][ i ] ) ) row_won = false;
      }
      
      if( row_won || col_won ) {
        x_won = true;
        break;
      }
    }
    
    if( !x_won ) {
      bool main_dig_1_won = true;
      bool main_dig_2_won = true;
      
      for( int i = 0; i < 4; ++i ) {
        if( !is_X( board[ i ][ i ] ) ) main_dig_1_won = false;
        if( !is_X( board[ i ][ 4-i-1 ] ) ) main_dig_2_won = false;
      }
      
      if( main_dig_1_won || main_dig_2_won ) {
        x_won = true;
      }
    }
    
    bool o_won = false;
    for( int i = 0; i < 4; ++i ) {
      bool row_won = true;
      bool col_won = true;
      
      for( int j = 0; j < 4; ++j ) {
        if( !is_O( board[ i ][ j ] ) ) col_won = false;
        if( !is_O( board[ j ][ i ] ) ) row_won = false;
      }
      
      if( row_won || col_won ) {
        o_won = true;
        break;
      }
    }
    
    if( !o_won ) {
      bool main_dig_1_won = true;
      bool main_dig_2_won = true;
      
      for( int i = 0; i < 4; ++i ) {
        if( !is_O( board[ i ][ i ] ) ) main_dig_1_won = false;
        if( !is_O( board[ i ][ 4-i-1 ] ) ) main_dig_2_won = false;
      }
      
      if( main_dig_1_won || main_dig_2_won ) {
        o_won = true;
      }
    }
    
    cout << "Case #" << cs << ": ";
    
    if( x_won ) cout << "X won\n";
    else if( o_won ) cout << "O won\n";
    else if( dots ) cout << "Game has not completed\n";
    else cout << "Draw\n";
  }
  
  return 0;
}
        
    
    
  