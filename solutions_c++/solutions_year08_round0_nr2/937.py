#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>

using namespace std;

struct p {
	int t1, t2, s;

	bool operator < (const p &x) const {
		if (t1 != x.t1)
			return t1 < x.t1;
		if (t2 != x.t2)
			return t2 < x.t2;
		return s < x.s;
	}
};

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int n;
	cin >> n;
	vector<p> sa;
	string s;
	for (int i = 0; i < n; ++i) {
		int t, na, nb;
		cin >> t >> na >> nb;
		sa.clear();
		for (int j = 0; j < na; ++j) {
			int h1, m1, h2, m2;
			cin >> s;
			h1 = (s[0] - '0') * 10 + s[1] - '0';
			m1 = (s[3] - '0') * 10 + s[4] - '0';
			cin >> s;
			h2 = (s[0] - '0') * 10 + s[1] - '0';
			m2 = (s[3] - '0') * 10 + s[4] - '0';
			p x = { h1 * 60 + m1, h2 * 60 + m2, 0 };
			sa.push_back(x);
		}
		for (int j = 0; j < nb; ++j) {
			int h1, m1, h2, m2;
			cin >> s;
			h1 = (s[0] - '0') * 10 + s[1] - '0';
			m1 = (s[3] - '0') * 10 + s[4] - '0';
			cin >> s;
			h2 = (s[0] - '0') * 10 + s[1] - '0';
			m2 = (s[3] - '0') * 10 + s[4] - '0';
			p x = { h1 * 60 + m1, h2 * 60 + m2, 1 };
			sa.push_back(x);
		}
		multiset<int> qa, qb;
		sort(sa.begin(), sa.end());
		int a = 100000, b = 100000, sum = 1000000;
		for (int j = 0; j <= na; ++j) {
			for (int k = 0; k <= nb; ++k) {
				if (na + nb > sum)
					break;
				bool f = true;
				qa.clear();
				qb.clear();
				for (int q = 0; q < j; ++q)
					qa.insert(0);
				for (int q = 0; q < k; ++q)
					qb.insert(0);
				for (int q = 0; q < sa.size(); ++q) {
					if (sa[q].s == 0) {
						if (!qa.empty() && *qa.begin() <= sa[q].t1) {
							qa.erase(qa.begin());
							qb.insert(sa[q].t2 + t);
						} else {
							f = false;
							break;
						}
					} else {
						if (!qb.empty() && *qb.begin() <= sa[q].t1) {
							qb.erase(qb.begin());
							qa.insert(sa[q].t2 + t);
						} else {
							f = false;
							break;
						}
					}
				}
				if (f) {
					a = j;
					b = k;
					sum = a + b;
				}
			}
		}
		printf("Case #%d: %d %d\n", i + 1, a, b);
	}

	return 0;
}
