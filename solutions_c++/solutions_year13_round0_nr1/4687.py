#include <cstdio>
#include <string>
#include <vector>

using namespace std;

bool win(const vector<char>& line, char player) {
  for (int i = 0; i < 4; ++i) {
    if (line[i] != 'T' && line[i] != player) {
      return false;
    }
  }
  return true;
}

string parse(string board[]) {
  vector<char> line;
  bool not_done = false;
  for (int i = 0; i < 4; ++i) {
    line.clear();
    for (int j = 0; j < 4; ++j) {
      line.push_back(board[i][j]);
      if (board[i][j] == '.') {
        not_done = true;
      }
    }
    if (win(line, 'O')) {
      return "O won";
    }
    if (win(line, 'X')) {
      return "X won";
    }
  }

  for (int i = 0; i < 4; ++i) {
    line.clear();
    for (int j = 0; j < 4; ++j) {
      line.push_back(board[j][i]);
    }
    if (win(line, 'O')) {
      return "O won";
    }
    if (win(line, 'X')) {
      return "X won";
    }
  }

  line.clear();
  for (int i = 0; i < 4; ++i) {
    line.push_back(board[i][i]);
  }
  if (win(line, 'O')) {
    return "O won";
  }
  if (win(line, 'X')) {
    return "X won";
  }

  line.clear();
  for (int i = 0; i < 4; ++i) {
    line.push_back(board[3-i][i]);
  }
  if (win(line, 'O')) {
    return "O won";
  }
  if (win(line, 'X')) {
    return "X won";
  }


  if (not_done) {
    return "Game has not completed";
  } else {
    return "Draw";
  }
}

int solve(int case_id) {
  char line[10];
  string board[4];
  for (int i = 0; i < 4; ++i) {
    gets(line);
    board[i] = line;
  }
  gets(line);

  string result = parse(board);

  printf("Case #%d: %s\n", case_id, result.c_str());
}

int main() {
  int case_num = 0;
  scanf("%d\n", &case_num);

  for (int i = 0; i < case_num; ++i) {
    solve(i+1);
  }
}
