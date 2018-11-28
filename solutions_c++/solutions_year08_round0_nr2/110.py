#include <string>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <math.h>
#include <sstream>
#include <iostream>
#include <queue>
#include <set>
#include <map>

#define ABS(x) ((x)<0?-(x):(x))
#define SQR(x) ((x)*(x))
#define PB push_back
#define MP make_pair
#define SS stringstream
#define LL long long
#define LD long double
#define SZ(x) int(x.size())
#define ALL(x) x.begin(),x.end()
#define FOR(a,b) for(int a=0;a<b;a++)
#define DFOR(a,b) for(int a=b-1;a>=0;a--)
#define CLR(a,b) memset(a,b,sizeof(a))

using namespace std;

int na, nb, t;

struct trip {
	int t1, t2;
	bool ab;
	trip(int a, int b, bool f) {
		t1 = a; t2 = b; ab = f;
	}
	friend bool operator < (const trip &a, const trip &b) {
		return a.t1 < b.t1;
	}
};

vector<trip> trips;

int readtime() {
	char s[10];
	scanf("%s", s);
	return (s[4]-'0') + 10 * (s[3]-'0') + 60 * (s[1]-'0') + 600 * (s[0]-'0');
}

void solvecase() {
	scanf("%d\n%d%d\n", &t, &na, &nb);
	trips.clear();
	FOR(i, na) {
		int a = readtime();
		int b = readtime();
		trips.PB(trip(a, b, true));
	}
	FOR(i, nb) {
		int a = readtime();
		int b = readtime();
		trips.PB(trip(a, b, false));
	}
	sort(ALL(trips));
	int resa = 0, resb = 0;
	vector<int> A, B;
	FOR(i, SZ(trips)) {
		if (trips[i].ab) {
			if (SZ(A) == 0 || A[0] > trips[i].t1) { // add new tram at A
				resa++;				
			} else { // use existing
				A.erase(A.begin());
			}
			B.PB(trips[i].t2 + t);
			sort(ALL(B));
		} else {
			if (SZ(B) == 0 || B[0] > trips[i].t1) {
				resb++;
			} else {
				B.erase(B.begin());
			}
			A.PB(trips[i].t2 + t);
			sort(ALL(A));
		}
	}
	printf("%d %d", resa, resb);
}

void solve() {
	int n;
	scanf("%d\n", &n);
	FOR(i, n) {
		printf("Case #%d: ", i+1);
		solvecase();
		printf("\n");
	}
}

int main() {
	freopen("b2", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	solve();
	return 0;
}