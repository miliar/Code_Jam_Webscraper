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
#define REP(i,n) for(typeof(n) i=0; i<(n); ++i)

const int infty = 999999999;

#define DEBUGGING 1

#if defined(DEBUGGING)
#define debug(...) printf(__VA_ARGS__)
#else
#define debug(...)
#endif

const double eps = 1E-1;

const int maxdrop = 100;
const int maxshift = 10;

int n, X, Y;
VI r;
vector<vector<double> > pos;

int overlap(int i)
{
	REP(j,i) {
		if ( hypot(pos[i][0]-pos[j][0],pos[i][1]-pos[j][1])
		     <=r[i]+r[j]+1.5 ) return 1;
	}

	return 0;
}

int main()
{
	srand(time(NULL));

	int run, nruns;

	cin >> nruns;

	for(run=1; run<=nruns; run++) {

		cin >> n >> X >> Y;
		r = VI(n);
		REP(i,n) cin >> r[i];

// 		sort(ALL(r));
// 		reverse(ALL(r));

		pos = vector<vector<double> >(n,vector<double>(2));

		pos[0][0] = pos[0][1] = eps;
		for(int i=1; i<n; i++) {
			int k;
			for(k=0; k<maxdrop; k++) {
				pos[i][0] = 1.0*X*rand()/(RAND_MAX+1.0);
				pos[i][1] = 1.0*Y*rand()/(RAND_MAX+1.0);
				if ( pos[i][0]>=X && pos[i][1]>=Y ) {
					fprintf(stderr,"drop outside: case %d at %d/%d\n",run,i,n);
					return 1;
				}
				if ( !overlap(i) ) break;
			}
			if ( k>=maxdrop ) {
				fprintf(stderr,"drop failed: case %d at %d/%d\n",run,i,n);
				return 1;
			}
			for(k=0; k<maxshift; k++) {
				double dx = 0.1*X*rand()/RAND_MAX;
				double dy = 0.1*Y*rand()/RAND_MAX;
				vector<double> oldpos = pos[i];
				pos[i][0] -= dx;
				pos[i][1] -= dy;
				if ( pos[i][0]<eps ||
				     pos[i][1]<eps || overlap(i) ) pos[i] = oldpos;
			}
		}

		for(int i=0; i<n; i++) {
			if ( pos[i][0]<=0 || pos[i][0]>=X ||
			     pos[i][1]<=0 || pos[i][1]>=Y ) {
				fprintf(stderr,"outside: case %d at %d\n",run,i);
//				return 1;
			}
			for(int j=0; j<i; j++) {
				double dx = pos[j][0] - pos[i][0];
				double dy = pos[j][1] - pos[i][1];
				if ( sqrt(dx*dx+dy*dy)<r[i]+r[j]+0.5 ) {
					fprintf(stderr,"overlap: case %d at %d - %d\n",run,j,i);
//					return 1;
				}
			}
		}

		printf("Case #%d:",run);
		REP(i,n) printf(" %.5lf %.5lf",pos[i][0],pos[i][1]);
		printf("\n");
	}

	return 0;
}
