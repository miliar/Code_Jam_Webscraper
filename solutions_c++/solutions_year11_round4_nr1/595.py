#include <cstdio>
#include <vector>
#include <cstring>
#include <string>
#include <map>
#include <utility>
#include <algorithm>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <cmath>

using namespace std;

pair<int,int> wi[2000];
int main(void) {
	int tx;
	scanf("%d",&tx);
	for (int tc=1; tc<=tx; ++tc) {
		int x,s,r,t,n;
		scanf("%d%d%d%d%d",&x,&s,&r,&t,&n);
		int w0 = x;
		for (int i=0; i<n; ++i) {
			int b,e;
			scanf("%d%d%d",&b,&e,&(wi[i].first));
			w0 -= wi[i].second = e-b;
		}
		wi[n++] = make_pair(0,w0);
		sort(wi,wi+n);
		long double ret=0;
		long double tsa = t;
		for (int i=0; i<n; ++i) {
			if (wi[i].second == 0) continue;
			long double ts = ((long double)wi[i].second) / (wi[i].first+r);
			if (ts > tsa) {
				long double dist = wi[i].second - tsa*(wi[i].first+r);
				ret += tsa;
				tsa = 0.0;
				ts = dist / (wi[i].first+s);
			} else {
				tsa -= ts;
			}
			ret += ts;
		}
		printf("Case #%d: %.9lf\n",tc,(double)ret);
	}
	return 0;
}
