#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <iostream>
using namespace std;

int T, N, S, P;
int a[105];
bool can[105];
int res;

void Test(int i) {
  int t = a[i];
  int b = t / 3;
  int m = t % 3;
  bool part[2];
  part[0] = part[1] = true;
  int max_t;
  if (m == 0) {
    if (b - 1 < 0 || b + 1 > 10) {
      part[1] = false;
      max_t = b;
    }
  } else if (m == 1) {
    if (b - 1 < 0) {
      part[1] = false;
      max_t = b + 1;
    }
  } else if (m == 2) {
    if (b + 2 > 10) {
      part[1] = false;
      max_t = b + 1;
    }
  }
  if (!part[1]) {
    can[i] = false;
    if (max_t >= P) {
      res++;
    }
  }
}
int main() {
  scanf("%d", &T);
  for (int ncas = 1; ncas <= T; ncas++) {
    res = 0;
    scanf("%d%d%d", &N, &S, &P);
    for (int i = 0; i < N; i++) {
      can[i] = true;
      scanf("%d", &a[i]);
      Test(i);
    }
    for (int i = 0; i < N; i++) {
      if (!can[i]) continue;
      int c = a[i];
      int b = c / 3;
      int m = c % 3;
      if (m == 0) {
        if (b >= P) {
          res++;
        } else if (b + 1 >= P && S > 0) {
          res++;
          S--;
        }
      } else if (m == 1) {
        if (b + 1 >= P) {
          res++;
        }
      } else if (m == 2) {
        if (b + 1 >= P) {
          res++;
        } else if (b + 2 >= P && S > 0) {
          S--;
          res++;
        }
      }
    }
    printf("Case #%d: %d\n", ncas, res);
  }
  return 0;
}
