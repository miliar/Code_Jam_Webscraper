#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

void solve() {
	int N;
	scanf("%d", &N);

	vector<int> candies;
	for(int i = 0; i < N; ++i) {
		int inp;
		scanf("%d", &inp);
		candies.push_back(inp);
	}

	sort(candies.begin(), candies.end());

	int result = 0;
	for(int i = 0; i < candies.size(); ++i) {
		result ^= candies[i];
	}

	if (result != 0) {
		printf("NO\n");
	}
	else {
		result = 0;
		for(int i = 1; i < candies.size(); ++i) {
			result = result + candies[i];
		}
		printf("%d\n", result);
	}
}

int main() {
	freopen("C:\\Users\\kiheon\\Downloads\\C-large.in", "r", stdin);
	freopen("C:\\workspace\\AOJ [C++]\\src\\output.txt", "w", stdout);
	int z;
	scanf("%d", &z);

	for (int i = 0; i < z; ++i) {
		printf("Case #%d: ", i + 1);
		solve();
	}

	return 0;
}
