#include <iostream>
#include <algorithm>
#include <map>
using namespace std;

struct point {
	int x, y;
} pnt[1024];

int main() {
	int t, n, tc = 0;
	freopen("E://in.txt", "r", stdin);
	freopen("E://out.txt", "w", stdout);
	scanf("%d", &t);
	while(t--) {
		scanf("%d", &n);
		int ans = 0;
		for(int i = 0; i < n; i++) scanf("%d%d", &pnt[i].x, &pnt[i].y);
		for(int i = 0; i < n; i++) {
			for(int j = i + 1; j < n; j++) {
				if(pnt[i].x > pnt[j].x && pnt[i].y < pnt[j].y || pnt[i].x < pnt[j].x && pnt[i].y > pnt[j].y) {
					ans++;
				}
			}
		}
		printf("Case #%d: %d\n", ++tc, ans);
	}
	return 0;
}