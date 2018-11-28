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

const int infty = 999999999;

//#define DEBUGGING 1

#if defined(DEBUGGING)
#define debug(...) printf(__VA_ARGS__)
#else
#define debug(...)
#endif

string welcome("welcome to code jam");

int main()
{
	int nruns;
	char tmp[510];
	string line;

	scanf("%d\n",&nruns);

	for(int run=1; run<=nruns; run++) {

		gets(tmp);
		line = string(tmp);

		int L = line.length();
		int W = welcome.length();

		VVI n(L+1,VI(W+1,0));
		n[0][0] = 1;

		REP(i1,L) for(int i2=i1+1; i2<=L; i2++) {
		    for(int j=1; j<=W; j++) {
				if ( line[i2-1]==welcome[j-1] ) {
					if ( n[i2][j]!=0 ) {
						debug("%2d,%2d -> %2d,%2d = %d + %d\n",
						      i1,j-1,i2,j,n[i2][j],n[i1][j-1]);
					}
					n[i2][j] = (n[i2][j] + n[i1][j-1]) % 10000;
				}
			}
		}

		int res = 0;
		REP(i,L+1) res = (res + n[i][W]) % 10000;
		printf("Case #%d: %04d\n",run,res);
	}

	return 0;
}
