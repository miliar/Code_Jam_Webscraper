#define _CRT_SECURE_NO_DEPRECATE

#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <iostream>
#include <sstream>

using namespace std;

template<class T> T sqr(const T& a) {
	return a * a;
}
template<class T> int size(const T& a) {
	return (int)a.size();
}
int dm[100100];
int a[100];
set<pair<int, int>> heap;
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int ntests;
	scanf("%d", &ntests);
	for (int itest = 1; itest <= ntests; itest++) {
		printf("Case #%d: ", itest);
		long long l;
		cin >> l;
		int n;
		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			scanf("%d", &a[i]);
		}
		sort(a, a + n);
		reverse(a, a + n);
		long long res = l / a[0];
		int len = l % a[0];
		memset(dm, 127, sizeof(dm));
		int inf = dm[0];
		dm[0] = 0;
		heap.clear();
		heap.insert(make_pair(0, 0));
		while (size(heap)) {
			int i = heap.begin()->second;
			heap.erase(heap.begin());
			for (int j = 1; j < n; j++) {
				if (i + a[j] < a[0]) {
					if (dm[i + a[j]] > dm[i] + 1) {
						heap.erase(make_pair(dm[i + a[j]], i + a[j]));
						dm[i + a[j]] = dm[i] + 1;
						heap.insert(make_pair(dm[i + a[j]], i + a[j]));
					}
				} else {
					if (dm[i + a[j] - a[0]] > dm[i]) {
						heap.erase(make_pair(dm[i + a[j] - a[0]], i + a[j] - a[0]));
						dm[i + a[j] - a[0]] = dm[i];
						heap.insert(make_pair(dm[i + a[j] - a[0]], i + a[j] - a[0]));
					}
				}
			}
		}
		if (dm[len] < inf) {
			cout << res + dm[len] << endl;
		} else {
			cout << "IMPOSSIBLE\n";
		}
	}
	return 0;
}