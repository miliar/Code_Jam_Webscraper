#include <iostream>
#include <cstdio>

using namespace std;

void doit () {
  int r, c;
  cin >> r >> c;
  char tiles[r][c];
  for(int i = 0; i < r; ++i) {
    for(int j = 0; j < c; ++j) {
      cin >> tiles[i][j];
    }
  }

  for(int i = 0; i < r; ++i) {
    for(int j = 0; j < c; ++j) {
      if(tiles[i][j] == '#') {
	if( i < (r-1)
	    && j < (c-1)
	    && tiles[i+1][j] == '#'
	    && tiles[i][j+1] == '#'
	    && tiles[i+1][j+1] == '#') {
	  tiles[i][j] = '/';
	  tiles[i][j+1] = '\\';
	  tiles[i+1][j] = '\\';
	  tiles[i+1][j+1] = '/';
	} else {
	  cout << "Impossible" << endl;
	  return;
	}
      }
    }}
  for(int i = 0; i < r; ++i) {
    for(int j = 0; j < c; ++j) {
      cout << tiles[i][j];
    }
    cout  << endl;
  }
}

int main() {
  int t;
  cin >> t;
  for(int i = 0; i < t; ++i) {
    cout << "Case #" << i+1 << ":" << endl;
    doit ();
  }
}
