#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#define ST first
#define ND second
#define MP make_pair
#define PB push_back
using namespace std;
typedef pair<int, int> PI;
typedef vector<int> VI;
typedef long long LL;
typedef double LF;
const int INF = 1000000100;
const int MAXN = 100010;

int t, tt, n, D, uch[11111], l[11111], d[11111];

int main () {
	scanf("%d", &t);
	while (t--) {
		scanf("%d", &n);
		for (int i=1; i<=n; i++)
			scanf("%d %d", &d[i], &l[i]);
		scanf("%d", &D);
		uch[1] = d[1];
		bool res = false;
		for (int i=2; i<=n; i++)
			uch[i] = 0;
		for (int i=1; i<=n; i++) {
		//	printf("%d %d\n", i, uch[i]);
			for (int j=i+1; j<=n && d[j] <= uch[i] + d[i]; j++)
				uch[j] = max(uch[j], min(l[j], d[j] - d[i]));
			if (d[i] + uch[i] >= D)
				res = true;
		}
		if (res)
			printf("Case #%d: YES\n", ++tt);
		else
			printf("Case #%d: NO\n", ++tt);
	}
}

