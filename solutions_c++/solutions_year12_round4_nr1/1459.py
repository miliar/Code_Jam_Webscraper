#include <iostream>
#include <iomanip>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;



bool aux(int N, vector<int> &d, vector<int> &l, int D, int x, int k) {
  int lcur = d[k] - x;
  int xmax = x + 2*lcur;
  if (xmax >= D) {
    return true;
  }
  if (k+1 == N) {
    return false;
  }
  int xmax2 = xmax;
  int imax = k;
  for (int i = k+1; i < N && d[i] <= xmax; i++) {
    int y = max(d[k], d[i] - l[i]);
    int ymax = y + 2*(d[i] - y);
    if (ymax > xmax2) {
      xmax2 = ymax;
      imax = i;
    }
  }
  if (imax == k) return false;
  if (aux(N, d, l, D, max(d[k], d[imax] - l[imax]), imax)) return true;
  for (int i = imax - 1; i > k; i--) {
    int y = max(d[k], d[i] - l[i]);
    if (y + 2*(d[i] - y) > d[imax]) {
      if (aux(N, d, l, D, y, i)) return true;
    }
  }
  return false;
/*
  int i = k+1;
  while (i < N && d[i] <= xmax) {
    int y = max(d[k], d[i] - l[i]);
    if (aux(N, d, l, D, y, i)) {
      return true;
    }
    i++;
  }
  return false;
*/
}

bool solve(int N, vector<int> &d, vector<int> &l, int D) {
  return aux(N, d, l, D, 0, 0);
}

int main() {
  int T;
  cin >> T;
  for (int testcase = 0; testcase < T; testcase++) {
    int N;
    cin >> N;
    vector<int> d(N);
    vector<int> l(N);
    for (int i = 0; i < N; i++) {
      cin >> d[i];
      cin >> l[i];
    }
    int D;
    cin >> D;
    bool res = solve(N, d, l, D);
    if (res)
      cout << "Case #" << testcase + 1 << ": " << "YES" << endl;
    else
      cout << "Case #" << testcase + 1 << ": " << "NO" << endl;
  }
  return 0;
}
