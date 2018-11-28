#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>
using namespace std;

const int N = 1000010;
int c[N];
int l, n, nc;
__int64 t;

int main() {
	int T;
	cin >> T;
	for (int kase = 0; kase < T; ++kase) {
		cin >> l >> t >> n >> nc;
		__int64 tot = 0;
		for (int i = 0; i < nc; ++i) {
			cin >> c[i];
			tot += c[i];
			for (int k = i + nc; k < n; k += nc) {
				c[k] = c[i];
				tot += c[k];
			}
		}
		//tot *= n / nc;
		tot *= 2;
		int pos = -1;
		__int64 time = 0;
		for (int i = 0; i < n; ++i) {
			pos = i;
			time += c[i] + c[i];
			if (time > t) break;
		}
		//printf("pos : %d\n", pos);
		vector<int> v;
		for (int i = pos + 1; i < n; ++i) {
			v.push_back(c[i]);
		}
		int dlast = c[pos];
		int timesaved = (time - t) / 2;
		v.push_back(timesaved);
		sort(v.begin(), v.end(), greater<int>());
		__int64 totts = 0;
		for (int i = 0; i < l && i < v.size(); ++i) {
			totts += v[i];
		}
		printf("Case #%d: %I64d\n", kase + 1, tot - totts);
	}
	return 0;
}

