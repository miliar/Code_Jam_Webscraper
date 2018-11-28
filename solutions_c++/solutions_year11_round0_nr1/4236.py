#include <cstdio>
#include <queue>
#include <cstring>

using namespace std;

class state {
public:
  int orange, blue, buttons;

  state(int _o, int _b, int _but) {
    this->orange = _o;
    this->blue = _b;
    this->buttons = _but;
  }
};

int T;
int buttons[101];
int bio[101][101][101];

void load() {
  scanf("%d", &T);
  for (int i = 0; i < T; ++i) {
    char t[2];
    int a;
    scanf("%s%d", t, &a);
    if (t[0] == 'B') {
      a *= -1;
    }
    buttons[i] = a;
  }
}

int solve() {
  queue <state> Q;

  memset(bio, -1, sizeof(bio));

  Q.push(state(1, 1, 0));
  bio[1][1][0] = 0;

  do {
    state s = Q.front();
    Q.pop();

    //printf("%d %d %d %d\n", s.orange, s.blue, s.buttons, bio[s.orange][s.blue][s.buttons]);

    if (s.buttons == T) {
      return bio[s.orange][s.blue][s.buttons];
    }

    for (int x = -1; x <= 1; ++x) {
      for (int y = -1; y <= 1; ++y) {
        state t(s.orange + x, s.blue + y, s.buttons);

        if (t.orange <= 0 || t.blue <= 0) {
          continue;
        }

        if (buttons[s.buttons] < 0 && y == 0) {
          if (t.blue == -buttons[s.buttons]) {
            t.buttons++;
          }
        } else if (buttons[s.buttons] > 0 && x == 0) {
          if (t.orange == buttons[s.buttons]) {
            t.buttons++;
          }
        }

        if (bio[t.orange][t.blue][t.buttons] == -1) {
          bio[t.orange][t.blue][t.buttons] = bio[s.orange][s.blue][s.buttons]+1;
          Q.push(t);
        }
      }
    }
  } while (Q.size());
}

int main() {
  int N;
  scanf("%d", &N);

  for (int tt = 0; tt < N; ++tt) {
    load();
    printf("Case #%d: %d\n", tt + 1, solve());
  }

  return 0;
}
