/*
 * =========================================================
 *       Filename:  A.cpp
 *    Description:  
 *        Created:  2011/6/4 22:13:48
 *         Author:  rocket323
 * =========================================================
 */
#include <stdio.h>
#include <cstring>
#include <sstream>
#include <math.h>
#include <iostream>
#include <algorithm>
using namespace std;
#define eps 1e-8

int x, s, r, t, n, a[2010], b[2010], w[2010], p;
double _left, ans;
int id[2010], m;

struct node
{
	int a, b, c;
}
E[4080];

void calc(int len, int w, int ed) {
	if(fabs(_left) < eps) {
		ans += len * 1.0 / (s + w);
		p = ed;
	}
	else {
		double tmp = len * 1.0 / (r + w);
		if(tmp <= _left) {
			_left -= tmp;
			ans += len * 1.0 / (r + w);
		}
		else {
			ans += _left;
			ans += (len - (r + w) * _left) * 1.0 / (s + w);
			_left = 0;
		}
		p = ed;
	}
}

bool cmp(node A, node B) {
	return A.c < B.c;
}

int main() {
	int T;
	scanf("%d", &T);
	for(int q=1; q<=T; ++q) {
		scanf("%d%d%d%d%d", &x, &s, &r, &t, &n);
		for(int i=0; i<n; ++i) {
			scanf("%d%d%d", &a[i], &b[i], &w[i]);
		}

		a[n] = b[n-1];
		b[n] = x;
		w[n++] = 0;

		m = 0;
		p = 0;
		for(int i=0; i<n; ++i) {
			E[m].a = p; E[m].b = a[i]; E[m++].c = 0;
			E[m].a = a[i]; E[m].b = b[i]; E[m++].c = w[i];
			p = b[i];
		}

		//for(int i=0; i<m; ++i) printf("%d %d %d\n", E[i].a, E[i].b, E[i].c);

		sort(E, E + m, cmp);

		ans = 0.0, _left = t;
		p = 0;

		for(int i=0; i<m; ++i) {
			if(E[i].b > E[i].a) calc(E[i].b - E[i].a, E[i].c, 0);
		}

		printf("Case #%d: %.9lf\n", q, ans);
	}
	return 0;
}

