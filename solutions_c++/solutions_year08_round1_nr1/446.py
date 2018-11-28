#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>

using namespace std;


vector<int> v1;
vector<int> v2;


int main() {
	int T, n;
	
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cin >> n;
		v1.clear();
		v2.clear();
		for (int i = 0; i < n; i++) {
			int temp;
			cin >> temp;
			v1.push_back(temp);
		}
		for (int i = 0; i < n; i++) {
			int temp;
			cin >> temp;
			v2.push_back(temp);
		}
		sort(v1.begin(), v1.end());
		sort(v2.begin(), v2.end());
		long long score = 0;
		for (int i = 0; i < n; i++) {
			score += (long long)v1[i] * v2[n - 1 - i];
		}
		cout << "Case #" << t << ": " << score << endl;
	}
}




