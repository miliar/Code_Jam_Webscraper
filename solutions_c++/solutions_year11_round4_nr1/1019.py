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

struct Node {
	int b , e , w;
	bool operator < (Node &cmp) const {
		return w < cmp.w;
	}
}hh[1111];
int main() {
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T , cas = 1;
	scanf("%d",&T);
	while (T --) {
		int X , S , R , t , N;
		scanf("%d%d%d%d%d",&X,&S,&R,&t,&N);
		double tot = X;
		for (int i = 0 ; i < N ; i ++) {
			scanf("%d%d%d",&hh[i].b,&hh[i].e,&hh[i].w);
			tot -= (hh[i].e - hh[i].b);
		}
		sort(hh , hh + N);
		double remain = t;
		double cost = 0;
		double speedR = R;
		double speedS = S;
		if (tot / speedR >= remain) {
			cost += remain;
			tot -= remain * speedR;
			remain = 0;
			cost += tot / speedS;
			tot = 0;
		} else {
			cost += tot / speedR;
			remain -= tot / speedR;
			tot = 0;
		}
		for (int i = 0 ; i < N ; i ++) {
			double tot = (hh[i].e - hh[i].b);
			double speedR = R + hh[i].w;
			double speedS = S + hh[i].w;
			if (tot / speedR >= remain) {
				cost += remain;
				tot -= remain * speedR;
				remain = 0;
				cost += tot / speedS;
				tot = 0;
			} else {
				cost += tot / speedR;
				remain -= tot / speedR;
				tot = 0;
			}
		}
		printf("Case #%d: %.10lf\n",cas ++ , cost);
	}
	return 0;
}