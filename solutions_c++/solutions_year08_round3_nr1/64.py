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

const int infty = 999999999;

#define DEBUGGING 1

#if defined(DEBUGGING)
#define debug(...) fprintf(stderr,__VA_ARGS__)
#else
#define debug(...)
#endif

int P, K, L;

int main()
{
	int run, nruns;
	
	scanf("%d\n",&nruns);

	for(run=0; run<nruns; run++) {
		scanf("%d %d %d\n",&P,&K,&L);

//		debug("%d %d %d\n",P,K,L);
		
		VI freq(L);

		for(int i=0; i<L; i++) scanf("%d",&freq[i]);

		sort(ALL(freq));

		long long res = 0;

		for(int i=0; i<L; i++) {
			res += freq[i]*((L-i-1)/K+1);
		}

		printf("Case #%d: %lld\n",run+1,res);
	}

	return 0;
}
