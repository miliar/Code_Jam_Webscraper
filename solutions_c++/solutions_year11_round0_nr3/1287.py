#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <utility>
#include <algorithm>
#include <numeric>
#include <string>
using namespace std;
int main() {
	ifstream cin("test.txt");
	ofstream cout("out.txt");
	int tests; cin >> tests;
	for (int test = 0; test < tests; ++test) {
		int N; cin >> N;
		vector<int> v(N);
		int x = 0;
		for (int i = 0; i < N; ++i) {
			cin >> v[i];
			x ^= v[i];
		}
		if (x != 0 || N < 2) {
			cout << "Case #" << (test + 1) << ": NO" << endl;
		} else {
			int r = accumulate(v.begin(), v.end(), 0)-*min_element(v.begin(), v.end());
			cout << "Case #" << (test + 1) << ": " << r << endl;
		}
	}
	//system("pause");
}