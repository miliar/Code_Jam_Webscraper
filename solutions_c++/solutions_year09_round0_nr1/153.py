/* Google Code Jam 2009, Qualification Round, Problem A: "Alien Language". */
/* Wed. Sept. 2, 2009, By: Samuel Tien-Chieh Huang. */
// Last update: Wed. Sept. 2, 2009.
#include <cstdio>
#include <string>
#include <iostream>
using namespace std;

int L, D, N;

int dict [5100][16];

int parse_mask (string &s, int &pos) {
  char ch = s [pos ++];
  if (ch == '(') {
    int ret = 0;
    for (;;) {
      ch = s [pos ++];
      if (ch == ')') break;
      ret |= 1 << (ch - 'a');
    }
    return ret;
  } else {
    return 1 << (ch - 'a');
  }
}

int main (void) {
  string line;
  getline (cin, line);
  sscanf (line.c_str (), "%d%d%d", &L, &D, &N);
  for (int i = 0; i < D; i ++) {
    getline (cin, line);
    for (int j = 0; j < L; j ++) {
      dict [i][j] = 1 << (line[j] - 'a');
    }
  }
  /*for (int i = 0; i < D; i ++) {
    for (int j = 0; j < L; j ++) printf (" %d", dict [i][j]);
    printf ("\n");
  }*/
  for (int i = 0; i < N; i ++) {
    int q [16], pos = 0;
    getline (cin, line);
    for (int j = 0; j < L; j ++) {
      q [j] = parse_mask (line, pos);
      //printf ("%d ", q [j]);
    }
    //printf ("\n");
    int res = 0;
    for (int j = 0; j < D; j ++) {
      int k;
      for (k = 0; k < L; k ++) {
        if ((dict [j][k] & q [k]) == 0) break;
      }
      if (k == L) res ++;
    }
    printf ("Case #%d: %d\n", i + 1, res);
  }
  return 0;
}
