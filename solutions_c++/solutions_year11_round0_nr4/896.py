#include <iostream>
#include <stdio.h>
using namespace std;

int T, N, nCase;
int a[1010], f[1010], num[1010];
double Min;

int main() {
  FILE *file = freopen("D-large.in", "r", stdin);
  FILE *file2 = freopen("D-large.out", "w", stdout);
  cin >> T;
  nCase = 1;
  while (T--) {
    cin >> N;
    Min = 0.0;
    for (int i = 1; i <= N; i++) {
      cin >> a[i];
      if (a[i] != i) {
        Min += 1.0;
      }
      f[i] = 1;
      num[i] = 0;
    }
    for (int i = 1; i <= N; i++) {
      if (f[i]) {
        int j = i;
        while (1) {
          num[i]++;
          f[j] = 0;
          if (a[j] == i) {
            break;
          }
          j = a[j];
        }
      }
    }
    double result = 1.0;
    for (int i = 1; i <= N; i++) {
      if (num[i] > 0) {
        result *= num[i];
        if (result > Min) {
          result = Min;
          break;
        }
      }
    }
    printf("Case #%d: %0.6llf\n", nCase++, result);
  }
}
