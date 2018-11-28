#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

long long l, t, n, c, csum;
long long a[10000], b[10000], d[10000];

long long num(int n)
{
	return n / c * csum + b[n % c];
}

void shift(int w)
{
	memcpy(d, a, sizeof(d));
	for (int i=0;i<c;++i)
		a[i] = d[(i + w)%c];
}

vector<pair<long long, long long>> v;
long long cut(long long extra)
{
	long long ret = 0;
	v.clear();
	for (int i=0;i<c;++i)
		v.push_back(make_pair(a[i], (long long)i));
	sort(v.begin(), v.end());

	while (l && v.size()) {
		pair<int, int> last = v[v.size() - 1];
		if (last.first < extra) {
			-- l;
			ret += extra;
			extra = 0;
		} else {
			int i = last.second;
			long long nr = n / c + (i < n % c ? 1 : 0);
			int cut = min(nr, l);
			ret += cut * last.first;
			v.pop_back();
			l -= cut;
		}
	}

	if (l && extra)
		ret += extra;

	return ret;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	long long T, x;
	cin >> T;
	for (long long TT=1;TT<=T;++TT) {
		cin >> l >> t >> n >> c;

		csum = 0;
		for (long long i=0;i<c;++i) {
			cin >> a[i];
			b[i] = csum;
			csum += a[i] + a[i];
		}

		int st = 0;
		int dr = n;
		while (st < dr) {
			int mij = (st + dr + 1) / 2;

			if (t < num(mij))
				dr = mij - 1;
			else
				st = mij;
		}
		long long extra = 0;
		long long best = num(n);
		
		if (dr < n) {
			if (num(dr) > t)
				extra = a[dr % c];
			else
				extra = a[dr % c] - (t - num(dr)) / 2;

			int w = (dr + 1) % c;

			shift(w);
			n -= dr + 1;
		}

		best -= cut(extra);

		
		cout << "Case #" << TT << ": " << best << endl;
	}

	return 0;
}