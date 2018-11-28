#include <iostream>
#include <algorithm>
#include <string>
#include <sstream>
#include <vector>
#include <queue>

using namespace std;

int main() {
	int numTest;
	cin >> numTest;
	for (int i = 0; i < numTest; i++) {
		int k;
		cin >> k;
		vector<int> vec1;
		for (int j = 0; j < k; j++) {
			int v; cin >> v; vec1.push_back(v);
		}
		vector<int> vec2;
		for (int j = 0; j < k; j++) {
			int v; cin >> v; vec2.push_back(v);
		}
		sort(vec1.begin(),vec1.end());
		sort(vec2.begin(),vec2.end());
		int sum = 0;
		for (int j = 0; j < vec1.size(); j++) {
			sum = sum + vec1[j]*vec2[vec2.size()-j-1];
		}
		cout << "Case #" << i+1 << ": " << sum << "\n";
	}
	return 0;
}