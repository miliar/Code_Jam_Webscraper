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
int dm[12][1100][12];
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int ntests;
	scanf("%d", &ntests);
	for (int itest = 1; itest <= ntests; itest++) {
		printf("Case #%d: ", itest);	
		int r = 0;
		scanf("%d", &r);
		int n = (1 << r);
		memset(dm, 63, sizeof(dm));
		int inf = dm[0][0][0];
		for (int i = 0; i < n; i++) {
			int t;
			scanf("%d", &t);
			for (int j = 0; j <= t; j++) {
				dm[0][i][j] = 0;
			}
		}
		for (int i = 1, k = n / 2; i <= r; i++, k >>= 1) {
			for (int j = 0; j < k; j++) {
				int p;
				scanf("%d", &p);
				for (int rem = 0; rem <= r; rem++) {
					int v1 = p + dm[i - 1][j + j][rem] + dm[i - 1][j + j + 1][rem];
					int v2 = dm[i - 1][j + j][rem + 1] + dm[i - 1][j + j + 1][rem + 1];
					dm[i][j][rem] = min(dm[i][j][rem], min(v1, v2));
				}
			}
		}
		int res = inf;
		for (int rem = 0; rem <= r; rem++) {
			res = min(res, dm[r][0][rem]);
		}
		printf("%d\n", res);
	}
	return 0;
}