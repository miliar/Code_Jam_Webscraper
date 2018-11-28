//: Piotr Skotnicki
// Google Code Jam 2010
// Qualification Round - C
#include <iostream>
#include <cstdio>

using namespace std;

#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)

typedef long long int64;
typedef unsigned long long uint64;

int q[1000];

void solve() {
    int64 eur = 0, p, s, k;
	int R, N, u, r = 0;
	
	cin >> R >> k >> N;
		
	s = 0;
	REP(i,N) {
		cin >> q[r];
		s += q[r];
		++r;
	}
		
	r = 0;
	
	for(int i = 0; i < R;) {
		p = 0;
		u = 0;
		while(p + q[r] <= k) {
			++u;
			p += q[r];
			++r;
			r %= N;
			if(u == N)
				break;
		}
		if(p == 0)
			break;
			
		if(u == N && R > 3 && i < R-1) {
			eur += (R-i-1) * s;
			i = R-1;
		} else {
			eur += p;
			++i;
		}
	}

    cout << eur;
}

int main(int argc, char* argv[]) {	
	ios_base::sync_with_stdio(false);

#define TASK "C"

#define LARGE 1
//#define SMALL 1
//#define OWN 1
	
#if LARGE
	freopen(TASK"-large.in", "r", stdin);
	freopen(TASK"-large.out", "w", stdout);
#elif SMALL
	freopen(TASK"-small-attempt0.in", "r", stdin);
	freopen(TASK"-small2.out", "w", stdout);
#elif OWN
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif

	int T;
	cin >> T;
	FOR(i, 1, T) {
		cout << "Case #" << i << ": ";
		solve();
		cout << endl;
	}
	
	fflush(stdout);
	return 0;	
}
