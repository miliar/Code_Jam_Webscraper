#include <string>
#include <iostream>
using namespace std;

int T;
int N,K;
char grid[55][55];
bool redWins, blueWins;
int dr[8] = {0,-1,-1,-1,0,1,1,1};
int dc[8] = {1,1,0,-1,-1,-1,0,1};

void scan( int r, int c, int d ){
  char prev = 'X';
  int streak = 0;
  while( (r < N) && (r >= 0) && (c < N) && (c >= 0) ){
    if( grid[r][c] == '.' ){
      streak = 0;
    } else {
      if( grid[r][c] == prev ){
	streak++;
	//cout << "streak of " << streak << " for " << prev << endl;
	if( streak >= K ){
	  if( prev == 'B' ){
	    blueWins = true;
	  } else if( prev == 'R' ){
	    redWins = true;
	  }
	}
      } else {
	streak = 1;
      }
    }
    prev = grid[r][c];
    r += dr[d];
    c += dc[d];
  }
}

int main(){
  cin >> T;
  for( int t=1; t<=T; t++ ){
    memset( grid, '.', sizeof( grid ) );
    cin >> N >> K;
    for( int i=0; i<N; i++ ){
      for( int j=0; j<N; j++ ){
	cin >> grid[i][j];
      }
    }
    // [sandy] shove to the right
    for( int r=0; r<N; r++ ){
      int write = N-1;
      for( int read=N-1; read >= 0; read-- ){
	if( grid[r][read] == 'R' || grid[r][read] == 'B' ){
	  char temp = grid[r][read];
	  grid[r][read] = '.';
	  grid[r][write] = temp;
	  write--;
	}
      }
    }
    /*for( int i=0; i<N; i++ ){
      for( int j=0; j<N; j++ ){
	cout << grid[i][j];
      }
      cout << endl;
      }*/
    redWins = false;
    blueWins = false;
    for( int r=0; r<N; r++ ){
      scan( r, 0, 0 );
      scan( r, 0, 1 );
      scan( r, 0, 7 );
    }
    for( int c=0; c<N; c++ ){
      scan( 0, c, 6 );
      scan( 0, c, 7 );
      scan( N-1, c, 1 );
    }
    string wins = "Neither";
    if( redWins ){
      if( blueWins ){
	wins = "Both";
      } else {
	wins = "Red";
      }
    } else if( blueWins ){
      wins = "Blue";
    }
    cout << "Case #" << t << ": " << wins << endl;
  }

}


