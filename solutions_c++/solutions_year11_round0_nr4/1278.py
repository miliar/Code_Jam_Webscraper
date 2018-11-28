#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <utility>
#include <algorithm>
#include <functional>
#include <numeric>
#include <string>
using namespace std;
int main() {
	ifstream cin("test.txt");
	ofstream cout("out.txt");
	int tests; cin >> tests;
	for (int test = 0; test < tests; ++test) {
		int N; cin >> N;
		vector<int> v(N), w(N);
		for (int i = 0; i < N; ++i) cin >> v[i];
		w = v; sort(w.begin(), w.end());
		transform(v.begin(), v.end(), w.begin(), v.begin(), equal_to<int>());
		cout << "Case #" << (test + 1) << ": " << N - accumulate(v.begin(), v.end(), 0) << endl;
	}
	//system("pause");
}