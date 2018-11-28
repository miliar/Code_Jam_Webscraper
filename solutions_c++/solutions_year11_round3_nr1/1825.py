#include <iostream>

using namespace std;

int main () {
  char grid[102][102];

  unsigned int x_diff[3] = {1, 0, 1};
  unsigned int y_diff[3] = {0, 1, 1};
  char diamond[3] = {'\\', '\\', '/'};

  unsigned int T, R, C;

  //get the number of test cases
  cin >> T;

  for (unsigned int i = 0; i < T; ++i) {
    bool status = true;
    cin >> R >> C;
    
    //clear all characters
    for (unsigned int j = 1; j <= R+2; ++j)
      for (unsigned int k = 1; k <= C+2; ++k)
	grid[j][k] = '.';
    
    //read in the grid
    for (unsigned int j = 1; j <= R; ++j)
      for (unsigned int k = 1; k <= C; ++k)
	cin >> grid[j][k];

    //transform into diamond
    for (unsigned int j = 1; j <= R && status; ++j) {
      for (unsigned int k = 1; k <= C && status; ++k) {
	if (grid[j][k] != '#')
	  continue;

	grid[j][k] = '/';
	for (unsigned int x = 0; x < 3 && status; ++x) {
	  if (grid[j+y_diff[x]][k+x_diff[x]] == '#')
	    grid[j+y_diff[x]][k+x_diff[x]] = diamond[x];
	  else
	    status = false;
	}
      }
    }

    //display result
    cout <<"Case #"<<i+1<<":\n";
    if (!status)
      cout <<"Impossible\n";
    else {
      for (unsigned int j = 1; j <= R; ++j) {
	for (unsigned int k = 1; k <= C; ++k) {
	  cout <<grid[j][k];
	}
	cout <<"\n";
      }
    }
  }

  return 0;
}
