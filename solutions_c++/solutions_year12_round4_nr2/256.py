#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#define MAXN 1003
#define INF 0x3f3f3f3f
using namespace std;

int n, w, l;
struct Data {
	int r, p;
	int x, y;
	void format() {
		x = max(x, 0);
		x = min(x, w);
		y = max(y, 0);
		y = min(y, l);
	}
	bool operator<(const Data &t) const {
		return r>t.r;
	}
}data[MAXN];

bool intersect(int s1, int e1, int s2, int e2) {
	int s = max(s1, s2);
	int e = min(e1, e2);
	return s < e;
}

bool chk(int p) {
	for(int i=0; i<p; ++i) {
		int cnt = 0;
		if(intersect(data[i].x - data[i].r, data[i].x + data[i].r,
				data[p].x - data[p].r, data[p].x + data[p].r)) {
			++cnt;
		}
		if(intersect(data[i].y - data[i].r, data[i].y + data[i].r,
				data[p].y - data[p].r, data[p].y + data[p].r)) {
			++cnt;
		}
		if(cnt == 2) {
			return false;
		}
	}
	return true;
}

bool solve() {
	sort(data, data+n);
	data[0].x = 0;
	data[0].y = 0;

	for(int i=0; i<n; ++i) {
		bool ok = true;
		for(int j=0; j<i; ++j) {
			data[i].x = data[j].x + data[j].r + data[i].r;
			data[i].y = data[j].y - data[j].r + data[i].r;
			data[i].format();

			if(chk(i)) {
				ok = true;
				break;
			}

			data[i].x = data[j].x - data[j].r + data[i].r;
			data[i].y = data[j].y + data[j].r + data[i].r;
			data[i].format();

			if(chk(i)) {
				ok = true;
				break;
			}
		}
		if(!ok) {
			return false;
		}
	}
	return true;
}

int main() {
//	freopen("in", "r", stdin);
//	freopen("out", "w", stdout);

	int dataset;
	scanf("%d", &dataset);
	for(int cas=1; cas <= dataset; ++cas) {
		scanf("%d %d %d", &n, &w, &l);

		for(int i=0; i<n; ++i) {
			data[i].p = i;
			scanf("%d", &data[i].r);
		}
		if(!solve()) {
			cerr<<"unable to solve it..."<<endl;
			break;
		}

		printf("Case #%d:", cas);
		for(int i=0; i<n; ++i) {
			for(int j=0; j<n; ++j) {
				if(data[j].p == i) {
					printf(" %d %d", data[j].x, data[j].y);
					break;
				}
			}
		}
		putchar(10);
	}

	return 0;
}

