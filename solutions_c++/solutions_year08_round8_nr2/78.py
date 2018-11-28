using namespace std;
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <list>
#include <set>
#include <algorithm>
#include <utility>
#include <functional>
#include <numeric>
#include <math.h>
#include <string.h>
#include <ctype.h>
#include <stdio.h>

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef istringstream ISS;

#define PB push_back
#define ALL(x) ((x).begin()),((x).end())
#define FOR(i,c) for(typeof(c.begin()) i=c.begin(); i!=c.end(); ++i)
#define REP(i,n) for(int i=0; i<(n); ++i)
#define REPD(i,n) for(int i=(n)-1; i>=0; --i)

#define DEBUGGING 1

#if defined(DEBUGGING)
#define debug(...) printf(__VA_ARGS__)
#else
#define debug(...)
#endif

const int infty = 999999999;

const int dx[8] = { 0, 1, 0,-1, 1, 1,-1,-1};
const int dy[8] = {-1, 0, 1, 0,-1, 1, 1,-1};

struct offer {
	string col;
	int c;
	int start, end;
};

int N;
int nc;

const int F = 10000;

map<string,int> color;
vector<vector<offer> > offers;

int arr2int(VI cols)
{
	sort(cols.begin(),cols.end());

	int res = 0;
	REP(i,cols.size()) {
		res *= nc;
		res += cols[i]+1;
	}

	return res;
}

VI int2arr(int n)
{
	VI res;

	while ( n%nc!=0 ) {
		res.PB((n%nc)-1);
		n /= nc;
	}

	sort(res.begin(),res.end());

	return res;
}


int main()
{
	int run, nruns;
	
	scanf("%d\n",&nruns);
	
	for(run=0; run<nruns; run++) {

		offers.clear();
		color.clear();
		
		cin >> N;
		REP(i,N) {
			offer tmp;
			cin >> tmp.col >> tmp.start >> tmp.end;
			tmp.start--;
			if ( color.count(tmp.col)==0 ) {
				int s = color.size();
				color[tmp.col] = s;
//				cout << tmp.col << " = " << color[tmp.col] << endl;
				offers.PB(vector<offer>());
			}
			tmp.c = color[tmp.col];
			offers[tmp.c].PB(tmp);
		}

		nc = offers.size()+1;
		
		VVI best(F+10,VI(nc*nc*nc,infty));

		best[0][0] = 0;

		REP(f,F-1) REP(c,best[f].size()) {
			REP(i,offers.size()) REP(j,offers[i].size()) {

				offer off = offers[i][j];

				if ( off.start>f || off.end<=f ) continue;

				VI cols = int2arr(c);
				int k;
				for(k=0; k<cols.size(); k++) if ( off.c==cols[k] ) goto coldone;

				if ( k>=3 ) continue;
				cols.PB(off.c);
			  coldone:
				if ( 1==0 ) printf("foo\n");
				
				best[off.end][arr2int(cols)] = min(best[off.end][arr2int(cols)],
												   best[f][c]+1);
			}
		}

		int res = infty;

		REP(c,best[F].size()) res = min(res,best[F][c]);

		if ( res==infty )
			printf("Case #%d: IMPOSSIBLE\n",run+1);
		else
			printf("Case #%d: %d\n",run+1,res);
	}

	return 0;
}
