#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cassert>
#include <cstdlib>
#include <ctime>

using namespace std;
typedef long long int64;
#define E(c) cerr<<#c
#define Eo(x) cerr<<#x<<" = "<<(x)<<endl


const int K = 20000;

int n;
int arr[1024];
int cnt[K];

bool Solve(int minl) {
	memset(cnt, 0, sizeof(cnt));
	for (int i = 0; i<n; i++) cnt[arr[i]]++;

	vector<int> rights;
	
	for (int i = 0; i<K; i++) {
		for (int j = 0; j<rights.size(); j++) if (rights[j] == i) {
			if (cnt[i]) {
				cnt[i]--;
				rights[j]++;
			}
		}

		if (!cnt[i]) {
			int t = 0;
			for (int j = 0; j<rights.size(); j++) if (rights[j] != i)
				rights[t++] = rights[j];
			rights.resize(t);
		}

		if (cnt[i]) {
			int k = cnt[i];
			for (int u = i; u<i+minl; u++) {
				cnt[u] -= k;
				if (cnt[u] < 0) return false;
			}
			for (int u = 0; u<k; u++) rights.push_back(i+minl);
		}
	}
	return true;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests;
	scanf("%d", &tests);
	for (int tt = 1; tt<=tests; tt++) {
		
		scanf("%d", &n);
		for (int i = 0; i<n; i++) scanf("%d", arr+i);

		int left;
		if (n > 0) {
			left = 1;
			int right = 1024;
			while (right - left > 1) {
				int middle = (right+left) >> 1;
				if (Solve(middle)) left = middle;
				else right = middle;
			}
		}
		else left = 0;

		printf("Case #%d: %d\n", tt, left);
		fflush(stdout);
	}
	return 0;
}
