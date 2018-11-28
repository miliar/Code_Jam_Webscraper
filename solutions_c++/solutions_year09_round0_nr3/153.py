/* Google Code Jam 2009, Qualification Round, Problem C: "Welcome to Code Jam". */
/* Wed. Sept. 2, 2009, By: Samuel Tien-Chieh Huang. */
// Last update: Wed. Sept. 2, 2009.
#include <cstdio>
#include <string>
#include <iostream>
using namespace std;

// Special case: No proper prefix is a proper substring.
char *key = "welcome to code jam";
#define KEY_LEN 19

int main (void) {
  string line;
  int nc, ca;
  getline (cin, line);
  sscanf (line.c_str (), "%d", &nc);
  for (ca = 1; ca <= nc; ca ++) {
    getline (cin, line);
    int len = line.length ();
    int state [KEY_LEN + 1] = {1, 0};
    for (int i = 0; i < len; i ++) {
      char ch = line [i];
      for (int j = 0; j < KEY_LEN; j ++) {
        if (ch != key [j]) continue;
        state [j + 1] += state [j];
        state [j + 1] %= 10000;
      }
    }
    printf ("Case #%d: %04d\n", ca, state [KEY_LEN]);
  }
  return 0;
}
