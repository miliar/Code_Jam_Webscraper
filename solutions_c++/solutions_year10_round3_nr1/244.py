#include <cstring>
#include <cstdio>
#include <vector>
#include <utility>
#include <algorithm>
using namespace std;
const int MAXN = 2000;
#define _cp(a,b) ((a) <= (b))

typedef int elemType;
elemType tmp[MAXN];

int inv(int n, elemType * a) {
	int l = n >> 1, r = n - l, i, j;
	int ret = (r > 1 ? (inv(l, a) + inv(r, a + l)) : 0);
	for (i = j = 0; i <= l; tmp[i + j] = a[i], i++) {
		for (ret += j; j < r && (i == l || !_cp(a[i], a[l + j])); tmp[i + j] = a[l + j], j++);
	}
	memcpy(a, tmp, sizeof(elemType) * n);
	return ret;
}

vector<pair<int, int> > data;
int main(){
	int cases;
	scanf("%d", &cases);
	for (int tt = 0; tt < cases; ++tt){
		int t;
		data.clear();
		scanf("%d", &t);
		for (int i = 0; i < t; ++i){
			int x, y;
			scanf("%d%d", &x, &y);
			data.push_back(make_pair(x, y));
		}
		sort(data.begin(), data.end());
		int f[MAXN];
		for (int i = 0; i < data.size(); ++i) f[i] = data[i].second;
		printf("Case #%d: %d\n", tt + 1, inv(data.size(), f));
	}
}