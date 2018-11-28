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

#define DEBUGGING 1

#if defined(DEBUGGING)
#define debug(...) printf(__VA_ARGS__)
#else
#define debug(...)
#endif

int L,D;

VS dict;

int match(string word, string pat)
{
	int pi = 0;
	REP(i,L) {
		if ( pat[pi]=='(' ) {
			while ( pat[++pi]!=')' ) {
				if ( word[i]==pat[pi] ) goto ok;
			}
			return 0;
		  ok:
			while ( pat[++pi]!=')' );
		} else {
			if ( word[i]!=pat[pi] ) return 0;
		}
		pi++;
	}

	return 1;
}

int main()
{
	int nruns;

	scanf("%d %d %d\n",&L,&D,&nruns);

	string tmp;
	REP(i,D) { cin >> tmp; dict.PB(tmp); }

	for(int run=1; run<=nruns; run++) {

		string pat;
		cin >> pat;

		int res = 0;
		REP(i,D) if ( match(dict[i],pat) ) res++;

		printf("Case #%d: %d\n",run,res);
	}

	return 0;
}
