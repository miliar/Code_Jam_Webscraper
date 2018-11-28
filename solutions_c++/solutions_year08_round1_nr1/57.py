#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <cstdlib>
#include <sstream>
#include <fstream>
#include <cstdio>
#include <set>
#include <queue>
#include <numeric>
#include <complex>
#include <climits>

using namespace std;

template<class T> inline bool fixmin(T &a, T b) {if (a<=b) return false; a=b; return true;}
template<class T> inline bool fixmax(T &a, T b) {if (a>=b) return false; a=b; return true;}

ifstream is("A.in");
ofstream os("A.out");

void solve() {
	int n;
	is >> n;
	int a;
	vector<long long> as, bs;
	for (int i=0; i<n; i++) {
		is >> a;
		as.push_back(a);
	}
	for (int i=0; i<n; i++) {
		is >> a;
		bs.push_back(a);
	}
	sort(as.begin(), as.end());
	sort(bs.begin(), bs.end());
	reverse(bs.begin(), bs.end());
	long long ret = 0LL;
	for (int i=0; i<n; i++) {
		ret += as[i]*bs[i];
	}
	os << ' ' << ret << endl;
}

int main () {
	int N; is >> N;
	for (int i=1; i<=N; i++) {
		os << "Case #" << i << ":";
		solve();
	}
	return 0;
}
