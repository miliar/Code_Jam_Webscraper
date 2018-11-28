#include <iostream>
#include <cmath>
#include <complex>
#include <algorithm>
#include <queue>
#include <cassert>

using namespace std;
typedef complex<long long> Point;

const double EPS = 1e-7;
const int N_MAX = 3000;

int N;
long long L, W;
long long radius[N_MAX];
int perm[N_MAX];
Point locs[N_MAX];

queue<int> Q;

bool comp_radius(int x, int y) {
  return radius[x] > radius[y];
}

void solve(Point upper_left, int l, int w) {
  //  cout << upper_left << " " << l << " " << w << endl;

  if (Q.empty())
    return;
  int cur = Q.front(); 
  long long r = radius[cur];
  if (l < 0 || w < 0)
    return;

  Q.pop();
  locs[cur] = upper_left;
  //  cout << cur << " loc: " << locs[cur] << endl;

  solve(upper_left + Point(0, 2 * r), r, w - 2 * r);
  solve(upper_left + Point(2 * r, 0), l - 2 * r, w);
}

void solve_case(int case_num) {
  cin >> N >> W >> L;
  for (int i = 0; i < N; i++) {
    cin >> radius[i];
    perm[i] = i;
  }

  sort(perm, perm + N, comp_radius);
  for (int i = 0; i < N; i++)
    Q.push(perm[i]);
  solve(Point(0, 0), L, W);

  assert(Q.empty());

  // (l, w)
  cout << "Case #" << case_num << ": ";
  for (int i = 0; i < N; i++)
    cout << " " << locs[i].imag() << " " << locs[i].real();
  cout << '\n';
}

int main() {
  int T;
  cin >> T;
  for (int i = 1; i <= T; i++)
    solve_case(i);
}
