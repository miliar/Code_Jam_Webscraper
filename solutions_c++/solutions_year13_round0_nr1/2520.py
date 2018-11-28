#include <cstdio>
#include <cstring>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main () {
	int T;
  vector<string> board;
  string answers[4] = {"X won", "O won", "Draw", "Game has not completed"};

	freopen("A-small-attempt0.in", "r", stdin);
	freopen("a.out", "w", stdout);

	scanf_s("%d", &T);
	for (int t = 1; t <= T; t++) {
    string input_string;
    bool empty_cell_exist = false;
    int who_won = -1;
		board.clear();
    for (int i = 0; i < 4; i++) {
      cin >> input_string;
			board.push_back(input_string);
		}

    int i, j;
    for (i = 0; i < 4; i++) for (j = 0; j < 4; j++) {
      if (board[i][j] == '.') {
        empty_cell_exist = true;
        break;
      }
    }

    // horizontal
    for (i = 0; i < 4; i++) {
			char pivot = board[i][0];
			if (pivot == 'T') pivot = board[i][1];
      for (j = 0; j < 4; j++) {
        if (!(board[i][j] == 'T' || board[i][j] == 'T') &&
            board[i][j] != pivot) break;
      }
      if (j == 4) {
        if (pivot == 'X') {
          who_won = 0;
        } else if (pivot == 'O') {
          who_won = 1;
        }
      }
    }

    // vertical
    for (i = 0; i < 4; i++) {
			char pivot = board[0][i];
			if (pivot == 'T') pivot = board[1][i];
      for (j = 0; j < 4; j++) {
        if (!(board[j][i] == 'T' || board[j][i] == 'T') &&
            board[j][i] != pivot) break;
      }
      if (j == 4) {
        if (pivot == 'X') {
          who_won = 0;
        } else if (pivot == 'O') {
          who_won = 1;
        }
      }
    }

		char pivot = board[0][0];
		if (pivot == 'T') pivot = board[1][1];
    // diagonal '\'
    for (i = 0; i < 4; i++) {
			if (!(board[i][i] == 'T' || board[i][i] == 'T') &&
				board[i][i] != pivot) break;
		}
		if (i == 4) {
			if (pivot == 'X') {
				who_won = 0;
			} else if (pivot == 'O') {
				who_won = 1;
			}
		}

		pivot = board[0][3];
		if (pivot == 'T') pivot = board[1][1];
    // diagonal '/'
    for (i = 0; i < 4; i++) {
			if (!(board[i][3 - i] == 'T' || board[i][3 - i] == 'T') &&
				board[i][3 - i] != pivot) break;
		}
		if (i == 4) {
			if (pivot == 'X') {
				who_won = 0;
			} else if (pivot == 'O') {
				who_won = 1;
			}
		}


    printf("Case #%d: ", t);
    if (who_won != -1) {
      printf("%s\n", answers[who_won].c_str());
    } else if (empty_cell_exist) {
      printf("%s\n", answers[3].c_str());
    } else {
      printf("%s\n", answers[2].c_str());
    }
	}

	return 0;
}
