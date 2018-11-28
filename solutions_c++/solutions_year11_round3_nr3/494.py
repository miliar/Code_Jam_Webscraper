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

#define NMAX 10020


class Problem {
public:
	long F[NMAX];
	int n, l, h;

	void Input() {
		memset(F,0,sizeof(F));
		cin>>n>>l>>h;
		REP(i,n)
			cin>>F[i];
	}

	void Solve_Naive() {
		FOR(v,l,h) {
			bool no = false;
			REP(i,n) {
				if( (F[i]%v!=0) && (v%F[i]!=0) ) {
					no = true;
					break;
				}
			}
			if(!no) {
				cout<<v;
				return;
			}
		}
		cout<<"NO";
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
		P->Solve_Naive();
		cout<<endl;
		delete P;
	}

    return 0;
}

/*
2
3 2 100
3 5 7
4 8 16
1 20 5 2

===

Case #1: NO
Case #2: 10


*/
