#include <iostream>
#include <cstdlib>
#include <vector>
using namespace std;

double solve(vector<int>& v) {
  int n = 0;
  for (int i = 0; i < v.size(); i++) {
	if (v[i] != i + 1) n++;
  }
  if (n == 0) return 0.0;
  return (double)n;
}

int main() {
  int T;
  cin >> T;
  for (int i = 0; i < T; i++) {
	int N;
	cin >> N;
	vector<int> v;
	for (int j = 0; j < N; j++) {
	  int t;
	  cin >> t;
	  v.push_back(t);
	}

	cout << "Case #" << i + 1 << ": " << solve(v) << endl;

  }
  return 0;
}
