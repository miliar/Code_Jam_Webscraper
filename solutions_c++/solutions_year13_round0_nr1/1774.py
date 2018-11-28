#include <iostream>
#include <string>
using namespace std;
string s[4];
int is_won( char c )
{
  int flag;
  for( int i=0; i<4; i++ ){
    flag=1;
    for( int j=0; j<4; j++ ){
      if( s[i][j] != c && s[i][j] != 'T' ){
        flag=0; break;
      }
    }
    if( flag ) return 1;
  }
  for( int i=0; i<4; i++ ){
    flag=1;
    for( int j=0; j<4; j++ ){
      if( s[j][i] != c && s[j][i] != 'T' ){
        flag=0; break;
      }
    }
    if( flag ) return 1;
  }
  flag=1;
  for( int i=0; i<4; i++ ){
    if( s[i][i] != c && s[i][i] != 'T' ){
      flag=0; break;
    }
  }
  if( flag ) return 1;
  flag=1;
  for( int i=0; i<4; i++ ){
    if( s[i][3-i] != c && s[i][3-i] != 'T' ){
      flag=0; break;
    }
  }
  if( flag ) return 1;
  return 0;
}
int main( void )
{
  int T;
  string r;
  cin >> T;
  for( int testcase=1; testcase<=T; testcase++ ){
    getline( cin, r );
    for( int i=0; i<4; i++ ){
      getline( cin, s[i] );
    }
    r = "Game has not completed";
    if( is_won( 'X' ) ) r = "X won";
    else if( is_won( 'O' ) ) r = "O won";
    else {
      int cnt=0;
      for( int i=0; i<4; i++ )
        for( int j=0; j<4; j++ )
          if( s[i][j] == '.' ) cnt++;
      if( cnt == 0 ) r = "Draw";
    }
    cout << "Case #" << testcase << ": " << r << endl;
  }
  return 0;
}
