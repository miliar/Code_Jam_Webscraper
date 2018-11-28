#include <map>
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
int solvablePos[10001];
int vines[10001][2];
int solvable(int from, int swing, int N) {
  if (from == N - 1 || solvablePos[from] <= swing) {
    return 1;
  }
  for (int x = from + 1; x < N; x++) {
    if (vines[from][0] < vines[x][0] && vines[from][0] + swing >= vines[x][0]) {
      if (solvable(x, min(vines[x][1], vines[x][0] - vines[from][0]), N)) {
        solvablePos[from] = min(solvablePos[from], swing);
        solvablePos[x] = min(solvablePos[x], min(vines[x][1], vines[x][0] - vines[from][0]));
        return 1;
      }
    }
  }
  return 0;
}
int solve() {
  int N, D;
  cin >> N;
  for (int x = 0; x < N; x++) {
    cin >> vines[x][0] >> vines[x][1];
  }
  cin >> D;
  for (int x = 0; x < N + 1; x++) {
    solvablePos[x] = D;
  }
  vines[N][0] = vines[N][1] = D;
  return solvable(0, vines[0][0], N + 1);
}
int main() {
  int T;
  cin >> T;
  for (int x = 1; x <= T; x++) {
    cout << "Case #" << x << ": " << (solve() ? "YES" : "NO") << endl;
  }
  return 0;
}

