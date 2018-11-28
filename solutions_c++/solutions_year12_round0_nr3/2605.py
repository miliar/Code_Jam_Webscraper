#include <set>
#include <map>
#include <iostream>
#include <string>
#include <stdio.h>
using namespace std;

int log10 (int x) {
  int k = 0;
  while (x) {
    ++k;
    x /= 10;
  }

  return k;
}

int pow10 (int x) {
  int k = 1;
  while (x) {
    k *= 10;
    --x;
  }

  return k;
}

void solve (int a_case) {
  int A, B;
  set<pair<int, int> > yay;
  cin >> A >> B;

  char str[32];
  for (int i = A; i < B; ++i) {
    int k = log10(i);

    for (int j = 1; j < k; ++j) {
      int i2 = (i % pow10(j)) * pow10(k - j) + (i / pow10(j));

      if (i < i2 && i2 <= B && log10(i2) == k) {
        yay.insert(make_pair(i, i2));
        // printf("%d %d = %d\n", i / pow10(j), i % pow10(j), i2);
      }
    }

  }

  printf("Case #%d: %d\n", a_case, (int)yay.size());
}

int main ()
{
  int n;

  cin >> n;
  for (int i = 0; i < n; ++i) solve(i+1);

  return 0;
}

