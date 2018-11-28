#include <iostream>
#include <cstdlib>
#include <vector>
using namespace std;


int solve(vector<int>& c) {
  int ans = 0;
  int sum = 0;
  int minv = c[0];
  for (size_t i = 0; i < c.size(); i++) {
	sum += c[i];
	ans ^= c[i];
	minv = min(minv, c[i]);
  }
  return ans == 0 ? sum - minv : -1;
}

int main() {
  int T;
  cin >> T;
  for (int i = 0; i < T; i++) {
	vector<int> c;
	int N;
	cin >> N;
	for (int j = 0; j < N; j++) {
	  int t;
	  cin >> t;
	  c.push_back(t);
	}
	int ans = solve(c);
	cout << "Case #" << i + 1 << ": ";
	if (ans == -1) cout << "NO" << endl;
	else cout << ans << endl;

  }
  return 0;
}
