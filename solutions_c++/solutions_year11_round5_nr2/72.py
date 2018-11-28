#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#define pb push_back
#define mp make_pair
#define sz(v) ((int)(v).size())
#define all(v) (v).begin(),(v).end()

using namespace std;

typedef pair<int, int> ii;
typedef long long int64;
typedef vector<int> vi;

template<class T> T abs(T a) {return a > 0 ? a : (-a); }
template<class T> T sqr(T a) {return a * a; }

using namespace std;

bool prolong(vector<int> &len, int &finished, int c, int OMAX) {
	int n = sz(len);
	if (c < n) return false;
	for (int i = 0; i < n; ++i)  {
		++len[i];
		--c;
	}
	int n_f = 0;
	while (sz(len) > 0 && len[sz(len) - 1] == OMAX) {
		len.pop_back();
		++n_f;
	}
	if (c < finished) {
		finished = c;
		c = 0;
	}
	else {
		c -= finished;
	}
	finished += n_f;
	if (c > 0) {
		reverse(all(len));
		while (c > 0) {
			len.pb(1);
			--c;
		}
		reverse(all(len));
	}
	return true;
}

bool can(vector<int> cnt, int OMAX) {
	if (OMAX == 0) return true;
	if (OMAX == 1) return true;
	int n = sz(cnt);
	vector<int> len;
	int finished = 0;
	for (int i = 0; i < n; ++i)
		if (!prolong(len, finished, cnt[i], OMAX))
			return false;
	return true;
}

const int MAXN = 10000 + 100;

void solve(int testnum) {
	cerr << testnum << endl;
	int n;
	scanf("%d", &n);
	vector<int> cnt(MAXN);
	for (int i = 0; i < n; ++i) {
		int x;
		scanf("%d", &x);
		++cnt[x];
	}
	int L = 0;
	int R = n + 1;
	if (n == 0) {
		L = 0;
		R = 1;
	}
	while (L != R - 1) {
		int q = (L + R) / 2;
		if (can(cnt, q)) L = q; else R = q;
	}
	printf("Case #%d: %d\n", testnum, L);
}

int main() {
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) solve(i);
	return 0;
}
