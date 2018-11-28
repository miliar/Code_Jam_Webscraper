#include <iostream>
#include <fstream>
using namespace std;
int** map;
char** basins;
int rows, cols;
char basin;
int sink[2];

void find(int x, int y) { //find sink for cell x,y
  int N = (y == 0) ? 10001 : map[y-1][x];
  int S = (y == rows - 1) ? 10001 : map[y+1][x];
  int W = (x == 0) ? 10001 : map[y][x-1];
  int E = (x == cols - 1) ? 10001 : map[y][x+1];
  int X = map[y][x];
  if(N >= X && S >= X && W >= X && E >= X) {
    sink[0] = x;
    sink[1] = y;
    return;
  }
  if(W < N) {
    if(S < E) {
      if(S < W) {
	find(x, y+1);
      } else {
	find(x-1, y);
      }
    } else {
      if(E < W) {
	find(x + 1, y);
      } else {
	find(x-1, y);
      }
    }
  } else {
    if(S < E) {
      if(S < N) {
	find(x, y+1);
      } else {
	find(x, y-1);
      }
    } else {
      if(E < N) {
	find(x + 1, y);
      } else {
	find(x, y-1);
      }
    }
  }
}

void label(int x, int y, int a, int b) { //second pair is target cell
  if (a < 0 || b < 0 || a > cols -1 || b > rows -1 || basins[b][a] != '.') {
    return;
  }
  int N = (b == 0) ? 10001 : map[b-1][a];
  int S = (b == rows - 1) ? 10001 : map[b+1][a];
  int W = (a == 0) ? 10001 : map[b][a-1];
  int E = (a == cols - 1) ? 10001 : map[b][a+1];
  int X = map[b][a];
  if(N >= X && S >= X && W >= X && E >= X) {
    return;
  }
  if((x == a && y == b-1 && N <= S && N <= W && N <= E) ||
     (x == a && y == b+1 && S < N && S < W && S < E) ||
     (x == a-1 && y == b && W < N && W <= E && W <= S) ||
     (x == a+1 && y == b && E < N && E < W && E <=S)) {
    basins[b][a] = basin;
    label(a, b, a, b - 1);
    label(a, b, a, b + 1);
    label(a, b, a - 1, b);
    label(a, b, a + 1, b);
    map[b][a] = 10001;
  }
}


int main(int argc, char** argv) {
  ifstream input;
  ofstream output;
  input.open(argv[1]);
  output.open(argv[2]);
  int T;
  input >> T;
  for(int k = 0; k < T; k++) {
    output << "Case #" << k + 1 << ":" << endl;
    input >> rows;
    input >> cols;
    map = new int*[rows];
    basins = new char*[rows];
    for(int i = 0; i < rows; i++) {
      map[i] = new int[cols];
      basins[i] = new char[cols];
      for(int j = 0; j < cols; j++) {
	basins[i][j] = '.';
	input >> map[i][j]; 
      }
    }
    basin = 'a';
    //compute
    for(int i = 0; i < rows; i++) {
      for(int j = 0; j < cols; j++) {
	if(basins[i][j] == '.') {
	  find(j, i);
	  label(sink[0], sink[1], sink[0] + 1, sink[1]);
	  label(sink[0], sink[1], sink[0] - 1, sink[1]);
	  label(sink[0], sink[1], sink[0], sink[1] + 1);
	  label(sink[0], sink[1], sink[0], sink[1] - 1);
	  basins[sink[1]][sink[0]] = basin;
	  basin++;
	}
      }
    }

    //cleanup
    for(int i = 0; i < rows; i++) {
      delete[] map[i];
      for(int j = 0; j < cols; j++) {
	output << basins[i][j] << ' ';
      }
      output << endl;
      delete[] basins[i];
    }
    delete[] map;
    delete[] basins;
  }
  input.close();
  output.close();
}
