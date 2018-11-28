#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>

using namespace std;

const int MaxN = 10;
const int dx[] = { -1, -1, -1, 0, 1, 1, 1, 0 };
const int dy[] = { -1, 0, 1, 1, 1, 0, -1, -1 };
char mp[MaxN][MaxN];

bool in(int x, int y) {
  return x >= 0 && x < 4 && y >= 0 && y < 4;
}

void sol() {
  int cnt = 0;
  for (int i = 0; i < 4; ++i)
    cnt += count(mp[i], mp[i] + 4, '.');
  for (int i = 0; i < 4; ++i)
    for (int j = 0; j < 4; ++j) {
      char id = mp[i][j];
      if (id == '.' || id == 'T')
        continue;
      for (int d = 0; d < 8; ++d) {
        if (in(i + dx[d] * 3, j + dy[d] * 3)) {
          bool ok = true;
          for (int k = 0; k < 4; ++k) {
            if (mp[i + dx[d] * k][j + dy[d] * k] != id && mp[i + dx[d] * k][j + dy[d] * k] != 'T') {
              ok = false;
              break;
            }
          }
          if (ok) {
            puts(id == 'O' ? "O won" : "X won");
            return;
          }
        }
      }
    }

  if (cnt == 0) {
    puts("Draw");
  } else {
    puts("Game has not completed");
  }
}

int main() {
  int T;

  freopen("data.in", "r", stdin);
  freopen("data.out", "w", stdout);
  
  scanf("%d", &T);
  for (int cas = 1; cas <= T; ++cas) {
    for (int i = 0; i < 4; ++i)
      scanf("%s", mp[i]);
    printf("Case #%d: ", cas);
    sol();
  }

  return 0;
}

