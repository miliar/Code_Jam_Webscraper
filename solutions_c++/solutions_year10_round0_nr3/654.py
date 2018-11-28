#include <iostream>
#include <vector>
#include <deque>

using namespace std;

struct Node {
  int next;
  int sum;
  bool access;
  Node(int n, int s, bool a = false)
    : next(n), sum(s), access(a) {};
};

int main() {
  int T, R, K, N, g;
  int lpstart, lpend, lpstep;
  int pos;
  long long lpsum, res;
  vector<Node> shifts;
  deque<int> G;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    cin >> R >> K >> N;
    shifts.clear();
    G.clear();
    for (int i = 0; i < N; ++i) {
      cin >> g;
      G.push_back(g);
    }
    for (int i = 0; i < N; ++i) {
      int sum = 0, j = 0;
      for (; j < N && sum + G[j] <= K; sum += G[j++]) ;
      G.push_back(G.front());
      G.pop_front();
      shifts.push_back(Node((i + j) % N, sum));
    }
    lpend = 0;
    while (!shifts[lpend].access) {
      shifts[lpend].access = true;
      lpend = shifts[lpend].next;
    }
    lpsum = shifts[lpend].sum;
    lpstart = shifts[lpend].next;
    lpstep = 1;
    while (lpstart != lpend) {
      lpsum += shifts[lpstart].sum;
      lpstart = shifts[lpstart].next;
      lpstep++;
    }
    pos = 0;
    res = 0;
    while (R > 0) {
      if (pos != lpstart) {
        res += shifts[pos].sum;
        pos = shifts[pos].next;
        R--;
      } else {
        res += (R / lpstep) * lpsum;
        R %= lpstep;
        while (R--) {
          res += shifts[pos].sum;
          pos = shifts[pos].next;
        }
      }
    }
    cout << "Case #" << t << ": " << res << endl;
  }
  return 0;
}
