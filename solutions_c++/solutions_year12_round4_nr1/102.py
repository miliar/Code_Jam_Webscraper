#include <iostream>

using namespace std;

const int N_MAX = 20000;

int N;
long long D;
long long pos[N_MAX];
long long lengths[N_MAX];
long long best_swing[N_MAX];
long long farthest_reach[N_MAX];

void solve_case(int case_num) {
  cin >> N;
  for (int i = 0; i < N; i++) {
    cin >> pos[i] >> lengths[i];
  }
  cin >> D;

  best_swing[0] = min(pos[0], lengths[0]);
  farthest_reach[0] = 2 * best_swing[0];
  for (int i = 1; i < N; i++) {
    best_swing[i] = 0;
    for (int j = 0; j < i; j++) {
      if (pos[i] <= farthest_reach[j])
	best_swing[i] = max(best_swing[i], min(lengths[i], pos[i] - pos[j]));
    }
    farthest_reach[i] = best_swing[i] + pos[i];
  }

  bool possib = false;
  for (int i = 0; i < N; i++)
    if (farthest_reach[i] >= D)
      possib = true;
  cout << "Case #" << case_num << ": " << (possib ? "YES\n" : "NO\n");
}


int main() {
  int T;
  cin >> T;
  for (int i = 1; i <= T; i++)
    solve_case(i);
}
