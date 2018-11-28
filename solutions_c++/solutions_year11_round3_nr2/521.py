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

#define NMAX 1002003
#define INF 100200300400500600LL


class Problem {
public:
	LL X[NMAX];
	LL SUM[NMAX];
	long L, N, C;
	LL t;
	int depth;
	map< pair<int,int>, LL > MEM;

	void Input() {
		memset(X,0,sizeof(X));
		MEM.clear();
		depth=0;

		cin>>L>>t>>N>>C;
		REP(i,C) {
			long a;
			cin>>a;
			for(int p=i; p<N; p+=C)
				X[p] = a;
		}

		SUM[0]=0;
		REP(p,N)
			SUM[p+1] = SUM[p]+X[p];

	}

	LL calc(int p, int amp) {
		// border
		if(amp<0)
			return INF;
		if(p>=N)
			return 0;
		if(depth>2000 || amp==0) /* arbitrary limit - turn off amplifyers */
			return (SUM[N]-SUM[p])*2;

		// dynamic
		LL &ret = MEM[ pair<int,int>(p,amp) ];
		if(ret!=0) 
			return ret;
		++depth;
		ret = min<LL>(
			X[p]*2 + calc(p+1, amp),
			X[p] + calc(p+1, amp-1)
			);
		--depth;
		return ret;
	}

	LL Solve() {
		// build L
		int p=0; LL start_t=0;
		for(; p<N && start_t<t; ++p) 
			start_t+=X[p]*2;
		if(p==N) 
			return start_t;

		// arrive at next star w/o amplifyer
		LL ret = start_t + calc(p, L);
		// arrive with partial amplifying
		if(start_t>t) {
			ret = min<LL>(ret, start_t-(start_t-t)/2 + calc(p, L-1));
		}

		return ret;

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
		cout<<"Case #"<<iCase<<": ";
		cout<<P->Solve();
		cout<<endl;
		delete P;
	}

    return 0;
}

/*
2
2 20 8 2 3 5
1 4 2 2 10 4

===

Case #1: 54
Case #2: 20


*/
