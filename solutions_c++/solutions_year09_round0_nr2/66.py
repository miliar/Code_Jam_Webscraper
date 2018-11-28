#include <iostream>
#include <string.h>
#include <map>
using namespace std ;
int alt[128][128] ;
int basin[128][128] ;
const int BIG = 100000 ;
char laballoc ;
int dy[] = { 0, -1, 1, 0 } ;
int dx[] = { -1, 0, 0, 1 } ;
char blabel(int x, int y) {
  if (basin[x][y])
    return basin[x][y] ;
  int bx = -1, by = -1 ;
  for (int d=0; d<4; d++) {
    int px = x + dx[d] ;
    int py = y + dy[d] ;
    if (alt[px][py] < alt[x][y]) {
      if (bx < 0 || alt[px][py] < alt[bx][by]) {
	bx = px ;
	by = py ;
      }
    }
  }
  char r = 0 ;
  if (bx < 0) {
    r = laballoc++ ;
  } else {
    r = blabel(bx, by) ;
  }
  basin[x][y] = r ;
  return r ;
}
char lin[15000] ;
int main(int argc, char *argv[]) {
  int T, H, W ;
  fgets(lin, 15000, stdin) ;
  sscanf(lin, "%d", &T) ;
  for (int i=0; i<T; i++) {
    laballoc = 'a' ;
    fgets(lin, 15000, stdin) ;
    sscanf(lin, "%d %d", &H, &W) ;
    memset(alt, 0, sizeof(alt)) ;
    memset(basin, 0, sizeof(basin)) ;
    for (int j=0; j<H; j++) {
      alt[j+1][0] = BIG ;
      alt[j+1][W+1] = BIG ;
      fgets(lin, 15000, stdin) ;
      char *p = lin ;
      for (int k=0; k<W; k++) {
	alt[0][k+1] = BIG ;
	alt[H+1][k+1] = BIG ;
	int v = 0 ;
	while (*p && *p <= ' ')
	  p++ ;
	while (*p > ' ') {
	  v = v * 10 + *p - '0' ;
	  p++ ;
	}
	alt[j+1][k+1] = v ;
      }
    }
    cout << "Case #" << (i+1) << ":" << endl ;
    for (int j=1; j<=H; j++) {
      for (int k=1; k<=W; k++) {
	if (k > 1)
	  cout << " " ;
	cout << blabel(j, k) ;
      }
      cout << endl ;
    }
  }
}
