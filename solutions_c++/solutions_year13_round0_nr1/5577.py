#include<iostream>
#include<string>
#include<vector>

using namespace std;

void verify(vector<string> board);

int main(int argv, char **argc) {
  int t;
  vector<string> board;

  cin >> t;

  for (int i = 0; i < t; ++i) {
    board.clear();
    for (int j = 0; j < 4; ++j) {
      string x;
      cin >> x;
      board.push_back(x);
    }

    cout << "Case #" << i+1 << ": ";
    verify(board);
  }

  return 0;
}

void verify(vector<string> board) {
  bool contains_empty = false;
  // Rows
  for(int i = 0; i < 4; ++i) {
    string row = board[i];
    int match = 0;
    char thischar = '\0';

    for (int j = 0; j < 4; ++j) {
      if (row[j] == '.') {
        contains_empty = true;
        break;
      } else if (row[j] == 'T') {
        // Wild card
        match++;
      } else if (thischar == '\0') {
        // Set first char
        thischar = row[j];
        match++;
      } else if (thischar == row[j]) {
        match++;
      } else {
        //Mismatch, skip row
        break;
      }
    }

    if (match == 4) {
      cout << thischar << " won" << endl;
      return;
    }
  }

  //Columns
  for(int i = 0; i < 4; ++i) {
    int match = 0;
    char thischar = '\0';

    for (int j = 0; j < 4; ++j) {
      if (board[j][i] == '.') {
        contains_empty = true;
        break;
      } else if (board[j][i] == 'T') {
        // Wild card
        match++;
      } else if (thischar == '\0') {
        // Set first char
        thischar = board[j][i];
        match++;
      } else if (thischar == board[j][i]) {
        match++;
      } else {
        //Mismatch, skip row
        break;
      }
    }

    if (match == 4) {
      cout << thischar << " won" << endl;
      return;
    }
  }

  // Diagonals
  int match = 0;
  char thischar = '\0';
  for (int i = 0; i < 4; ++i) {
    if (board[i][i] == '.') {
      contains_empty = true;
      break;
    } else if (board[i][i] == 'T') {
      // Wild card
      match++;
    } else if (thischar == '\0') {
      // Set first char
      thischar = board[i][i];
      match++;
    } else if (thischar == board[i][i]) {
      match++;
    } else {
      //Mismatch, skip row
      break;
    }
  }
  if (match == 4) {
    cout << thischar << " won" << endl;
    return;
  }
  
  match = 0;
  thischar = '\0';
  for (int i = 0; i < 4; ++i) {
    if (board[3 - i][i] == '.') {
      contains_empty = true;
      break;
    } else if (board[3 - i][i] == 'T') {
      // Wild card
      match++;
    } else if (thischar == '\0') {
      // Set first char
      thischar = board[3 - i][i];
      match++;
    } else if (thischar == board[3 - i][i]) {
      match++;
    } else {
      //Mismatch, skip row
      break;
    }
  }
  if (match == 4) {
    cout << thischar << " won" << endl;
    return;
  }


  if (contains_empty) {
    cout << "Game has not completed" << endl;
    return;
  }

  cout << "Draw" << endl;
  return;
}
