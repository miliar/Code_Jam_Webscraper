#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>
using namespace std;

string input[4];

int row_judge(int x) {
  int X_num = 0;
  int T_num = 0;
  int O_num = 0;
  int i;
  for (i = 0; i < 4; ++i) {
    if (input[x][i] == 'X') {
      X_num++;
    } else if (input[x][i] == 'T') {
      T_num++;
    } else if (input[x][i] == 'O') {
      O_num++;
    }
  }
  if (X_num == 4 || (X_num == 3 && T_num == 1)) {
    return 1;
  } else if (O_num == 4 || (O_num == 3 && T_num == 1)) {
    return -1;
  } else {
    return 0;
  }
}

int col_judge(int x) {
  int X_num = 0;
  int T_num = 0;
  int O_num = 0;
  int i;
  for (i = 0; i < 4; ++i) {
    if (input[i][x] == 'X') {
      X_num++;
    } else if (input[i][x] == 'T') {
      T_num++;
    } else if (input[i][x] == 'O') {
      O_num++;
    }
  }
  if (X_num == 4 || (X_num == 3 && T_num == 1)) {
    return 1;
  } else if (O_num == 4 || (O_num == 3 && T_num == 1)) {
    return -1;
  } else {
    return 0;
  }
}

int diagonal_judge() {
  int X_num = 0;
  int T_num = 0;
  int O_num = 0;
  int i;
  for (i = 0; i < 4; ++i) {
    if (input[i][i] == 'X') {
      X_num++;
    } else if (input[i][i] == 'T') {
      T_num++;
    } else if (input[i][i] == 'O') {
      O_num++;
    }
  }
  if (X_num == 4 || (X_num == 3 && T_num == 1)) {
    return 1;
  } else if (O_num == 4 || (O_num == 3 && T_num == 1)) {
    return -1;
  } else {
    X_num = 0;
    T_num = 0;
    O_num = 0;
    for (i = 0; i < 4; ++i) {
      if (input[i][3 - i] == 'X') {
        X_num++;
      } else if (input[i][3 - i] == 'T') {
        T_num++;
      } else if (input[i][3 - i] == 'O') {
        O_num++;
      }
    }
    if (X_num == 4 || (X_num == 3 && T_num == 1)) {
      return 1;
    } else if (O_num == 4 || (O_num == 3 && T_num == 1)) {
      return -1;
    } else {
      return 0;
    }
  }
}

void judge() {
  int i, j, res;
  bool is_completed = 1;
  for (i = 0; i < 4; ++i) {
    for (j = 0; j < 4; ++j) {
      if (input[i][j] == '.') {
        is_completed = 0;
      }
    }
  }

  for (i = 0; i < 4; ++i) {
    res = row_judge(i);
    if (res == 1) {
      cout << "X won" << endl;
      return;
    } else if (res == -1) {
      cout << "O won" << endl;
      return;
    }
  }

  for (i = 0; i < 4; ++i) {
    res = col_judge(i);
    if (res == 1) {
      cout << "X won" << endl;
      return;
    } else if (res == -1) {
      cout << "O won" << endl;
      return;
    }
  }

  res = diagonal_judge();
  if (res == 1) {
    cout << "X won" << endl;
    return;
  } else if (res == -1) {
    cout << "O won" << endl;
    return;
  }

  if (is_completed) {
    cout << "Draw" << endl;
    return;
  }
  cout << "Game has not completed" << endl;
}

int main() {
  int cases;
  int i, j;
  cin >> cases;

  for (i = 1; i <= cases; ++i) {
    for (j = 0; j < 4; ++j) {
      cin >> input[j];
    }

    cout << "Case #" << i << ": ";
    judge();
  }

  return 0;
}

