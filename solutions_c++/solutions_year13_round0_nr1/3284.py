#include <iostream>
#include <fstream>

using namespace std;

char board[4][4];

int Four_In_A_Row(char ch);

int main() {
  for(int i = 0; i < 4; i++) {
    for (int j = 0; j < 4; j++) {
      board[i][j] = 0;
    }
  }

  ifstream infile;
  ofstream outfile;
  infile.open("test.txt");
  if(infile.fail()) {
    cout << "Didn't work" << endl;
  } else {
    cout << "Opened" << endl;
  }

  outfile.open("Codejamtest.txt");
  if(outfile.fail()) {
    cout << "Didn't work" << endl;
  } else {
    cout << "Opened" << endl;
  }

  int num_tests, empty_dot_bool; // bool is 1 if there, 0 if not
  infile >> num_tests;

  for(int i = 0; i < num_tests; i++) {
    empty_dot_bool = 0;
    for(int m = 0; m < 4; m++) {
      for(int n = 0; n < 4; n++) {
	infile >> board[m][n];
	if(board[m][n] == '.') {
	  empty_dot_bool = 1;
	}
      }
    }

    if(Four_In_A_Row('X')) {
      outfile << "Case #"<< i + 1  << ": X won" << endl;
    } else if (Four_In_A_Row('O')) {
      outfile << "Case #"<< i + 1  << ": O won" << endl;      
    } else if (empty_dot_bool != 0) {
      outfile << "Case #" << i + 1 << ": Game has not completed" << endl;
    } else {
      outfile << "Case #" << i + 1 << ": Draw" << endl;
    }
  }
}

int Four_In_A_Row(char ch) {
  int counter = 0;
  for(int i = 0; i < 4; i++) {
    for(int j = 0; j < 4; j++) {
      if(board[i][j] == ch || board[i][j] == 'T') {
	counter++;
      } else {
	break;
      }
    }
    if(counter == 4) {
      return 1;
    }
    counter = 0;
  }


  for(int i = 0; i < 4; i++) {
    for(int j = 0; j < 4; j++) {
      if(board[j][i] == ch || board[j][i] == 'T') {
	counter++;
      } else {
	break;
      }
    }
    if(counter == 4) {
      return 1;
    }
    counter = 0;
  }

  for(int i = 0; i < 4; i++) {
    if(board[i][i] == ch || board[i][i] == 'T') {
	counter++;
    } else {
       break;
    }
    if(counter == 4) {
      return 1;
    }
  }
  counter = 0;

  for(int i = 0; i < 4; i++) {
    if(board[3 - i][i] == ch || board[3 - i][i] == 'T') {
	counter++;
    } else {
       break;
    }
    if(counter == 4) {
      return 1;
    }
  }

  return 0;
}
