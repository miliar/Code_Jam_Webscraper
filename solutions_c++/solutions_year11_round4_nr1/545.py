/* Google Code Jam 2011, Round 2, Problem A: "Airport Walkways". */
/* Sat. Jun. 4, 2011, By: Samuel Tien-Chieh Huang. */
// Last update: Sat. Jun. 4, 2011.
#include <cstdio>
#include <map>
using namespace std;

int main (void) {
  int nc, ca;
  scanf ("%d", &nc);
  for (ca = 1; ca <= nc; ++ ca) {
    int x, s, r, t, n, pos = 0;
    scanf ("%d%d%d%d%d", &x, &s, &r, &t, &n);
    map <int, int> s2d;  // [speed] => [span].
    for (int i = 0; i < n; ++ i) {
      int lo, hi, w;
      scanf ("%d%d%d", &lo, &hi, &w);
      s2d[s] += lo - pos;  // Walk to next walkway.
      s2d[w + s] += hi - lo;  // Walkway.
      pos = hi;
    }
    s2d[s] += x - pos;  // Walk to end.
    // Allot running time to slowest section, until used up quota.
    double rt = t, tott = 0;
    map <int, int>::iterator it;
    for (it = s2d.begin (); it != s2d.end (); ++ it) {  // Already sorted.
      double rd = rt * (it->first - s + r);  // Distance capacity if run.
      if (rd < it->second) {  // Will use up quota.
        // Run.
        tott += rt;
        rt = 0;
        // Walk.
        tott += (it->second - rd) / it->first;
      } else {  // Can run all the way.
        double dt = it->second / (double)(it->first - s + r);
        rt -= dt;
        tott += dt;
      }
    }    
    printf ("Case #%d: %.9f\n", ca, tott);
  }
  return 0;
}
