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
#define REP(i,n)  for(int i=0; i<(n); i++)
#define REPD(i,n) for(int i=(n)-1; i>=0; i--)

#define DEBUGGING 1

#if defined(DEBUGGING)
#define debug(...) fprintf(stderr,__VA_ARGS__)
#else
#define debug(...)
#endif

const int infty = 999999999;

int X,Y;
VS seats;

int main()
{
	int run, nruns;
	
	scanf("%d\n",&nruns);

	for(run=0; run<nruns; run++) {
		scanf("%d %d\n",&Y,&X);

		seats = VS(Y,string(X,'?'));
		
		REP(y,Y) {
			REP(x,X) scanf("%c",&seats[y][x]);
			scanf("\n");
		}

		REP(y,Y) debug("%s\n",seats[y].c_str());

		VVI best(Y+1,VI(2<<X,0));

		REP(y,Y) {
			REP(i,2<<X) REP(j,2<<X) {
				int cnt = 0;
				REP(x,X) {
					if ( i&(1<<x) ) {
						cnt++;
						if ( seats[y][x]=='x' ) goto wrong;
						if ( x>0 && ((i&(1<<(x-1))) ||
									 ((j&(1<<(x-1))))) ) goto wrong;
						if ( x<X-1 && ((i&(1<<(x+1))) ||
									   ((j&(1<<(x+1))))) ) goto wrong;
					}
				}
				best[y+1][i] >?= best[y][j] + cnt;
			  wrong:
				cnt = 0;
			}
		}

		int res = 0;
		REP(i,2<<X) res >?= best[Y][i];
		
		printf("Case #%d: %d\n",run+1,res);
	}

	return 0;
}
