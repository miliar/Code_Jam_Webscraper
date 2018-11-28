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

const int kMax = 2000005;
int T, max_n, min_n;
int res;
int len[kMax];
int pow_nbit[9];

void Init() {
  int nbit = 1;
  pow_nbit[0] = 1;
  pow_nbit[1] = 10;
  len[0] = 0;
  len[1] = 1;
  for (int i = 2; i < kMax; i++) {
    if (i % pow_nbit[nbit] == 0) {
      nbit++;
      pow_nbit[nbit] = pow_nbit[nbit - 1] * 10; 
    }
    len[i] = nbit;
  }
}

void SubTest(int i, int min_n, int max_n) {
  int L = len[i];
  vector<int> rec;
  for (int j = 1; j < L; j++) {
    int m = i % pow_nbit[j];
    int n = i / pow_nbit[j];
    int r = m * pow_nbit[L - j] + n;
    if (r >= min_n && r <= max_n && len[r] == L &&
        r > i) {
      int sz = rec.size();
      bool dup = false;
      for (int k = 0; k < sz; k++) {
        if (r == rec[k]) {
          dup = true;
          break;
        }
      }
      if (!dup) {
        rec.push_back(r);
        res++;
      }
    }
  }
}

void Test(int min_n, int max_n) {
  for (int i = min_n; i < max_n; i++) {
    SubTest(i, min_n, max_n);
  }
}
int main() {
  scanf("%d", &T);
  Init();
  for (int ncas = 1; ncas <= T; ncas++) {
    res = 0;
    scanf("%d%d", &min_n, &max_n);
    Test(min_n, max_n);
    printf("Case #%d: %d\n", ncas, res);
  }
  return 0;
}
