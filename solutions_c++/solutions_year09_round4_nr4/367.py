#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <queue>
using namespace std;

int main() {
	freopen("output.txt", "w", stdout);
	int cas, cass=0;
	for (scanf("%d", &cas); cas--; ) {
		int n;
		int x[10], y[10], r[10];
		scanf("%d", &n);
		for (int i=0; i<n; ++i) scanf("%d %d %d", &x[i], &y[i], &r[i]);
		double res = 1e10;
		if (n==1) {
			res = min(res, r[0]+0.0);
		}
		if (n==2) {
			res = max(r[0]+0.0, r[1]+0.0);
		}
		for (int i=0; i<n; ++i) {
			for (int j=0; j<i; ++j) {
				double dis = sqrt((x[i]-x[j])*(x[i]-x[j])+(y[i]-y[j])*(y[i]-y[j])+0.0);
				dis += r[i];
				dis += r[j];
				dis /= 2;
				for (int k=0; k<n; ++k) if (k!=i && k!=j) dis = max(dis, r[k]+0.0);
				res = min(res, dis);
			}
		}
		printf("Case #%d: %.9lf\n", ++cass, res);
	}

	return 0;
}