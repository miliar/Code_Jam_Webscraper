#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>

using namespace std;

int main() {
  ifstream fin ("A.in");
  ofstream fout ("A.out");

  int numTimes;
  fin >> numTimes;
  for (int turn = 1; turn <= numTimes; turn++) {
    int R, C;
    fin >> R >> C;

    char** array;
    array = new char*[R];
    for (int i = 0; i < R; i++) {
      array[i] = new char[C];
      string line;
      fin >> line;
      for (int j = 0; j < C; j++) {
        array[i][j] = line[j];
      }
    }

      bool fail = false;
      for (int i = 0; i < R; i++) {
        if (fail) break;
        for (int j = 0; j < C; j++) {
          char now = array[i][j];
          if (now == '#') {
            if (i == (R-1) || j == (C-1)) {
              fail = true;
              break;
            }
            if ((array[i][j+1] == '#') && (array[i+1][j] == '#') && (array[i+1][j+1] == '#')) {
              array[i][j] = '/';
              array[i][j+1] = '\\';
              array[i+1][j] = '\\';
              array[i+1][j+1] = '/';
            }
            else {
              fail = true;
              break;
            }
          }
        }
      }
    fout << "Case #" << turn << ":" << endl;
    if (fail) fout << "Impossible" << endl;
    else {
      for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
          fout << array[i][j];
        }
        fout << endl;
      }
    }
  }
}
