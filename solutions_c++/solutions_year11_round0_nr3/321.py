#include <map>
#include <set>
#include <cmath>
#include <cstdio>
#include <vector>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

vector<int> vec;
int cas, n, mask1, mask2;

int main() {
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	scanf("%d", &cas);
	for (int c = 1; c <= cas; ++c) {
		scanf("%d", &n);
		vec.resize(n);
		mask2 = 0;
		for (int i = 0; i < n; ++i) {
			scanf("%d", &vec[i]);
			mask2 ^= vec[i];
		}
		printf("Case #%d: ", c);
		if (mask2 != 0) {
			printf("NO\n");
		} else {
			mask1 = 0;
			int sum = 0;
			int maxi = 1000000000;
			for (int i = 0; i < n; ++i) {
				maxi = min(maxi, vec[i]);
				sum += vec[i];
			}
			sum -= maxi;
			printf("%d\n", sum);
		}
	}
	return 0;
}