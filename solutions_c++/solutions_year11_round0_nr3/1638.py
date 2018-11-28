#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <string>
#define out(v) cout << #v << ": " << (v) << endl
using namespace std;
typedef long long LL;

int T, N, C[1005];

int main() {
	cin >> T;
	for (int id = 1; id <= T; ++id) {
		cin >> N;
		int sum = 0, ans = 0;
		for (int i = 0; i < N; ++i)
			cin >> C[i], sum ^= C[i], ans += C[i];
		sort(C, C + N);
		cout << "Case #" << id << ": ";
		if (sum == 0) {
			cout << ans - C[0] << endl;
		} else {
			cout << "NO" << endl;
		}
	}
	return 0;
}
