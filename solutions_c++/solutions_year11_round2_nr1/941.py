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

#define NMAX 111


class Problem {
public:
	long n;
	char M[NMAX][NMAX];
	struct team {
		long wins, plays;
		LD WP, WP_wo_win, WP_wo_loss;
		LD OWP, OOWP;
		LD RPI;
		team(): wins(0), plays(0) {}
	} T[NMAX];

	void Input() {
		memset(M,0,sizeof(M));
		memset(T,0,sizeof(T));
		cin>>n;

		string s;
		REP(i,n) {
			cin>>s;
			REP(j,n) {
				M[i][j] = s[j];
			}
			T[i].wins=0; T[i].plays=0;
		}
	}

	void Solve() {
		// WP
		REP(i,n) {
			REP(j,n) {
				if(M[i][j]!='.') ++T[i].plays;
				if(M[i][j]=='1') ++T[i].wins;
			}
			T[i].WP = (LD)T[i].wins / (LD)T[i].plays;
			T[i].WP_wo_loss = (LD)T[i].wins / (LD)(T[i].plays-1);
			T[i].WP_wo_win  = (LD)(T[i].wins-1) / (LD)(T[i].plays-1);
		}

		// OWP
		REP(i,n) {
			LD owp_sum=0;
			REP(j,n) {
				if(M[i][j]=='0') owp_sum += T[j].WP_wo_win;
				if(M[i][j]=='1') owp_sum += T[j].WP_wo_loss;
			}
			T[i].OWP = owp_sum / T[i].plays;
		}

		// OOWP
		REP(i,n) {
			LD oowp_sum=0;
			REP(j,n) {
				if(M[i][j]!='.') oowp_sum += T[j].OWP;
			}
			T[i].OOWP = oowp_sum / T[i].plays;
		}

		// RPI
		REP(i,n) {
			T[i].RPI = (LD).25*T[i].WP + (LD).50*T[i].OWP + (LD).25*T[i].OOWP;
			cout << setiosflags(ios::fixed) << setprecision(12) << T[i].RPI<<endl;
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
3
.10
0.1
10.
4
.11.
0.00
01.1
.10.

===
Case #1:
0.5
0.5
0.5
Case #2:
0.645833333333
0.368055555556
0.604166666667
0.395833333333


*/
