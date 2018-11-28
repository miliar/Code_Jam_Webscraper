#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
int costs[101][257][257];
int D, I, M, N, values[101];
int solvecost(int pos, int last, int ii) {
  if (pos == N) return 0;
  if (costs[pos][last][ii] != -1) return costs[pos][last][ii];
  if (ii == 256) return costs[pos][last][ii] = 1000000000;

  costs[pos][last][ii] = solvecost(pos + 1, last, ii) + D;

  int minz = max(0, (last < 256 ? last - M : 0));
  int maxz = min(255, (last < 256 ? last + M : 255));
  for (int z = minz; z <= maxz; z++) {
    costs[pos][last][ii] = min(costs[pos][last][ii], solvecost(pos + 1, z, ii) + abs(z - values[pos]));
    costs[pos][last][ii] = min(costs[pos][last][ii], solvecost(pos, z, ii + 1) + I);
  }
  
  return costs[pos][last][ii];
}
int solving() {
  cin >> D >> I >> M >> N;
  for (int x = 0; x < N; x++) {
    cin >> values[x];
    for (int y = 0; y < 257; y++) {
      for (int ii = 0; ii < 257; ii++) {
        costs[x][y][ii] = -1;
      }
    }
  }
  return solvecost(0, 256, 0);
}
int main() {
  int t;
  cin >> t;
  for (int x = 1; x <= t; x++) cout << "Case #" << x << ": " << solving() << endl;
  return 0;
}

