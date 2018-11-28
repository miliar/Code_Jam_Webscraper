#include <iostream>
#include <vector>

using namespace std;

vector<int> a;

vector<int> r, l;

int res = 0;

void count() {
	if (r.size() == 0 || l.size() == 0)
		return;
	int rsum = r[0], lsum = l[0];
	int rsumx = r[0], lsumx = l[0];
	for (int i = 1; i < (int)r.size(); ++i) {
		rsumx ^= r[i];
		rsum += r[i];
	}
	for (int i = 1; i < (int)l.size(); ++i) {
		lsumx ^= l[i];
		lsum += l[i];
	}
	if (rsumx == lsumx && max(rsum, lsum) > res)
		res = max(rsum, lsum);
}

void run(int p) {
	if (p >= a.size()) {
		count();
		return;
	}
	r.push_back(a[p]);
	run(p+1);
	r.pop_back();
	l.push_back(a[p]);
	run(p+1);
	l.pop_back();
}

int main() {
	int T;
	cin >> T;
	for (int test = 0; test < T; ++test) {
		int n;
		cin >> n;
		a.clear();
		res = 0;
		for (int j = 0; j < n; ++j) {
			int t;
			cin >> t;
			a.push_back(t);
		}
		run(0);
		if (res == 0)
			cout << "Case #" << test+1 << ": " << "NO" << endl;
		else
			cout << "Case #" << test+1 << ": " << res << endl;
	}
	return 0;
}