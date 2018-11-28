#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char** argv) {

  if (argc < 2) {
    //cerr << "You should provide an input file" << endl;
    return 1;
  }

  ifstream myfile(argv[1]);
  if (!myfile.is_open()) {
    //cerr << "Cannot open file" << endl;
    return 1;
  }

  int nb_tests;
  myfile >> nb_tests;

  for (int test_i = 1; test_i <= nb_tests; test_i++) {
    // Read input data
    char game[4][4];
    for (int i = 0; i < 4; i++) {
      string line;
      myfile >> line;
      for (int j = 0; j < 4; j++) {
        game[i][j] = line[j];
        //cout << line[j];
      }
      //cout << endl;
    }

    // Solve it
    bool winO = false, winX = false;
    for (int x = 0; x < 4; x++) {
      for (int y = 0; y < 4; y++) {
        char player = game[x][y];
        if (player == '.') {
          // Not a player
          continue;
        }
        if (player == 'O' and winO ||
          player == 'X' and winX) {
          // Already won
          continue;
        }

        // Check if winner:
        bool win = false;
        // 1/ vertical
        if (x < 1) {
          char player2 = (player == 'T' ? game[x+1][y] : player);
          if (player2 != '.') {
          bool win2 =
            (game[x+1][y] == player2 || game[x+1][y] == 'T') &&
            (game[x+2][y] == player2 || game[x+2][y] == 'T') &&
            (game[x+3][y] == player2 || game[x+3][y] == 'T');
          win |= win2;
          if (win2 && player == 'T') {
            player = player2;
          }
          }
        }
        // 2/ horizontal
        if (y < 1) {
          char player2 = (player == 'T' ? game[x][y+1] : player);
          if (player2 != '.') {
          bool win2 =
            (game[x][y+1] == player2 || game[x][y+1] == 'T') &&
            (game[x][y+2] == player2 || game[x][y+2] == 'T') &&
            (game[x][y+3] == player2 || game[x][y+3] == 'T');
          win |= win2;
          if (win2 && player == 'T') {
            player = player2;
          }
          }
        }
        // 3/ diagonal
        if (x < 1 && y < 1) {
          char player2 = (player == 'T' ? game[x+1][y+1] : player);
          if (player2 != '.') {
          bool win2 =
            (game[x+1][y+1] == player2 || game[x+1][y+1] == 'T') &&
            (game[x+2][y+2] == player2 || game[x+2][y+2] == 'T') &&
            (game[x+3][y+3] == player2 || game[x+3][y+3] == 'T');
          win |= win2;
          if (win2 && player == 'T') {
            player = player2;
          }
          }

        }
        // 4/ other diagonal
        if (x >= 3 && y < 1) {
          //cerr << player << endl;
          char player2 = (player == 'T' ? game[x-1][y+1] : player);
          if (player2 != '.') {
          bool win2 =
            (game[x-1][y+1] == player2 || game[x-1][y+1] == 'T') &&
            (game[x-2][y+2] == player2 || game[x-2][y+2] == 'T') &&
            (game[x-3][y+3] == player2 || game[x-3][y+3] == 'T');
          //cerr << game[x][y] << (game[x-1][y+1]) << game[x-2][y+2] << game[x-3][y+3] << endl;
          win |= win2;
          //cerr << "player: " << player << "=player2: " << player2 << endl;
          if (win2 && player == 'T') {
            player = player2;
          }
          }
        }


        if (win) {
          if (player == 'O') {
            winO = true;
            //cerr << "winO = true" << endl;
          } else if (player == 'X') {
            winX = true;
          }
        }
      }
    }
    cout << "Case #" << test_i << ": ";
    if (winX and winO) {
      cout << "Draw";
    } else if (winX) {
        cout << "X won";
    } else if (winO) {
        cout << "O won";
    } else {
      // TODO check if is full
      bool full = true;
      for (int x = 0; x < 4; x++) {
        for (int y = 0; y < 4; y++) {
          if (game[x][y] == '.') {
            full = false;
          }
        }
      }
      if (full) {
        cout << "Draw";
      } else {
        cout << "Game has not completed";
      }
    }
    cout << endl;

  }

  return 0;
}
