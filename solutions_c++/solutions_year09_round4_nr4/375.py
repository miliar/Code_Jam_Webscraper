#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;

struct plant {
  double x, y, r;
  };

double dist(plant a, plant b) {
  double dx = a.x-b.x, dy = a.y-b.y;
  double d2 = dx*dx + dy*dy;
  double d = sqrt(d2) + a.r + b.r;
  return d/2;
  }

double answer(plant plants[], int N) {
  if (N == 1) return plants[0].r;
  if (N == 2) return min(dist(plants[0], plants[1]), max(plants[0].r, plants[1].r));
  // (N== 3)
  return min(dist(plants[0], plants[1]), min(dist(plants[1], plants[2]), dist(plants[2], plants[0])));
  }

int main() {
  int T; cin >> T;
  for (int cc = 1; cc <= T; ++cc) {
    int N; cin >> N;
    plant plants[40];
    for (int i = 0; i < N; ++i)
      cin >> plants[i].x >> plants[i].y >> plants[i].r;
    cout << "Case #" << cc << ": " << answer(plants, N) << endl;
    }
  }