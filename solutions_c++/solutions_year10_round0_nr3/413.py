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
typedef vector<LL> VLL;
typedef vector<VLL> VVLL;
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

int rides, places, ng;
VI g;

VLL next, prof;
VVLL next2, prof2;

int main()
{
	int nruns;
	cin >> nruns;

	for(int run=1; run<=nruns; run++) {

		cin >> rides >> places >> ng;
		g = VI(ng);
		next = prof = VLL(ng);
		next2.clear();
		prof2.clear();
		REP(i,ng) cin >> g[i];

		REP(i,ng) {
			int j;
			for(j=i; prof[i]+g[j]<=places && (j!=i || prof[i]==0); j=(j+1)%ng) prof[i] += g[j];
			next[i] = j;
			debug("i = %d: next = %lld, profit = %lld\n",i,next[i],prof[i]);
		}

		long long res = 0;
		int first = 0;

		for(int k=0; (1<<k)<=rides; k++) {
			debug("k = %d\n",k);
			next2.push_back(next);
			prof2.push_back(prof);
			if ( k>0 ) {
				REP(i,ng) {
					next2[k][i] = next2[k-1][next2[k-1][i]];
					prof2[k][i] = prof2[k-1][i] + prof2[k-1][next2[k-1][i]];
					debug("i = %d: next = %lld, profit = %lld\n",i,next2[k-1][i],prof2[k-1][i]);
					debug("i = %d: next = %lld, profit = %lld\n",i,next2[k][i],prof2[k][i]);
				}
			}

			if ( rides&(1<<k) ) {
				res += prof2[k][first];
				first = next2[k][first];
			}
		}

		printf("Case #%d: %lld\n",run,res);
	}

	return 0;
}
