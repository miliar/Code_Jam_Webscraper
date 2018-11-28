/* Google Code Jam 2011, Qualification Round, Problem B: "Magicka". */
/* Fri. May. 6, 2011, By: Samuel Tien-Chieh Huang. */
// Last update: Fri. May. 6, 2011.
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <map>
using namespace std;

int encode (string &s, int lo, int hi) {
  int ret = 0;
  for (int i = lo; i < hi; ++ i) ret |= 1 << (int)(s[i] - 'A');
  return ret;
}

int main (void) {
  int nc, ca;
  cin >> nc;
  for (ca = 1; ca <= nc; ++ ca) {
    int c, d, n;
    string s, cur = "";
    // Build combine list.
    cin >> c;
    map <int, char> comb;
    for (int i = 0; i < c; ++ i) {
      cin >> s;
      comb[encode (s, 0, 2)] = s[2];
    }
    // Build opposed list.
    cin >> d;
    vector <int> oppo;
    for (int i = 0; i < d; ++ i) {
      cin >> s;
      oppo.push_back (encode (s, 0, 2));
    }
    // Process spell.
    cin >> n >> s;
    for (int i = 0; i < n; ++ i) {  // O(n^2), but fast enough for contest.
      // Grow string.
      cur += s[i];
      // Perform combinations for last two characters.
      int len = cur.length (), code;
      code = encode (cur, len - 2, len);
      if ((len >= 2) && comb.count (code)) cur = cur.substr (0, len - 2) + comb [code];
      // If find oppose, clear string.
      len = cur.length ();
      code = encode (cur, 0, len);
      for (int j = 0; j < d; ++ j) {
        if ((code & oppo[j]) == oppo[j]) {
          cur = "";
          break;
        }
      }
    }
    printf ("Case #%d: [", ca);
    for (int i = 0; i < (int) cur.length (); ++ i) printf ((i == 0) ? "%c" : ", %c", cur[i]);
    printf ("]\n");
  }
  return 0;
}
