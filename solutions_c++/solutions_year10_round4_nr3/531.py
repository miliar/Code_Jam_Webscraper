#include <iostream>
#include <vector>
#include <string>
using namespace std;

struct Rect {
  int x1, y1, x2, y2;
};

int solve(void)
{
  int R;
  cin >> R;
  vector<Rect> bact(R);
  for( int i = 0 ; i < R ; ++i )
    cin >> bact[i].x1 >> bact[i].y1 >> bact[i].x2 >> bact[i].y2;
  int w = 0, h = 0;
  for( int i = 0 ; i < R ; ++i ) {
    if( w < bact[i].x2 ) w = bact[i].x2;
    if( h < bact[i].y2 ) h = bact[i].y2;
  }

  vector<string> bac(h, string(w, 'x'));
  for( int i = 0 ; i < R ; ++i ) {
    for( int y = bact[i].y1 - 1 ; y < bact[i].y2 ; ++y )
      for( int x = bact[i].x1 - 1 ; x < bact[i].x2 ; ++x )
        bac[y][x] = 'o';
  }

  int gen = 0;
  for( bool cont = true ; cont ; ++gen ) {
    for( int y = h - 1 ; y >= 0 ; --y ) {
      for( int x = w - 1 ; x >= 0 ; --x ) {
        bool a = ( x > 0 && bac[y][x-1] == 'o' );
        bool b = ( y > 0 && bac[y-1][x] == 'o' );
        if( a && b ) bac[y][x] = 'o';
        else if( !a && !b ) bac[y][x] = 'x';
      }
    }
    //for( int i = 0 ; i < h ; ++i ) cout << bac[i] << "\n"; cout << "\n";
    // Check
    cont = false;
    for( int i = 0 ; i < h ; ++i ) {
      if( bac[i].find('o') != string::npos ) {
        cont = true;
        break;
      }
    }
  }

  return gen;
}

int main(void)
{
  int C;
  cin >> C;
  for( int c = 1 ; c <= C ; ++c ) {
    cerr << "Case #" << c << "\n";
    cout << "Case #" << c << ": " << solve() << "\n";
  }
  return 0;
}
