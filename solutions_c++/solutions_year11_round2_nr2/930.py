#include <iostream>
#include <sstream>
#include <algorithm>
#include <iomanip>
#include <cassert>
#include <cstring>
#include <string>
#include <vector>
#include <cstdio>
#include <queue>
#include <cmath>
#include <set>

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

#define NMAX 222


class Problem {
public:
	long c, d, n;
	vector<int> X;

	struct hotdog {
		int p,v;
	} T[NMAX];

	int sum[NMAX];


	void Input() {
		X.clear();
		cin>>c>>d;

		REP(i,c) {
			cin>>T[i].p>>T[i].v;
			if(i==0) sum[i]=T[i].v;
			else sum[i]=sum[i-1]+T[i].v;
		}
	}

	LD Solve() {
		long r=0;
		REP(a,c) {
			FOR(b,a,c-1) {
				int ile = sum[b]; if(a>0) ile-=sum[a-1];
				long should_dist = (ile-1)*d;
				long cur_dist = T[b].p-T[a].p;
				r = max<int>(r, should_dist-cur_dist);
			}
		}

		// ponowne skalowanie przez 2
		return ((LD)r) / 2.0L;
	}
};


int main() {
    ios_base::sync_with_stdio(0);

	// cases
	long nCases;
	cin>>nCases;
	FOR(iCase, 1, nCases) {
		Problem *P = new Problem();
		P->Input();
		cout<<"Case #"<<iCase<<": "<< P->Solve() <<endl;
		delete P;
	}

    return 0;
}

/*
2
3 2
0 1
3 2
6 1
2 2
0 3
1 1

===

Case #1: 1.0
Case #2: 2.5


*/
