#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <map>
#include <set>
#include <vector>

using namespace std;

int main() {
  int n_cases;
  cin >> n_cases;

  for (int i_case = 0; i_case < n_cases; i_case++) {
    int n, s, p;
    cin >> n >> s >> p;

    int ans = 0;
    for (int i = 0; i < n; i++) {
      int x;
      cin >> x;
      if (x >= 3*p-2) ans++;
      else if (x >= 3*p-4 && x > 0 && s > 0) {
        ans++;
        s--;
      }
    }
    printf ("Case #%d: %d\n", i_case+1, ans);
  } // end case
}
