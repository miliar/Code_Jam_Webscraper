#include <cstdio>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;


int main() {
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		int N;
		cin >> N;
		vector<int> C;
		int r = 0;
		int sum = 0;
		int min = 0x7fffffff;
		for (int k = 0; k < N; k++) {
			int t;
			cin >> t;
			r ^= t;
			sum += t;
			if (min > t)
				min = t;
			C.push_back(t);
		}
		
		if (r != 0) {
			printf("Case #%d: NO\n", i+1);
		} else {
			printf("Case #%d: %d\n", i+1, sum-min);
		}

	}

}

