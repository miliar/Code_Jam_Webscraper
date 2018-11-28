#include<iostream>
#include<cstring>
#include<map>
#include<algorithm>
#include<stack>
#include<queue>
#include<cmath>
#include<string>
#include<cstdlib>
#include<vector>
#include<cstdio>
#include<set>
#include<list>
#include<numeric>
#include<cassert>
#include<ctime>
#include<bitset>

using namespace std;

const int MAXN = 1000100;
const double EPS = 1e-8;

int pos[MAXN];
int n, D, C;

bool gao(double t)
{
	double last = pos[0] - t;
	for (int i = 1; i <  n;  i++) {
		double y = last + D;
		if (pos[i] < y) {
			if (pos[i] + t < y) return false;
			last = y;
		} else {
			double tt = min(t, pos[i] - y);
			last = pos[i] - tt;
		}
	}
	return true;
}


int main()
{
#ifndef ONLINE_JUDGE
	freopen("D:\\B-small-attempt0.in","r",stdin ) ;
	freopen("D:\\out.txt","w",stdout ) ;
#endif

	int T, t = 1;
	for (scanf("%d", &T); T--; ) {
		scanf("%d%d", &C, &D);
		n = 0;
		int p, v;
		for (int i = 0; i < C; i++) {
			scanf("%d%d", &p, &v);
			while(v--) {
				pos[n++] = p;
			}
		}
		sort(pos, pos+n);
		double left = 0, right = 1e20;
		int cnt = 0;
		while(cnt++ < 100 && right - left > EPS) {
			double mid = (right + left) / 2.0;
			if (gao(mid)) right = mid;
			else left = mid;
		}
		printf("Case #%d: %.6f\n", t++, (left+right)/2);
	}
	return 0;
}