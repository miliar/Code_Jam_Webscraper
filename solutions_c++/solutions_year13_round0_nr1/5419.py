// Tic-Tac-Toe-Tomek

#include <vector>
#include <iostream>
#include <string>

using namespace std;

#define for0(i,l) for(int i = 0; i < (l); ++i)

int main () {
  int T;
  cin >> T;
  for0(t,T) {
    vector < string > b (4, "");
    for0(i,4)
      cin >> b[i] >> ws;

    bool draw = true;
    char won = 'D';
    
    // horizontal
    for0(i,4) {
      char first = b[i][0];
      if (first == 'T')
        first = b[i][1];
      int line_count = 0;
      for0(j,4) {
        if (b[i][j] == 'T' || (b[i][j] == first && b[i][j] != '.'))
          line_count++;
        else if (first == '.')
          draw = false;
      }
      if (line_count == 4)
        won = first;
    }
        
    // vertical
    for0(i,4) {
      char first = b[0][i];
      if (first == 'T')
        first = b[1][i];
      int line_count = 0;
      for0(j,4) {
        if (b[j][i] == 'T' || (b[j][i] == first && b[j][i] != '.'))
          line_count++;
        else if (first == '.')
          draw = false;
      }
      if (line_count == 4)
        won = first;
    }

    if (won == 'D') {
      int i = 0; int j = 0;
      char first = b[0][0];
      if (first == 'T')
        first = b[1][1];
      int line_count = 0;
      for0(k,4) {
        if (b[i+k][j+k] == 'T' || (b[i+k][j+k] == first && b[i+k][j+k] != '.'))
          line_count++;
      }
      if (line_count == 4)
        won = first;
    }
        
    if (won == 'D') {
      int i = 0; int j = 3;
      char first = b[0][3];
      if (first == 'T')
        first = b[1][2];
      int line_count = 0;
      for0(k,4) {
        if (b[i+k][j-k] == 'T' || (b[i+k][j-k] == first && b[i+k][j-k] != '.'))
          line_count++;
      }
      if (line_count == 4)
        won = first;
    }

    cout << "Case #" << t+1 << ": ";
    if (won == 'D' && draw)
      cout << "Draw" << endl;
    else if (won == 'D' && !draw)
      cout << "Game has not completed" << endl;
    else
      cout << won << " won" << endl;
  }
}

