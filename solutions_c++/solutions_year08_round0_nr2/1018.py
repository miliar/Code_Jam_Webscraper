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

ifstream is("B.in");
ofstream os("B.out");

int readtime () {
	int a, b;
	char c;
	is >> a >> c >> b;
	return 60*a + b;
}

void solve() {
	int T, A, B;
	is >> T >> A >> B;
	vector<pair<int, int> > as, bs;
	for (int i=0; i<A; i++) {
		int a, b;
		a = readtime(); b = readtime();
		as.push_back(make_pair(a, b));
	}
	for (int i=0; i<B; i++) {
		int a, b;
		a = readtime(); b = readtime();
		bs.push_back(make_pair(a, b));
	}
	sort(as.begin(), as.end());
	sort(bs.begin(), bs.end());
	//for (int i=0; i<A; i++) cout << as[i].first << ':' << as[i].second << ' ';
	int doneA[A+1];
	int doneB[B+1];
	memset(doneA, 0, sizeof(doneA));
	memset(doneB, 0, sizeof(doneB));
	int fa=0;
	int fb=0;
	int retA = 0, retB = 0;
	while (fa < A || fb < B) {
		int next = 1;
		if (fb==B || fa!=A && as[fa].first < bs[fb].first) {
			next = 0;
		}
		next ? retB++ : retA++ ;
		int t = 0;
		while (1) {
			//cout << next << ':' << t << ' ';
			bool done = 0;
			if (next == 0) {
				for (int i=0; i<A; i++) if (as[i].first >= t && !doneA[i]) {
					t = as[i].second+T;
					doneA[i] = 1;
					next = 1;
					done = 1;
					break;
				}
			} else {
				for (int i=0; i<B; i++) if (bs[i].first >= t && !doneB[i]) {
					t = bs[i].second+T;
					doneB[i] = 1;
					next = 0;
					done = 1;
					break;
				}
			}
			while (doneA[fa]) fa++;
			while (doneB[fb]) fb++;
			if (done) continue;
			//cout << endl;
			break;
		}
	}
	os << ' ' << retA << ' ' << retB << endl;
}

int main () {
	int N; is >> N;
	for (int i=1; i<=N; i++) {
		os << "Case #" << i << ":";
		solve();
	}
	return 0;
}
