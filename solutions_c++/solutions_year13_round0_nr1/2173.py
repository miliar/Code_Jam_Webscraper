#include <algorithm>
#include <functional>

#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <string>
#include <vector>
#include <map>

using namespace std;

bool done, xwon, owon;

struct Line {
  int x, o, t;
  Line() {
    x = o = t = 0;
  }
  void update(char c) {
    if (c == 'T') ++t;
    else if (c == 'X') ++x;
    else if (c == 'O') ++o;
    else done = false;


    if (x+t == 4) xwon = true;
    if (o+t == 4) owon = true;
  }
};

string get() {
  if (xwon) {
    return "X won";
  } else if (owon) {
    return "O won";
  } else if (!done) {
    return "Game has not completed";
  } else {
    return "Draw";
  }
}

int main(void)
{
  int T; scanf("%d", &T);

  for (int counter = 0; counter < T; ++counter) {
    map<int, Line> row;
    map<int, Line> col;
    map<int, Line> diag1;
    map<int, Line> diag2;

    done = true;
    xwon = owon = false;

    for (int i = 0; i < 4; ++i)
      for (int j = 0; j < 4; ++j) {
        char c; scanf(" %c", &c);
        row[i].update(c);
        col[j].update(c);
        diag1[i+j].update(c);
        diag2[i-j].update(c);
      }

    printf("Case #%d: %s\n", counter + 1, get().c_str());
    fflush(stdout);
  }

  return (0-0);
}
