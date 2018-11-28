/*
 * =========================================================
 *       Filename:  B.cpp
 *    Description:  
 *        Created:  2011/5/22 1:01:27
 *         Author:  rocket323
 * =========================================================
 */
#include <stdio.h>
#include <cstring>
#include <sstream>
#include <iostream>
#include <math.h>
#include <algorithm>
#define eps (1e-8)
#define maxl 1000010
using namespace std;

int n, d, c;
double list[maxl], a[maxl];

bool check(double len) {
	for(int i=0; i<n; ++i) a[i] = list[i];
	a[0] -= len;
	for(int i=1; i<n; ++i) {
		if(a[i] < a[i-1] - eps) {
			double cost = d + fabs(a[i] - a[i-1]);
			if(cost > len + eps) return 0;
			else a[i] = a[i-1] + d;
		}
		else {
			double dist = fabs(a[i] - a[i-1]);
			if(dist < d) {
				double cost = d - dist;
				if(cost > len + eps) return 0;
				else a[i] = a[i-1] + d;
			}
			else {
				double left = dist - d;
				if(left > len) left = len;
				a[i] -= left;
			}
		}
	}
	return 1;
}

int main() {
	int t;
	scanf("%d", &t);
	for(int q=1; q<=t; ++q) {
		scanf("%d%d", &c, &d);
		n = 0;
		for(int i=0; i<c; ++i) {
			int p, v;
			scanf("%d%d", &p, &v);
			for(int j=0; j<v; ++j) list[n++] = (double)p;
		}

		double l = 0.0, r = 1e12, mid, ans = -1.0;
		while(l <= r - eps) {
			mid = (l + r) / 2.0;
			if(check(mid)) {
				ans = mid;
				r = mid - eps;
			}
			else l = mid + eps;
		}
		printf("Case #%d: %.8lf\n", q, ans);
	}
	return 0;
}

