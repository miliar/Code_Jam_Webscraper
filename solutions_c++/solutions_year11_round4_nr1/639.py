#include <iostream>
#include <algorithm>
#include <iomanip>
#include <cassert>
#include <cstring>
#include <string>
#include <vector>
#include <cstdio>
#include <queue>
#include <cmath>
#include <map>

using namespace std;

typedef vector<int> VI;
typedef long long LL;
typedef long double LD;
#define FOR(x, b, e) for(int x=b; x<=(e); ++x)
#define FORD(x, b, e) for(int x=b; x>=(e); --x)
#define REP(x, n) for(int x=0; x<(n); ++x)
#define VAR(v,n) typeof(n) v=(n)
#define ALL(c) c.begin(),c.end()
#define SIZE(x) (int)x.size()
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define PB push_back
#define ST first
#define ND second

#define SMAX 20200

struct way {
	long len, speed;
};
bool operator<(const way &a, const way &b) {
	return a.speed<b.speed;
}

class Problem {
public:
	long X, S, R, N;
	LD Trun;
	long RS;
	way W[SMAX];
	long wcnt;

	LD Solve() {
		// in
		cin>>X>>S>>R>>Trun>>N;
		RS = R-S;
		long last = 0, b,e,s;
		wcnt = 0;
		REP(i, N) {
			cin>>b>>e>>s;

			if(b>last) {
				way &p = W[wcnt++];
				p.len = b-last;
				p.speed = S;
			}

			way &x = W[wcnt++];
			x.len = e-b;
			x.speed = s+S;

			last = e;
		}
		if(e<X) {
			way &p = W[wcnt++];
			p.len = X-e;
			p.speed = S;
		}

		// solve
		sort(W, W+wcnt);
		LD razem = 0;
		REP(i, wcnt) {
			way &x = W[i];
			LD t0 = (LD)x.len/(LD)x.speed;
			LD t1 = (LD)x.len/(LD)(x.speed+RS);
			if(Trun>t1) {
				// jeszcze moze biec
				Trun -= t1;
				razem += t1;
			}else{
				// koncowka biegu
				LD dist1 = Trun*(LD)(x.speed+RS);
				LD dist0 = (LD)x.len - dist1;
				t1 = Trun;
				t0 = dist0 / (LD)x.speed;

				Trun = 0;
				razem += t1 + t0;
			}
		}

		return razem;
	}
};

int main() {
    ios_base::sync_with_stdio(0);

	int nCases; cin>>nCases;
	REP(iCase, nCases) {
		Problem *P = new Problem();
		cout<<"Case #"<<(iCase+1)<<": "<<setiosflags(ios_base::fixed)<<setprecision(8)<<(P->Solve())<<endl;
		delete P;
	}
	return 0;
}



/*
30
10 1 4 1 2
4 6 1
6 9 2
12 1 2 4 1
6 12 1
20 1 3 20 5
0 4 5
4 8 4
8 12 3
12 16 2
16 20 1

*/