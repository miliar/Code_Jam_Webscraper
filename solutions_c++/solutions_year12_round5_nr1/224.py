#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
#include <queue>
#include <map>
#include <set>
#include <ctime>
#define MAXN 1003
using namespace std;
const int INF = 0x3f3f3f3f;
const double eps = 1e-9;
typedef long long LL;
typedef pair<int, int> pii;

int l[MAXN];
int p[MAXN];
int n;
pii tmp[MAXN];

int main() {
#ifndef ONLINE_JUDGE
//	freopen("in", "r", stdin);
//	freopen("out", "w", stdout);
#endif

	int dataset;
	scanf("%d", &dataset);
	for(int cas=1; cas<=dataset; ++cas) {
		scanf("%d", &n);
		for(int i=0; i<n; ++i) {
			scanf("%d", &l[i]);
		}
		for(int i=0; i<n; ++i) {
			scanf("%d", &p[i]);
			tmp[i].first = -p[i];
			tmp[i].second = i;
		}
		sort(tmp, tmp+n);

		printf("Case #%d:", cas);
		for(int i=0; i<n; ++i) {
			printf(" %d", tmp[i].second);
		}
		putchar(10);
	}

	return 0;
}
