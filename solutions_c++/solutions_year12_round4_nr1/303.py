#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#define LS(p) ((p)<<1)
#define RS(p) ( (LS(p))|1)
#define MID(l,r) ( ((l) + (r) ) >> 1 )
#define MAXN 10003
#define INF 0x3f3f3f3f
#define MAXD 17
using namespace std;

struct Data {
	int d, l;
	int pre;
	bool operator<(const Data &t) const {
		return d<t.d;
	}
}data[MAXN];

int n;
int dis;

bool solve() {
	sort(data+1, data+n);
	data[0].pre = 0;
	int p = 1;
	for(int i=0; i<n; ++i) {
		if(data[i].pre == INF) {
			continue;
		}
		int next = min(data[i].d - data[i].pre, data[i].l) + data[i].d;
		if(next >= dis) {
			return true;
		}
		while(p<n) {
			if(data[p].d <= next) {
				data[p].pre = min(data[p].pre, data[i].d);
				++p;
			} else {
				break;
			}
		}
	}

	return false;
}

int main() {
//	freopen("in", "r", stdin);
//	freopen("out", "w", stdout);

	int dataset;
	scanf("%d", &dataset);
	for(int cas=1; cas <= dataset; ++cas) {
		scanf("%d", &n);
		for(int i=0; i<n; ++i) {
			scanf("%d %d", &data[i].d, &data[i].l);
			data[i].pre = INF;
		}
		scanf("%d", &dis);
		printf("Case #%d: %s\n", cas, solve()? "YES": "NO");
	}

	return 0;
}

