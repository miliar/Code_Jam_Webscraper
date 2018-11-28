#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <climits>
#include <ctime>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
#include <deque>
#include <list>
#include <queue>
#include <set>
#include <map>
#include <limits>
#include <cstring>

using namespace std;

char number[150];
int qmarks[150];
int n, nq;

int main() {
  int nCases;
  scanf("%d", &nCases);
  for (int iCase = 1; iCase <= nCases; iCase++) {
    scanf("%149s", number);
    n = strlen(number);
    nq = 0;
    for (int i = 0; i < n; i++) {
      if (number[i] == '?') {
        qmarks[nq] = i;
        nq++;
      }
    }
    int maxI = 1 << nq;
    for (int i = 0; i < maxI; i++) {
      for (int j = 0; j < nq; j++) {
        number[qmarks[j]] = (i & (1 << j)) ? '1' : '0';
      }
      long long value = 0;
      for (int j = 0; j < n; j++) {
        value = (value << 1) + number[j] - '0';
      }
      long long squareRoot = (long long) sqrtl((long double) value);
      if (squareRoot * squareRoot == value)
        break;
    }
    printf("Case #%i: %s\n", iCase, number);
  }
  return 0;
}
