#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <deque>
#include <iostream>
#include <limits>
#include <numeric>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

////////////////////////////////////////////////////////
#define SIZE(v)			((int)v.size())
#define PB(v,x)			(v.push_back(x))
#define FOR(i,f,t)		for (int i = f; i < t; ++i)
#define FOREQ(i,f,t)	FOR(i,f,(t+1))
#define FOR0(i,t)		FOR(i,0,t)
#define FOR0EQ(i,t)		FOREQ(i,0,t)
#define FORIDX(i,v)		FOR(i,0,SIZE(v))
#define FOREACH(i,v)	for (auto i = v.begin(); i != v.end(); ++i)

#define IPMAP(v,f)		do {FOREACH(i,v) { *i=f(*i); }} while(0)

#define IN(x)			(in.x)
#define INP(x)			(in->x)

#define INPUTS			struct inputs
#define READ_INPUT		void read_input(inputs *in)

#define BEGIN_SOLN		void solve() { inputs in; read_input(&in);
#define END_SOLN		}

#define LMB(n,f)	    [](n){return f;}

typedef vector<int> vi;
typedef vector<char> vc;
typedef vector<string> vs;
////////////////////////////////////////////////////////

INPUTS { int n; vs sch; vi ops; };
READ_INPUT { cin >> INP(n); INP(sch).resize(INP(n)); FOR0(i,INP(n)) { cin >> INP(sch)[i]; }  }

////////////////////////////////////////////////////////

int ops(vs sch,int t) {
	int ops=0;
	int n=SIZE(sch);
	FOR0(i,n) if (sch[t][i] != '.') ++ops;
	return ops;
}

int is_op(vs sch,int t,int j) {
	return sch[t][j] != '.';
}

double WP(vs sch,int t) {
	int n=SIZE(sch);
	int played=0,won=0;

	FOR0(i,n) {
		if (sch[t][i] != '.') ++played;
		if (sch[t][i] == '1') ++won;
	}

	return (double)won/(double)played;
}

double OWP(vs sch,int t) {
	int n=SIZE(sch);
	double owp=0;
	vs sch2(sch);

	FOR0(i,n) {
		FOR0(j,n) {
			if (i==t||j==t) sch2[i][j]='.';
		}
	}

	FOR0(i,n) if (is_op(sch,t,i)) { owp += WP(sch2,i); }
	return owp/ops(sch,t);
}

double RPI(vs sch,int t) {
	int n=SIZE(sch);
	double wp = WP(sch,t);
	double owp = OWP(sch,t);
	double oowp=0;

	FOR0(i,n) {
		if (is_op(sch,t,i)) oowp += OWP(sch,i);
	}
	oowp /= ops(sch,t);

	return 0.25 * wp + 0.5 * owp + 0.25 * oowp;
}

BEGIN_SOLN
{
	int n=SIZE(IN(sch));

	cout << "\n";
	FOR0(i,n) {
		cout << RPI(IN(sch),i) << "\n";
	}
}
END_SOLN

////////////////////////////////////////////////////////
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n; cin >> n;

	cout.precision(12);

	FOR0(i,n) {
		cout << "Case #" << (i + 1) << ": ";
		solve();
		cout << "\n";
	}

	return 0;
}
////////////////////////////////////////////////////////