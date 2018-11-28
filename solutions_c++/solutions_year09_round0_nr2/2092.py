#include <vector>
#include <set>
#include <iostream>
#include <fstream>
using namespace std;

int htmap[100][100];
char basinmap[100][100];
int drow[] = {-1,  0, 0, 1};
int dcol[] = { 0, -1, 1, 0};

set< pair<int,int> > FindSinks(int rows, int cols) {
  set< pair<int,int> > retval;
  for(int r = 0; r < rows; r++) {
    for(int c = 0; c < cols; c++) {
      int i;
      for(i = 0; i < 4; i++) {
	if(r+drow[i] < 0 || r+drow[i] == rows || c+dcol[i] < 0 || c+dcol[i] == cols) continue;
	if(htmap[r+drow[i]][c+dcol[i]] < htmap[r][c]) break;
      }
      if(i == 4) retval.insert(pair<int,int>(r,c));
    }
  }
  return retval;
}

void UpdateHeight(int rows, int cols, int rowidx, int colidx, char &lettervalue, set< pair<int,int> > &sinks, char &cursinkletter) {
  if(basinmap[rowidx][colidx] != '?') {
    lettervalue = basinmap[rowidx][colidx];
    basinmap[rowidx][colidx] = lettervalue;
    return;
  }
  if( sinks.find( pair<int,int>(rowidx,colidx) ) != sinks.end() ) {
    lettervalue = cursinkletter;
    basinmap[rowidx][colidx] = lettervalue;
    cursinkletter+=1;
    return;
  }
  // Do stuff
  int minht = 10001, minrow = 0, mincol = 0;
  for(int i = 0; i < 4; i++) {
    if(rowidx+drow[i] < 0 || rowidx+drow[i] == rows || colidx+dcol[i] < 0 || colidx+dcol[i] == cols) continue;
    if( htmap[rowidx+drow[i]][colidx+dcol[i]] < minht ) {
      minht = htmap[rowidx+drow[i]][colidx+dcol[i]];
      minrow = rowidx+drow[i];
      mincol = colidx+dcol[i];
    }
  }
  UpdateHeight(rows, cols, minrow, mincol, lettervalue, sinks, cursinkletter);
  basinmap[rowidx][colidx] = lettervalue;
}
void CompleteBasinMap(int htmap[100][100], char basinmap[100][100], int rows, int cols) {
  memset(basinmap, '?', 100*100*sizeof(char));

  set< pair<int,int> > sinks = FindSinks(rows, cols);
  char sinkletter = 'a';
  for(int i = 0; i < rows; i++) {
    for(int j = 0; j < cols; j++) {
      char letter = '?';
      UpdateHeight(rows, cols, i, j, letter, sinks, sinkletter);
    }
  }
}
/*
void ShowMatrix(int matrix[100][100], int rows, int cols)
{
  cout << "++++++++++++++" << endl;
  for(int i = 0; i < rows; i++) {
    for(int j = 0; j < cols; j++) {
      cout << matrix[i][j] << " ";
    }
    cout << endl;
  }
  cout << "++++++++++++++" << endl;
}
*/
int main(int argc, char *argv[]) {
  if(argc < 2) return -1;
  ifstream infile(argv[1]);
  int numtestcases = 0, rows = 0, cols = 0;
  
  infile >> numtestcases;
  for(int i = 0; i < numtestcases; i++) {
    infile >> rows;
    infile >> cols;
    memset(htmap, 0, 100*100*sizeof(int));

    for(int r = 0; r < rows; r++) {
      for(int c = 0; c < cols; c++) {
	infile >> htmap[r][c];
      }
    }
    CompleteBasinMap(htmap, basinmap, rows, cols);
    
    cout << "Case #" << (i+1) << ":" << endl;
    int p, q;
    for(p = 0; p < rows; p++) {
      for(q = 0; q < cols-1; q++) {
	cout << basinmap[p][q] << " ";
      }
      cout << basinmap[p][q] << endl;
    }
  }

  return 0;

}
