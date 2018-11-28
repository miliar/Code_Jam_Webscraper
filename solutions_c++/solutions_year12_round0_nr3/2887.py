#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;

int get_digits(int x) {
  int ans = 0;
  while (x > 0) {
    ans++;
    x /= 10;
  }
  return ans;
}

bool update (int x[], int n) {
  int i = n-1;
  while (x[i] >= 9 && i >= 0) i--;

  if (i < 0) return false;

  (x[i])++;
  int tmp = x[i];
  for (int j = n-1; j > i; j--) x[j] = x[i];
  return true;
}

void print_set(set<int> s) {
  for (set<int>::iterator it = s.begin();
       it != s.end();
       it++) {
    printf ("%d ", *it);
  }
  printf ("\n");
}

bool already_used (set<int> used, int d[], int n) {
  int x = 0, pow = 1;
  for (int i = n-1; i >= 0; i--) {
    x += pow * d[i];
    pow *= 10;
  }
  return used.count(x);
}

int main() {
  int n_cases;
  cin >> n_cases;
  for (int i_case = 0; i_case < n_cases; i_case++) {
    int a, b;
    cin >> a >> b;

    int n_dig = get_digits(a);
    int d[n_dig];
    memset (d, 0, sizeof(int)*n_dig);
    int ans = 0; // max = 0
    do {
      set<int> used;
      do {
        if (already_used (used, d, n_dig)) continue;

        int test[n_dig];
        memset (test, 0, sizeof(int)*n_dig);
        for (int i = 0; i < n_dig; i++) {
          int pow = 1;
          for (int j = 0; j < n_dig; j++) {
            test[(i + j) % n_dig] += d[i]*pow;
            pow *= 10;
          }
        }

        set<int> s;
        for (int i = 0; i < n_dig; i++) {
          if (test[i] >= a && test[i] <= b) s.insert(test[i]);
          used.insert(test[i]);
        }

        int n_valid = s.size();
        ans += n_valid*(n_valid-1)/2;
        /*
        if (n_valid >= 0) {
          printf ("%d %d: ", ans, n_valid);
          //print_set(s);
          for (int i = 0; i < n_dig; i++) printf ("%d ", test[i]);
          printf ("\n");
        }*/
      } while (next_permutation (d, d+n_dig));
    } while (update (d, n_dig));//, &max));

    printf ("Case #%d: %d\n", i_case+1, ans);
  }
}
