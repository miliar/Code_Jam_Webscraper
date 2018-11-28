#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int T;
int P, Q;
vector<int> list;
vector<int> S;
int opt[101][101];
int w[101][101];

int calc(int i, int j) {
  if (i == j) {
    return S[i];
  }
  if (opt[i][j] != -1) {
    return opt[i][j];
  }
  opt[i][j] = 0x7fffffff;
  for (int k = i; k < j; k++) {
    opt[i][j] = min(opt[i][j], (calc(i, k) + calc(k + 1, j) + w[i][j]));
  }
  return opt[i][j];
}

void work() {
  cin >> P >> Q;
  list = vector<int>(Q);
  for (int i = 0; i < Q; i++) {
    cin >> list[i];
  }
  list.push_back(0);
  list.push_back(P + 1);
  sort(list.begin(), list.end());
  S = vector<int>();
  for (int i = 1; i < (int) list.size(); i++) {
    S.push_back(list[i] - list[i - 1] - 1);
  }
  int n = S.size();
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      opt[i][j] = -1;
      w[i][j] = j - i - 1;
      for (int k = i; k <= j; k++) {
	w[i][j] += S[k];
      }
    }
  }
  cout << calc(0, n - 1) - P + Q;
}

int main() {
  cin >> T;
  for (int i = 1; i <= T; i++) {
    cout << "Case #" << i << ": ";
    work();
    cout << endl;
  }
  return 0;
}
