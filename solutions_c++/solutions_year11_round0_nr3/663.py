#include <cstdio>
#include <algorithm>
#include <cstring>
#include <iostream>
#include <vector>
#include <set>
#include <string>
#include <map>

using namespace std;

int N, T;

int mem[1005];

int main() {
	cin >> T;
	for(int t = 1 ; t <= T ; t++) {
		cin >> N;
		int x = 0;
		int sum = 0;
		int m = (1 << 26);
		for(int a, i = 0 ; i < N ; i++) {
			cin >> a;
			x ^= a;
			sum += a;
			m = min(m, a);
		}
		cout << "Case #" << t << ": ";
		if (x != 0) {
			cout << "NO" << endl;
		}	else {
			cout << (sum - m) << endl;
		}
	}
	return 0;
}
