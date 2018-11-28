#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <queue>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <numeric>
using namespace std;

#define FOR(i,a,b) for(int i=(a); i<(int)(b); ++i)
#define ALL(a) (a).begin(),(a).end()
#define PB(a) push_back(a)
#define MP(a,b) make_pair((a),(b))
#define sqr(a) ((a)*(a))
typedef long long i64;
typedef unsigned long long u64;

int nextInt() {
	int x;
	scanf("%d", &x);
	return x;
}

long long nextLong() {
	long long x;
	scanf("%I64d", &x);
	return x;
}

double nextDouble() {
	double x;
	scanf("%lf", &x);
	return x;
}

const int BUFSIZE = 1000000;
char buf[BUFSIZE + 1];
string nextString() {
	scanf("%s", buf);
	return buf;
}

const int MAX = 10000 + 10;
typedef vector<vector<int> > Adj;

int solve(vector<int> a) {
	if (a.size() == 0) {
		return 0;
	}
	vector<int> c(MAX);
	for (int i = 0; i < a.size(); ++i) {
		c[a[i]]++;
	}
	multiset<int> cur;
	int res = INT_MAX;
	for (int i = 0; i < MAX; ++i) {
		multiset<int> next;
		for (int j = 0; j < c[i]; ++j) {
			if (cur.size() == 0) {
				next.insert(1);
			} else {
				multiset<int>::iterator it = cur.begin();
				int nLength = *it + 1;
				next.insert(nLength);
				cur.erase(it);
			}
		}
		if (cur.size() > 0) {
			res = min(res, *cur.begin());
		}
		cur = next;
	}
	return res;
}


int main() {
	freopen("B-large.in", "rt", stdin);
	freopen("B-large.out", "wt", stdout);
	int T = nextInt();
	for (int cas = 1; cas <= T; ++cas) {
		int n = nextInt();
		vector<int> a(n);
		for (int i = 0; i < n; ++i) {
			a[i] = nextInt();
		}
		int res = solve(a);		
		cerr << cas << endl;
		printf("Case #%d: %d\n", cas, res);
	}
	return 0;
}

