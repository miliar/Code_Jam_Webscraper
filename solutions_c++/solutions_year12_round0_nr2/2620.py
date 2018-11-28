#include <vector>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
const int maxn = 100 + 5;
int T, N, S, p;

inline int v0(int t) {
	if (t == 0) return 0;
	return 1 + (t - 1) / 3;
}
inline int v1(int t) {
	if (t <= 1) return t;
	return 2 + (t - 2) / 3;
}

int main() {
	scanf("%d", &T);
	for (int index = 1; index <= T; ++index) {
		scanf("%d%d%d", &N, &S, &p);
		vector<int> iv;
		for (int i = 0, t; i < N; ++i) {
			scanf("%d", &t);
			iv.push_back(t);
		}
		int ans = 0;
		for (vector<int>::iterator it = iv.begin(); it != iv.end() && S; ++it)
			if (v0(*it) < p && v1(*it) >= p) {
				iv.erase(it);
				it = iv.begin();
				--S;
				++ans;
			}
		for (vector<int>::iterator it = iv.begin(); it != iv.end(); ++it)
			if (v0(*it) >= p)
				++ans;
		printf("Case #%d: %d\n", index, ans);
	}
	return 0;
}
