#define _CRT_SECURE_NO_DEPRECATE

#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>

using namespace std;

template<class T> T sqr(const T& a) {
	return a * a;
}
template<class T> int size(const T& a) {
	return (int)a.size();
}
bool connectedX(const int x1,const int x2,const int x3,const int x4) {
	return x2 >= x3 && x4 >= x1;
}
struct SRect {
	int x1, y1, x2, y2;
	void scan() {
		scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
	}
	bool connected(const SRect &r) const {
		return connectedX(x1 - 1, x2 + 1, r.x1, r.x2) && connectedX(y1 - 1, y2 + 1, r.y1, r.y2);
	}
} rect[1010];
int was[1010];
int n;
void dfs(int i, int &x2, int &y2, int lab) {
	was[i] = lab;
	for (int j = 0; j < n; j++) {
		if (was[j] != -1) continue;
		if (rect[i].connected(rect[j])) {
			if (rect[j].x2 > x2) {
				x2 = rect[j].x2;
			}
			if (rect[j].y2 > y2) {
				y2 = rect[j].y2;
			}
			dfs(j, x2, y2, lab);
		}
	}
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int ntests;
	scanf("%d", &ntests);
	for (int itest = 1; itest <= ntests; itest++) {
		printf("Case #%d: ", itest);
		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			rect[i].scan();
			was[i] = -1;
		}
		int ans = -1;
		for (int i = 0; i < n; i++) {
			if (was[i] != -1) continue;
			int x2 = rect[i].x2, y2 = rect[i].y2;
			dfs(i, x2, y2, i);
			int res = 0;
			for (int j = 0; j < n; j++) {
				if (was[j] == i) {
					res = max(res, x2 - rect[j].x1 + y2 - rect[j].y1);
				}
			}
			ans = max(ans, res);
		}
		printf("%d\n", ans + 1);
	}
	return 0;
}