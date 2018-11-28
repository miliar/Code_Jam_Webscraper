#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <utility>
#include <algorithm>
#include <cmath>

using namespace std;

double calc(int xs[], int ys[], int rs[], int p1, int p2, int p3)
{
  double x = xs[p1] - xs[p2];
  double y = ys[p1] - ys[p2];
  double r = sqrt(x*x+y*y);

  return max((r+rs[p1]+rs[p2])/2, double(p3));
}

int main()
{
  int cas;
  int C;

  cin >> C;

  for (cas = 1; cas <= C; cas++) {
    int N;
    int xs[40];
    int ys[40];
    int rs[40];
    cin >> N;
    for (int i = 0; i < N; i++) {
      cin >> xs[i] >> ys[i] >> rs[i];
    }

    double r;
    if (N == 3) {
      r = calc(xs, ys, rs, 0, 1, 2);
      r = min(r, calc(xs, ys, rs, 0, 2, 1));
      r = min(r, calc(xs, ys, rs, 1, 2, 0));
    } else if (N == 2) {
      r = max(rs[0], rs[1]);
    } else {
      r = rs[0];
    }
    
    cout << "Case #" << cas << ": " << fixed << r << endl;
  }

  return 0;
}

