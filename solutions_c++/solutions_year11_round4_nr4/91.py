#include <map>
#include <queue>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <boost/dynamic_bitset.hpp>

using namespace std;

const int MAXN = 500;

typedef boost::dynamic_bitset<> bitset;

int d[MAXN];
vector<int> e[MAXN];
bitset bs[MAXN], pre[MAXN];
map<bitset, int> dp[MAXN];

int main() {
	int re, n, m, a, b, ans;
	vector<int> v;

	scanf("%d", &re);
	for (int ri = 1; ri <= re; ++ri) {
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; ++i) {
			d[i] = -1;
			e[i].clear();
			dp[i].clear();
			pre[i] = bs[i] = bitset(n);
			bs[i].set(i);
		}
		for (int i = 0; i < m; ++i) {
			scanf("%d,%d", &a, &b);
			e[a].push_back(b);
			e[b].push_back(a);
			bs[a].set(b);
			bs[b].set(a);
		}

		v.clear();
		d[0] = 0;
		v.push_back(0);
		for (int h = 0; h < (int)v.size(); ++h) {
			a = v[h];
			for (vector<int>::const_iterator i = e[a].begin(); i != e[a].end(); ++i) {
				if (d[*i] == -1) {
					d[*i] = d[a] + 1;
					v.push_back(*i);
				}
			}
		}

		for (int i = 0; i < n; ++i) {
			for (int j = bs[i].find_first(); j != (int)bitset::npos; j = bs[i].find_next(j)) {
				if (d[j] == d[i] - 1) {
					pre[i].set(j);
				}
			}
		}

		ans = 0;
		dp[0][bitset(n)] = 0;
		for (int i = 0; i < (int)v.size(); ++i) {
			a = v[i];
			for (map<bitset, int>::const_iterator j = dp[a].begin(); j != dp[a].end(); ++j) {
				bitset t = j->first;
				b = j->second;
		//		cout << "[" << a << "] " << t << "+" << b << endl;
				if (a == 1) {
					ans = max(ans, (int)t.count() + b);
				}
				t |= bs[a];
				b += (t & pre[a]).count();
				t &= ~pre[a];
				for (vector<int>::const_iterator k = e[a].begin(); k != e[a].end(); ++k) {
					if (d[*k] == d[a] + 1) {
						int& c = dp[*k][t];
						c = max(c, b);
					}
				}
			}
		}

		printf("Case #%d: %d %d\n", ri, d[1] - 1, ans - d[1]);
	}

	return 0;
}

