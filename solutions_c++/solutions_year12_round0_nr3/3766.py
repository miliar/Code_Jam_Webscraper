#include <iostream>
#include <set>
#include <stdio.h>
#include <string.h>

using namespace std;

int t, a, b, c1, c2, pow, digits, pdigits;
long long cnt = 0;
set<int> sett;

int main() {
    scanf("%d\n", &t);
    for (int i = 1; i <= t; ++i) {
        scanf("%d %d\n", &a, &b);
        cnt = 0;
        for (int j = a; j < b; ++j) {
            sett.clear();
            digits = pdigits = 0;
            pow = j;
            while (pow != 0) {
                  ++digits;
                  pow = pow / 10;
            }
            pow = 10;
            while (pow < j) {
                  c1 = j % pow;
                  c2 = j / pow;
                  pow = pow * 10;
                  ++pdigits;
                  for (int k = 0; k < digits - pdigits; ++k) {
                      c1 = c1 * 10;
                  }
                  c1 = c1 + c2;
                  if (sett.find(c1) == sett.end() && j < c1 && c1 <= b) {
                     // cout << j << " " << c1 << endl;
                     ++cnt;
                     sett.insert(c1);
                  }
            }
        }
        printf("Case #%d: %lld\n", i, cnt);
    }
    return 0;
}
