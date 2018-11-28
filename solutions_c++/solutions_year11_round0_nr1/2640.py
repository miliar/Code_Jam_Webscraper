#include <cstdio>
#include <iostream>
#include <algorithm>
#include <queue>

using namespace std;

const int nmax = 105;

struct Move {
  char r;
  int pos;
  int seq;
};

int main(void) {
  int nc;
  queue<Move> qo, qb;

  freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w", stdout);

  scanf("%d", &nc);
  for (int c = 1; c <= nc; c++) {
    int ni;
    scanf("%d", &ni);

    for (int i = 0; i < ni; ++i) {
      Move mv;

      scanf(" %c %d", &mv.r, &mv.pos);
      mv.seq = i;

      if (mv.r == 'O') {
        qo.push(mv);
      } else {
        qb.push(mv);
      }
    }

    int time = 0;
    int poso = 1, posb = 1;
    int seq = 0;
    while(!qo.empty() || !qb.empty()) {
      bool popped = false;

      if (!qo.empty()) {
        Move mo = qo.front();
        if (mo.pos == poso) {
          if (mo.seq == seq) {
            popped = true;
            qo.pop();
          }
        } else if (mo.pos > poso) {
          poso++;
        } else {
          poso--;
        }
      }

      if (!qb.empty()) {
        Move mb = qb.front();

        if (mb.pos == posb) {
          if (mb.seq == seq) {
            popped = true;
            qb.pop();
          }
        } else if (mb.pos > posb) {
          posb++;
        } else {
          posb--;
        }
      }


      if (popped) seq++;
      time++;
    }

    printf("Case #%d: %d\n", c, time);
  }

  

  


}