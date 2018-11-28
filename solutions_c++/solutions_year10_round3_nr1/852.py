#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

const int MAXN = 1009;
struct Point {
	int x, y;
	Point() {}
	Point(int x_, int y_) : x(x_), y(y_) {}
};

Point pt[MAXN];
int N;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int i, j, T, cas = 0, ans;
	scanf("%d", &T);
	while (T--) {
		scanf("%d", &N);
		for (i = 0; i < N; ++i) {
			scanf("%d%d", &pt[i].x, &pt[i].y);
		}
		ans = 0;
		for (i = 0; i < N; ++i) {
			for (j = i + 1; j < N; ++j) {
				if ((pt[i].x < pt[j].x && pt[i].y > pt[j].y) ||
					(pt[i].x > pt[j].x && pt[i].y < pt[j].y)) {
					++ans;
				}
			}
		}
		printf("Case #%d: %d\n", ++cas, ans);
	}
	return 0;
}
