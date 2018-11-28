#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <math.h>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <vector>
#pragma comment (linker, "/STACK:256000000")
using namespace std;
const int mxx = 1000010;
int s[mxx];
void solve() {
	int i,j,n,b,e, wi,x,w,r;
	double t;
	cin >> x >> w >> r >> t >> n;
	for (i=0;i<=x;++i)
		s[i] = 0;

	for (i=1;i<=n;++i) {
		cin >> b >> e >> wi;
		for (j=b;j<e;++j)
			s[j] = wi;

	}
	sort(s,s+x);
	double res = .0, add, len;
	const double eps = 1e-8;
	for (i=0;i<x;++i) {
		add = 1.0 / (s[i] + r + .0);
		if (t - add >= -eps) {
			t -= add;
			res += add;
		}
		else {
			res += t;
			len = 1 - t * (s[i] + r + .0);
			t = 0;
			add = len / (s[i] + w + .0);
			res += add;
		}
	}
	printf("%.9lf\n",res);
}
int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t, tst;
	cin >> t;
	for (tst = 1; tst <= t; ++tst) {
		cout << "Case #" << tst << ": ";
		solve();
	}
	
	return 0;
}