#include <iostream>
#include <cstdio>

using namespace std;

const int MAXN = 5;
char s[MAXN][MAXN];

bool check(int i, int j, char c) {
  return s[i][j] == c || s[i][j] == 'T';
}

bool win(char c, int n) {
  for (int i = 0; i < n; ++i) {
    int cnt = 0;
    for (int j = 0; j < n; ++j) {
      cnt += check(i, j, c);
    }
    if (cnt == n) {
      return true;
    }
  }

  for (int j = 0; j < n; ++j) {
    int cnt = 0;
    for (int i = 0; i < n; ++i) {
      cnt += check(i, j, c);
    }
    if (cnt == n) {
      return true;
    }
  }

  if (check(0, 0, c) && check(1, 1, c) && check(2, 2, c) && check(3, 3, c)) {
    return true;
  }
  if (check(0, 3, c) && check(1, 2, c) && check(2, 1, c) && check(3, 0, c)) {
    return true;
  }
  return false;
}

int main() {
  freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w", stdout);
  int t, cas = 1;
  int n = 4;

  scanf("%d", &t);
  while (t--) {
    printf("Case #%d: ", cas++);

    int cnt = 0;
    for (int i = 0; i < n; ++i) {
      scanf("%s", s[i]);
      for (int j = 0; j < n; ++j) {
        cnt += s[i][j] != '.';
      }
    }
    if (win('X', n)) {
      puts("X won");
    } else if (win('O', n)) {
      puts("O won");
    } else if (cnt == n * n) {
      puts("Draw");
    } else {
      puts("Game has not completed");
    }
  }
  return 0;
}
