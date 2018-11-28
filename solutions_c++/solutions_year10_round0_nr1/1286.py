#include <iostream>
#include <cstdio>

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		int n, k;
		cin >> n >> k;
		
		bool snapers[n];
		for (int i = 0; i < n; i++) snapers[i] = 0;
		
		for (int i = 0; i < k; i++) {
			for (int j = 0; j < n; j++) {
				if (!snapers[j]) {
					snapers[j] = 1;
					break;
				}
				snapers[j] = 0;
			}
		}
		
		bool all = true;
		for (int i = 0; i < n; i++)
			if (!snapers[i])
				all = false;
		
		cout << "Case #" << t + 1 << ": " << (all ? "ON" : "OFF") << endl;
	}
}

