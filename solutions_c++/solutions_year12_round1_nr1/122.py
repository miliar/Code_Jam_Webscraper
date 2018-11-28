#include <algorithm>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define pb push_back
#define go(x,it) for(typeof((x).begin()) it=(x).begin(); it!=(x).end(); it++)
#define x first
#define y second

typedef long long ll;

bool solve(int C) {
  printf("Case #%d: ", C);
  int A, B;
  cin>>A>>B;
  vector<double> p(A);
  double X = 1;
  double best_backspace = B + B + 1;
  for (int i = 0; i < A; i++) {
    best_backspace = min(best_backspace, X * ((A - i) + (B - i) + 1) + (1 - X) * (A - i + (B - i) + 1 + B + 1));
    cin>>p[i];
    X *= p[i];
  }
  int i = A;
  best_backspace = min(best_backspace, X * ((A - i) + (B - i) + 1) + (1 - X) * (A - i + (B - i) + 1 + B + 1));

  double res = B + 2;

  // finish typing
  res = min(res, X * (B - A + 1) + (1 - X) * (B - A + 1 + B + 1));

  // backspace
  res = min(res, best_backspace);

  printf("%0.6lf\n", res);

  return true;
}

int main() {
  std::ios_base::sync_with_stdio(false);
  srand(time(NULL));
  int n = 1;
  cin>>n;
  for (int i = 1; i <= n; i++) {
    if (!solve(i)) {
      break;
    }
  }
  return 0;
}

