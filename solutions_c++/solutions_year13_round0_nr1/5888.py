#include <iostream>
#include <cstdio>
#include <map>

using namespace std;

char check_four(char a, char b, char c, char d) {
  map<char, int> player_counts;

  player_counts['T'] = 0;
  player_counts['O'] = 0;
  player_counts['X'] = 0;
  player_counts['.'] = 0;

  player_counts[a]++;
  player_counts[b]++;
  player_counts[c]++;
  player_counts[d]++;

  if (player_counts['O'] == 4 || (player_counts['O'] == 3 && player_counts['T'] == 1))
    return 'O';
  if (player_counts['X'] == 4 || (player_counts['X'] == 3 && player_counts['T'] == 1))
    return 'X';
  return 'E';
}

int main(int argc, char *argv[]) {
  int n;
  char board[4][4];

  freopen(argv[1], "r", stdin);

  cin >> n;

  for (int c = 1; c <= n; ++c) {
    cout << "Case #" << c << ": ";

    for (int i = 0; i < 4; ++i) {
      for (int j = 0; j < 4; ++j) {
        cin >> board[i][j];
      }
    }

    /*
    cout << endl;
    for (int i = 0; i < 4; ++i) {
      for (int j = 0; j < 4; ++j) {
        cout << board[i][j];
      }
      cout << endl;
    }
    */

    bool all_moves = true;
    char winner = 'E';
    char curr_player;

    // diags
    winner = check_four(board[0][0], board[1][1], board[2][2], board[3][3]);
    if (winner == 'E')
      winner = check_four(board[0][3], board[1][2], board[2][1], board[3][0]);
    for (int i = 0; i < 4 && winner == 'E'; ++i) {
      if (board[i][0] == 'T') {
        curr_player = board[i][1];
        if (board[i][2] == curr_player && board[i][3] == curr_player)
          winner = curr_player;
      }

      winner = check_four(board[i][0], board[i][1], board[i][2], board[i][3]);

      for (int j = 0; j < 4; ++j) {

        if (board[i][j] == '.') {
          all_moves = false;
          continue;
        }

        if (winner == 'E')
          winner = check_four(board[0][j], board[1][j], board[2][j], board[3][j]);
      }
    }

    if (all_moves && winner == 'E') {
      cout << "Draw";
    }
    if (!all_moves && winner == 'E') {
      cout << "Game has not completed";
    }
    if (winner != 'E')
      cout << winner << " won";
    cout << endl;
  }

  return 0;
}
