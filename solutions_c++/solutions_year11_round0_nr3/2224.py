#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void candysplit(int N, vector<int> C) {
	unsigned int x = 0;
	for (int j = 0; j < N; ++j)
		x ^= C[j];
	if (x != 0)
		cout << "NO";
	else {
		sort(C.begin(), C.begin()+N);
		int sum = 0;
		for (int j = 1; j < N; ++j)
			sum += C[j];
		cout << sum;
	}

	cout << "\n";
}

int main() {

  int T, N;
  cin >> T;
  vector<int> C;
  C.resize(1000);
  for (int c=0; c < T; ++c) {
	cin >> N;
	for (int j = 0; j < N; ++j) {
		cin >> C[j];
	}
	cout << "Case #" << c+1 << ": ";
	candysplit(N, C);   
  }

}
