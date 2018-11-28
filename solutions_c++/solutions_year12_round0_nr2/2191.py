#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>

using namespace std;

bool survive(int score, int target) {
	if (score >= target + 2 * (max(0, target - 1))) {
		return true;
	}
	return false;
}

bool surprise(int score, int target) {
	if (score >= target + 2 * (max(0, target - 2))) {
		return true;
	}
	return false;
}

int main() {
	int T; cin >> T;
	for (int t = 0; t < T; t++) {
		int N, S, p;
		cin >> N >> S >> p;
		vector<int> data;
		for (int i = 0; i < N; i++) {
			int val; cin >> val;
			data.push_back(val);
		}
		int count = 0;
		for (int i = 0; i < data.size(); i++) {
			if (survive(data[i],p)) {
				count++;
				continue;
			}
			if (S > 0 && surprise(data[i],p)) {
				count++;
				S--;
				continue;
			}
		}
		cout << "Case #" << (t+1) << ": " << count << "\n";
	}
	return 0;
}