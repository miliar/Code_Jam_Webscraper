/* Google Code Jam 2009: Round 1B: Problem B: "The Next Number". */
// Sat. Sept. 12, 2009, By: Samuel Tien-Chieh Huang.
// Last update: Sat. Sept. 12, 2009.
#include <cstdio>
#include <string>
#include <iostream>
#include <algorithm>
using namespace std;

int main (void) {
  string line;
  getline (cin, line);
  int nc;
  sscanf (line.c_str (), "%d", &nc);
  for (int ca = 1; ca <= nc; ca ++) {
    getline (cin, line);
    printf ("Case #%d: ", ca);
    if (!next_permutation (line.begin (), line.end ())) {
      int i;
      for (i = 0; i < (int) line.length (); i ++) {
        if (line [i] != '0') break;
      }
      char t = line [i];
      line [i] = '0';
      line = t + line;
    }
    printf ("%s\n", line.c_str ());
  }
  return 0;
}
