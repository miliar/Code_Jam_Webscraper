#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <queue>
#include <cmath>
#include <map>
#include <set>
#include <cctype>
#include <iostream>
#include <sstream>
using namespace std;

int D , C;
struct Node {
	int pos , num;
	bool operator < (Node cmp) const {
		return pos < cmp.pos;
	}
}hh[222];


bool ok(double t) {
	double Left = -1e20;
	for (int i = 0 ; i < C ; i ++) {
		for (int j = 0 ; j < hh[i].num ; j ++) {
			Left = max(Left + D, hh[i].pos - t);
			if(Left > hh[i].pos + t) return false;
		}
	}
	return true;
}
int main() {
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T;
	scanf("%d",&T);
	for (int cas = 1 ; cas <= T ; cas ++) {
	
		scanf("%d%d",&C,&D);
		double sum = 0;
		for (int i = 0 ; i < C ; i ++) {
			scanf("%d%d",&hh[i].pos , &hh[i].num);
			sum += hh[i].num;
		}
		sort(hh , hh + C);
		double lo = 0;
		double hi = sum * D;
		int tt = 100;
		while (tt --) {
			double mid = (lo + hi) / 2;
			if (ok(mid)) hi = mid;
			else lo = mid;
		}
		printf("Case #%d: %.10lf\n" , cas , hi);
	}
	return 0;
}