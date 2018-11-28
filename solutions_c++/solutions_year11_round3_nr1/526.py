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

#define NMAX 55


class Problem {
public:
	char T[NMAX][NMAX];
	int r, c;

	void Input() {
		memset(T,0,sizeof(T));
		cin>>r>>c;

		REP(y,r) {
			REP(x,c) {
				cin>>T[y][x];
			}
		}
	}

	void Solve() {
		bool impossible = false;
		REP(y,r) {
			REP(x,c) {
				if(T[y][x]=='#') {
					if(T[y][x+1]=='#' && T[y+1][x]=='#' && T[y+1][x+1]=='#') {
						T[y][x] = '/'; T[y+1][x+1] = '/';
						T[y+1][x] = '\\'; T[y][x+1] = '\\';
					}else{
						impossible = true;
					}
				}
			}
		}
		if(impossible) {
			cout<<"Impossible"<<endl;
		}else{
			REP(y,r) {
				REP(x,c) {
					cout<<T[y][x];
				}
				cout<<endl;
			}
		}
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
		cout<<"Case #"<<iCase<<":"<<endl;
		P->Solve();
		delete P;
	}

    return 0;
}

/*
3
2 3
###
###
1 1
.
4 5
.##..
.####
.####
.##.. 

===

Case #1:
Impossible
Case #2:
.
Case #3:
./\..
.\//\
./\\/
.\/.. 


*/
