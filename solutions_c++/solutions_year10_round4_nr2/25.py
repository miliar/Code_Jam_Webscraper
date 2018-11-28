#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

int P;
int M[1024];
vector<int> price[10];

long long INF = 2000000000LL;
long long memo[16][1024][16];

long long solve(int lv, int x, int have) {
  if(lv == -1) return P - have <= M[x] ? 0 : INF;
  long long& ref = memo[lv][x][have];
  if(ref != -1) return ref;

  ref = solve(lv - 1, 2 * x, have) + solve(lv - 1, 2 * x + 1, have);
  ref = min(ref, solve(lv - 1, 2 * x, have + 1) +
                 solve(lv - 1, 2 * x + 1, have + 1) + price[lv][x]);
  return ref;
}

int main() {
  int T; cin >> T;
  for(int t = 1; t <= T; t++) {
    cin >> P;
    for(int i = 0; i < 1 << P; i++) cin >> M[i];
    for(int i = 0; i < P; i++) {
      price[i].clear();
      for(int j = 0; j < 1 << (P - i - 1); j++) {
        int x; cin >> x;
        price[i].push_back(x);
      }
    }
    memset(memo, -1, sizeof(memo));
    int result = solve(P - 1, 0, 0);
    cout << "Case #" << t << ": " << result << endl;
  }
}
