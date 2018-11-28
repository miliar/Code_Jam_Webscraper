#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <cassert>
#include <ctime>
#include <algorithm>
#include <queue>
#include <memory.h>
#include <stack>

using namespace std;

#define pb push_back
#define mp make_pair
#define fir first
#define fi first
#define sec second
#define y1 botva23
typedef long long int64;
typedef long double ld;

const int inf = 2000000000;
const ld eps = 1e-07;

int n;
int d[70000];
int l[70000];
int x;
int a[70000];

void solve() {
	scanf("%d", &n);
	for (int i = 0; i < n; ++i)
		scanf("%d %d", &d[i], &l[i]);
	scanf("%d", &x);
	for (int i = 0; i < n; ++i)
		a[i] = 0;
	a[0] = d[0];
	bool f = false;
	for (int i = 0; i < n; ++i) {
		if (d[i] + a[i] >= x) {
			f = true;
			break;
		}
		for (int j = i + 1; j < n; ++j) {
			if (d[i] + a[i] < d[j])
				break;
			a[j] = max(a[j], min(d[j] - d[i], l[j]));	
		}
	}
	if (f)
		printf("YES\n");
	else printf("NO\n");
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}