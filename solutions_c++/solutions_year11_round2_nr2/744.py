#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <string>
#include <iostream>
#include <functional>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <set>

using namespace std;

#define	COUNT(a)	(sizeof(a) / sizeof((a)[0]))

int main(int argc, char *argv[])
{
	int nc, ci;
	
	scanf("%d", &nc);
	for (ci = 1; ci <= nc; ci++) {
		int i, j, k, d, c, total = 0;
		scanf("%d %d", &c, &d);
		
		vector<pair<int, int> > a;
		for (i = 0; i < c; i++) {
			int p, v;
			scanf("%d %d", &p, &v);
			a.push_back(make_pair(p, v));
			total += v;
		}
		
		sort(a.begin(), a.end());
		double ans = 0;
		for (i = 0; i < c; i++) {
			for (j = 0; j <= i; j++) {
				int len = a[i].first - a[j].first;
				int n = 0;
				for (k = j; k <= i; k++) n += a[k].second;
				if (len >= (n - 1) * d) continue;
				if (n <= 1) continue;
				double t = (double) ((n - 1) * d - len) / 2.0;
				// printf("%d - %d: %f (n = %d)\n", i, j, t, n);
				if (t > ans) ans = t;
			}
		}
	
		printf("Case #%d: %f\n", ci, ans);
	}
	
	return 0;
}
