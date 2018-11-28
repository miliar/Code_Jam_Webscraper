#line 95 "AgeEncoding.cpp"
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cstring>
using namespace std;

#define REP(i, n) for(int i = 0; i<(n); i++)
#define abs(a) ((a) >= 0 ? (a) : -(a))
#define inf 2000000001
typedef vector<int> VI;
typedef vector<string> VS;

typedef long long i64;
typedef unsigned long long u64;

/*

3
4 6 4
1 4 2 1
100 10 1
1
5 5 10
2 4 2 3 4 2 1 2 1 3


 */
void go(int t) {
	int R, k, N;
	cin>>R>>k>>N;
	vector<i64> v;
	i64 s = 0;
	v.push_back(s);
	for (int i = 0; i < N; i++) {
		int a;
		cin>>a;
		s += a;
		v.push_back(s);
	}
	if (s <= k) {
		cout << "Case #" << t << ": " << s * R << endl;
		return;
	}
	VI q;
	map<int, int> m;
	int last = 1;

	m[1] = 0;
	i64 total = 0;
	vector<i64> sum(2*N+2);
	sum[0] = 0;
	for (int r = 1; r <= R; r++) {
		i64 start = v[last - 1];
		i64 tgt = start + k;
		int next = upper_bound(v.begin() + last, v.end(), tgt) - v.begin();
		i64 earn = 0;

		if (next < N + 1) {
			if (next == last) {
				// can't fit
				break;
			}
			earn = v[next - 1] - start;
		} else {
			tgt -= v[N];
			next = upper_bound(v.begin() + 1, v.begin() + last, tgt) - v.begin();
			earn = v[N] - start + v[next - 1];
		}

		total += earn;
		sum[r] = total;
//		cerr << r << ": " << earn << ", " << total << endl;
		if (m.count(next)) {
			int sr = r - m[next];
			int rest = R - r;
			total += rest / sr * (sum[r] - sum[m[next]]) + (sum[rest % sr + m[next]] - sum[m[next]]);
			break;
		} else {
			m[next] = r;
		}
		last = next;
	}
	cout << "Case #" << t << ": " << total << endl;
}

int main() {
	int T;
	cin>>T;
	for (int t = 1; t <= T; t++) {
		go(t);
	}
    return 0;
}
