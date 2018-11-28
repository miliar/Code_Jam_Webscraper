#include <cstdio>
#include <iostream>
#include <algorithm>
#include <random>
#include <functional>

using namespace std;

int T, N, W, L;
double r[1000];
double x[1000], y[1000];

std::uniform_int_distribution<int> distribution(0, 1000000000);
std::mt19937 engine; // Mersenne twister MT19937
auto generator = std::bind(distribution, engine);

double random() {
  return generator() / 1000000000.0;
}

bool dfs(int from) {

  if (from >= N)
    return true;

  for (int n = 0; n < 1000; n++) {
    bool fail = false;
    x[from] = random() * W;
    y[from] = random() * L;
    for (int i = 0; i < from; i++) {
      double d = (x[i] - x[from]) * (x[i] - x[from]) + 
          (y[i] - y[from]) * (y[i] - y[from]);
      if (d <= (r[i] + r[from]) * (r[i] + r[from])) {
        fail = true;
        break;
      }
    }
    if (!fail && dfs(from + 1))
      return true;
  }
  return false;
}

int main() {

  cin >> T;
  for (int CASE = 1; CASE <= T; CASE++) {
    cin >> N >> W >> L;
    for (int i = 0; i < N; i++)
      cin >> r[i];
    while (!dfs(0));
    printf("Case #%d:", CASE);
    for (int i = 0; i < N; i++)
      printf(" %f %f", x[i], y[i]);
    cout << endl;
  }

}
