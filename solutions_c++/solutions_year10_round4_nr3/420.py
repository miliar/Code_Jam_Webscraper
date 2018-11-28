#include<iostream>
#include<string>
#include<cstring>
using namespace std;

int ncases;
int board[110][110];
int R, x1, x2, y1, y2;
int tim;

bool wasAlive( int x, int y ){
  return ( board[x][y] > 0 && board[x][y] < tim );
}

int predAlive( int x, int y ){
  return ( wasAlive(x-1,y) ? 1 : 0 ) + ( wasAlive(x,y-1) ? 1 : 0 );
}

int simulate(){
  int remaining = 0;
  for( int x=100; x>=1; x-- ){
    for( int y=100; y>=1; y-- ){
      if( wasAlive( x,y ) ){
	if( predAlive( x,y ) > 0 ){
	  remaining++;
	} else {
	  board[x][y] = 0;
	}
      } else {
	if( predAlive( x,y ) == 2 ){
	  board[x][y] = tim;
	  remaining++;
	}
      }
    }
  }
  return remaining;
}

int main(){
  cin >> ncases;
  for( int ncase=1; ncase<=ncases; ncase++ ){
    memset( board, 0, sizeof( board ) );
    cin >> R;
    for( int r=0; r<R; r++ ){
      cin >> x1 >> y1 >> x2 >> y2;
      for( int x=x1; x<=x2; x++ ){
	for( int y=y1; y<=y2; y++ ){
	  board[x][y] = 1;
	}
      }
    }
    tim = 2;
    while( simulate() > 0 ){
      tim++;
    }
    cout << "Case #" << ncase << ": " << tim-1 << endl;
  }

}
