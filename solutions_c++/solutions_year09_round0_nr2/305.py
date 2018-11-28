// 2009/09/03 Naoyuki Hirayama

#include <iostream>
#include <string>
#include <vector>

static int alt[100][100];
static int basin[100][100];

int main() {
  int T; // number of maps
  std::cin >> T;

  for( int i = 0 ; i < T ; i++ ) {
    int H, W; // height and width
    std::cin >> H >> W;
    for( int y = 0 ; y < H ; y++ ) {
      for( int x = 0 ; x < W ; x++ ) {
        std::cin >> alt[y][x];
        basin[y][x] = 0;
      }
    }

    int label = 1;
    for( int y = 0 ; y < H ; y++ ) {
      for( int x = 0 ; x < W ; x++ ) {
        int a = alt[y][x];
        if( (0 < y && alt[y-1][x] < a) ||
            (0 < x && alt[y][x-1] < a) ||
            (x < W-1 && alt[y][x+1] < a) ||
            (y < H-1 && alt[y+1][x] < a) ) {
          continue; // not sink
        }
        basin[y][x] = label++;
      }
    }

    int blank;

 retry:
    blank = 0;
    for( int y = 0 ; y < H ; y++ ) {
      for( int x = 0 ; x < W ; x++ ) {
        if( 0 < basin[y][x] ) { continue; }
        int lowest = alt[y][x];
        int yy = -1;
        int xx = -1;
        if(0 < y && alt[y-1][x] < lowest) {
          lowest = alt[y-1][x];
          yy = y-1; xx = x;
        }
        if(0 < x && alt[y][x-1] < lowest) {
          lowest = alt[y][x-1];
          yy = y; xx = x-1; 
        }
        if(x < W-1 && alt[y][x+1] < lowest) {
          lowest = alt[y][x+1]; 
          yy = y ; xx = x+1;
        }
        if(y < H-1 && alt[y+1][x] < lowest) {
          lowest = alt[y+1][x];
          yy = y+1; xx = x;
        }
        // std::cerr << y << ", " << x << ": " << yy << ", " << xx << ", " << lowest << std::endl;
        if( lowest < alt[y][x] ) {
          assert( 0 <= xx && 0 <= yy );
          basin[y][x] = basin[yy][xx];
        }
        if( basin[y][x] == 0 ) { blank++; }
      }
    }
    if( 0 < blank ) { goto retry; }

    int charmap[26] = { 0 }; 
    int c = 'a';

    std::cout << "Case #" << (i+1) << ": " << std::endl;
    for( int y = 0 ; y < H ; y++ ) {
      for( int x = 0 ; x < W ; x++ ) {
        int k = basin[y][x] - 1;
        if( charmap[k] == 0 ) {
          charmap[k] = c++;
        }
        std::cout << (char)(charmap[k]);
        if( x < W-1) { std::cout << ' '; }
      }
      std::cout << std::endl;
    }
  }
}
