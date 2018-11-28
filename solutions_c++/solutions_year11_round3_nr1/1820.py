#include <iostream>
#include <fstream>

using namespace std;

//check for blue tiles
bool hasblue(char x[50][50], int R, int C) {
  if (x == NULL) {
    return false;
  }
  for (int i = 0; i < R; i++) {
    for (int j = 0; j < C; j++) {
      if (x[i][j] == '#') {
	return true;
      }
    }
  }
  return false;
}

int main (int argc, char* argv[]) {

  if (argc < 2) {
    cout << "not enough arguments" << endl;
    return -1;
  }

  ifstream input(argv[1]); // open file 

  int numcases = 0;

  if (input.bad()) {
    cout << "Bad input" << endl;
    return -2;
  }

  input >> numcases;
  
  
  // loop for each case.
  for (int i = 1; i <= numcases; i++) {
    cout << "Case #" << i << ": " << endl;
    int R = 0;
    int C = 0;
    input >> R;
    input >> C;
    
    char grid[50][50];

    //fill grid
    for (int j = 0; j < R; j++) {
      for (int k = 0; k < C; k++) {
	input >> grid[j][k];
      }
    }
    
    for (int j = 0; j < R; j++) {
      for (int k = 0; k < C;k++) {
	// if i'm at a blue tile, check surroundings
	if( grid[j][k] == '#' && j + 1 <= R && k + 1 <= C) {
	  
	  // check for other blue tiles
	  if ( grid[j+1][k] == '#' &&
	       grid[j][k+1] == '#' &&
	       grid[j+1][k+1] == '#') {
	    //replace with red!
	    grid[j][k] = '/';
	    grid[j+1][k] = '\\';
	    grid[j][k+1] = '\\';
	    grid[j+1][k+1] = '/';
	  }


	}
      }
    }

    if (hasblue(grid, R, C)) {
      cout << "Impossible" << endl;
      continue;
    }

    for (int j = 0; j < R; j++) {
      for (int k = 0; k < C; k++) {
	cout << grid[j][k];
      }
      cout << endl;
    }
  } // end case loop

  return 0;
}
