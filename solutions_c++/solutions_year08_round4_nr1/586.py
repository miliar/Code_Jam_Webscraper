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

#define DEBUGGING 1

#if defined(DEBUGGING)
#define debug(...) fprintf(stderr,__VA_ARGS__)
#else
#define debug(...)
#endif

const int infty = 999999999;

int M, V, nint;
VI tree, val, best, change;

int rec(int i)
{
	if ( i>=nint ) {
		if ( tree[i]==V ) best[i] = 0;
		return tree[i];
	}

	int left  = rec(2*i+1);
	int right = rec(2*i+2);
	if ( tree[i] ) {
		val[i] = left && right;
	} else {
		val[i] = left || right;
	}

	if ( val[i]==V ) {
		best[i] = 0;
	} else {
		if ( (tree[i]==1 && V==0) ||
			 (tree[i]==0 && V==1) ) {
			best[i] <?= min(best[2*i+1],best[2*i+2]);
		} else {
			best[i] <?= best[2*i+1]+best[2*i+2];
		}
		if ( change[i] ) {
			if ( (tree[i]!=1 && V==0) ||
				 (tree[i]!=0 && V==1) ) {
				best[i] <?= min(best[2*i+1],best[2*i+2])+1;
			} else {
				best[i] <?= best[2*i+1]+best[2*i+2]+1;
			}
		}
	}

//	debug("pos %d: val=%d, change=%d, best=%d\n",i,val[i],change[i],best[i]);
	return val[i];
}

int main()
{
	int run, nruns;
	
	scanf("%d\n",&nruns);

	for(run=0; run<nruns; run++) {
		scanf("%d %d\n",&M,&V);
		
		nint = (M-1)/2;

		tree = VI(M);
		change = VI(nint);
		val  = VI(nint);
		best = VI(M,infty);

		int i;
		for(i=0; i<nint; i++) scanf("%d %d\n",&tree[i],&change[i]);
		for(; i<M; i++) scanf("%d",&tree[i]);

		rec(0);

		if ( best[0]<infty ) {
			printf("Case #%d: %d\n",run+1,best[0]);
		} else {
			printf("Case #%d: IMPOSSIBLE\n",run+1);
		}
	}

	return 0;
}
