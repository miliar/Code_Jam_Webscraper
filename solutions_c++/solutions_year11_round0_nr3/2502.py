#include <fstream>
#include <iostream>
#include <stdio.h>
#include <math.h>
#include <string.h>

using namespace std;

int solve(int n, int a[]) {

  int min = a[0];
  int sum = 0;
  int xorall = 0;
  for (int i = 0; i < n; i ++) {
    xorall ^= a[i];
    sum += a[i];
    if (a[i] < min) min = a[i];
  }
  if (xorall == 0) return sum - min;

  return -1;
}

int main() {

  ifstream f("candy.in");  
  ofstream g("candy.out");

  int t, n;
  int a[50000];

  f >> t;

  for (int i = 0; i < t; i++) {
    f >> n;
    for (int j = 0; j < n; j++) {
      f >> a[j];
    }
    int res = solve(n, a);
    if (res < 0) g << "Case #" << i + 1 << ": NO" << endl;
    else g << "Case #" << i + 1 << ": " << res << endl;
  }
  
  return 0;
}

