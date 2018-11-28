#include <vector>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <string>
#include <cstdlib>
#include <map>
#include <queue>

using namespace std;

#define FOR(i,a,n) for (int i = (a); i < (n); ++i)
#define FORE(i,a,n) for (int i = (a); i <= (n); ++i)
#define FORD(i,a,b) for (int i = (a); i >= (b); --i)
#define REP(i,n) FOR(i,0,n)
#define REPE(i,n) FORE(i,0,n)
#define LL long long
#define FIR(n) REP(i,n)
#define FJR(n) REP(j,n)
#define ALL(v) v.begin(), v.end()

#define FI FIR(n)
#define FJ FJR(n)
#define FR(i,a) FOR(i,a,n)
#define REPN(i) REP(i,n)

typedef pair<int, int> PI;
typedef vector<PI> VPI;

struct Task {
	VPI routesA, routesB;
	int T, NA, NB;
	priority_queue<int, vector<int>, greater<int> > qA, qB;

	int readTime() {
		int a, b;
		scanf("%d:%d", &a, &b);
		return 60*a+b;
	}

	void input() {
		cin >> T >> NA >> NB; 
		string s1, s2;
		FIR(NA) {
			int t1 = readTime();
			int t2 = readTime();
			routesA.push_back(PI(t1, t2));
		}
		FIR(NB) {
			int t1 = readTime();
			int t2 = readTime();
			routesB.push_back(PI(t1, t2));
		}
		
	}
	PI solve() {
		sort(ALL(routesA)); reverse(ALL(routesA));
		sort(ALL(routesB)); reverse(ALL(routesB));
		int a = 0, b = 0;

		REP(time, 24*60) {
			for(; routesA.size() && routesA.back().first == time; routesA.pop_back()) {
				if (qA.size() && qA.top() <= time) qA.pop(); else ++a;
				qB.push(routesA.back().second + T);
			}

			for(; routesB.size() && routesB.back().first == time; routesB.pop_back()) {
				if (qB.size() && qB.top() <= time) qB.pop(); else ++b;
				qA.push(routesB.back().second + T);
			}
			
		}

		return PI(a, b);
	}
};

int main() {
freopen("B-large.in", "rt", stdin);
freopen("B-large.out", "w", stdout);

	int tc; cin >>tc;
	REP(TC, tc) {
		Task t;
		t.input();
		PI res = t.solve();
		printf("Case #%d: %d %d\n", TC+1, res.first, res.second);
	}

fclose(stdout);
}
