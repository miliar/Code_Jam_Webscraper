#include <cassert>
#include <cstdio>
#include <map>
#include <set>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <vector>
#include <iostream>

using namespace std;

int main(void) {
  int tn, nt;
  scanf("%d", &nt);
  for (tn=1; tn<=nt; tn++) {
    printf ("Case #%d: ", tn);

    long long n;
    int p1, p2;

    cin >> n >> p1 >> p2;
    n = min(n, 100ll);

    int ok = 0;
    if (p2 == 100)
      ok = p1 == 100;
    else if (p2 == 0)
      ok = p1 == 0;
    else {
      for (int i=1; i<=n; i++)
        if ((p1 * i) % 100 == 0) {
          ok = 1;
        } 
    }

    puts (ok ? "Possible" : "Broken");
  }

  return 0;
}
