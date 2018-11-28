//Problem A. Password Problem
#include <algorithm>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <cstring>
#include <climits>
using namespace std;
#define PB push_back
#define MP make_pair
#define REP(i,n) for(i=0;i<(n);++i)
#define FOR(i,l,h) for(i=(l);i<=(h);++i)
#define FORD(i,h,l) for(i=(h);i>=(l);--i)
#define foreach(itr, cont) for (typeof(cont.begin()) itr = cont.begin(); itr != cont.end(); itr++)
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int,int> PII;

int a[1001], b[1001];
bool solve(const vector<int>& ord, const vector<int>& r, vector<int> &x, vector<int> &y, int W, int L) {
	int cur = 0;
	int first_y = true;
	int height = 0;
	while (cur < r.size()) {
		int mr = 0;
		bool first = true;
		int i;
		for (i = cur; i < r.size(); i ++) {
			int idx = ord[i];
			if (first) {
				first = false;
				x[idx] = 0;
			}
			else {
				int prev = ord[i-1];
				x[idx] = x[prev] + r[prev] + r[idx];
			}

			if (first_y) y[idx] = 0;
			else y[idx] = height + r[idx];

			if (x[idx] > W || y[idx] > L) break;
			mr = max(mr, r[idx]);
		}
		if (i == r.size()) return true;
		if (i == cur) return false;
		cur = i;
		if (first_y) height += mr;
		else height += 2 * mr;
		first_y = false;
	}
	return true;
}
int main() {
	int T, N, W, L;

	ifstream in("B-small-attempt3.in");
	ofstream out("B-small-attempt3.out");
	//ifstream in("C-large.in");
	//ofstream out("C-large.out");

	in >> T;
	for (int cs = 1; cs <= T; cs ++) {
		out << "Case #" << cs << ": ";

		in >> N >> W >> L;
		vector<int> r(N);
		vector<int> perm(N);
		for (int i = 0; i < N; i ++) {
			in >> r[i];
			perm[i] = i;
		}
		bool yes = false;
		vector<int> x(N), y(N);
		int cond = 0;
		do {
			//cout <<"here " << cs << endl;
			if (solve(perm, r, x, y, W, L)) {
				yes = true;
				cond = 0;
				break;
			}
			if (solve(perm, r, x, y, L, W)) {
				yes = true;
				cond = 1;
				break;
			}
		} while (next_permutation(perm.begin(), perm.end()));

		if (yes) {
			//cout << N << endl;
			for (int i = 0; i < N; i ++) {
				if (cond == 0) out << x[perm[i]] << " " << y[perm[i]];
				else out << y[perm[i]] << " " << x[perm[i]];
				if (i != N-1) out << " ";
			}
		}
		else out << "error" << endl;
		out << endl;
	}
	return 0;
}

