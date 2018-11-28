#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <cstdlib>
#include <queue>
using namespace std;

#define N 1010000
typedef long long ll;
int xx, a[N], n, c, L, tx, x[N];
ll t, ans;

void open() {
	freopen("B.txt", "r", stdin);
	freopen("B2.txt", "w", stdout);
}

int main() {
	priority_queue<int> pq;
	pq.push(1);
	pq.push(2);
	cout << pq.top() << endl;
	//open();
	xx = 1;
	scanf("%d", &tx);
	while (tx--) {
		scanf("%d%lld%d%d", &L, &t, &n, &c);
		for (int i = 0; i < c; i++) {
			scanf("%d", &x[i]);
		}
		int num = 0;
		while (num < n) {
			a[num] = x[num%c];
			num++;
		}
		ans = 0LL;
		for (int i = 0; i < n; i++) ans+=(ll)a[i] * 2LL;
		bool started = 0;
			int maxi = 0, cnt = 0;
			for (int i = 0; i < n; i++) {
				if (started) {
					maxi = max(maxi, a[i]);
				}
				else if (cnt + a[i] * 2 > t) {
					maxi = max(maxi, a[i] - (t - cnt)/2);
					started = 1;
				}
				else {
					cnt += a[i] * 2;
				}
			}
			ans -= maxi;
		}
		else if (L == 2) {
			int maxi = 0, maxi2 = 0, cnt = 0;
			for (int i = 0; i < n; i++) {
				if (started) {
					if (maxi < a[i]) {
						maxi2 = maxi;
						maxi = a[i];
					}
					else if (maxi2 < a[i]) maxi2 = a[i];
				}
				else if (cnt + a[i] * 2 > t) {
					maxi = a[i] - (t - cnt)/2;
					started = 1;
				}
				else {
					cnt += a[i] * 2;
				}
			}
			ans -= maxi + maxi2;
		}
		printf("Case #%d: ", xx++);
		printf("%d\n", ans);
	}
	return 0;
}