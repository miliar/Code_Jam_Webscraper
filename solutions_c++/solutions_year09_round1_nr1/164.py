#include <stdio.h>
#include <iostream>
#include <string>

#define N 50000000
short a[11][N];
bool b[11];

void cal(int j, int i) {
  a[j][i] = -2;
  int sum = 0;
  int k = i;
  while (k > 0) {
    int m = k % j;
    sum += m*m;
    k = k / j;
  }
  if (sum > N) {
    a[j][i] = 0;
    return;
  }
  if (a[j][sum] == -2) {
    a[j][i] = 0;
  } else if (a[j][sum] == -1) {
    cal(j, sum);
    if (a[j][sum] < 0) {
      printf("error2:%d,%d\n", j, sum);
    }
    a[j][i] = a[j][sum];
  } else if (a[j][sum] == 0) {
    a[j][i] = 0;
  } else if (a[j][sum] == 1) {
    a[j][i] = 1;
  } else {
    printf("error:%d,%d\n", j, i);
  }
}

int getN() {
  int i, j;
  bool flg;
  for (i = 2; i < N; i++) {
    flg = true;
    for (j = 3; j <= 10; j++) {
      if (b[j]) {
        if (a[j][i] == -1) {
          cal(j, i);
        }
        if (a[j][i] == 0) {
          flg = false;
          break;
        }
      }
    }
    if (flg) return i;
  }
  return -1;
}

int main()
{
  FILE *out = fopen("out.txt", "w");
  int T;
  std::string s;
  std::cin >> T;
  getline(std::cin, s);
  int i, j, k;
  for (i = 1; i < N; i++) {
    for (j = 3; j <= 10; j++) {
      if (i == 1 || (i % j == 0 && a[j][i/j] == 1)) {
        a[j][i] = 1;
      }
      else {
        a[j][i] = -1;
      }
    }
  }
  for (i = 0; i < T; i++) {
    getline(std::cin, s);
    for (j = 0; j < 11; j++) b[j] = false;
    while(s.length() > 0) {
      sscanf(s.c_str(), "%d", &k);
      printf("%d,", k);
      b[k] = true;
      int pos = s.find(' ');
      if (pos == -1) break;
      s = s.substr(pos+1, s.length() - pos - 1);
    }
    int n = getN();
    fprintf(out, "Case #%d: %d\n", i+1, n);
    printf("\n");
  }
  fclose(out);
  return 0;
}
