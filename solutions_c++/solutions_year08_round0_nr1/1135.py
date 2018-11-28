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

const int maxS = 110;
const int maxQ = 1010;

int S, Q;
map<string,int> engine;
VI query;
VVI best;

int main()
{
	int run, nruns;
	char tmp[255];
	
	scanf("%d\n",&nruns);

	for(run=0; run<nruns; run++) {

		engine = map<string,int>();
		query = VI();
		
		scanf("%d\n",&S);
		for(int i=0; i<S; i++) {
			fgets(tmp,255,stdin);
			while ( tmp[strlen(tmp)-1]=='\n' ) tmp[strlen(tmp)-1] = 0;
//			debug("%d: %s\n",i,tmp);
			engine[string(tmp)] = i;
		}

//		debug("read %d engines\n",S);

		scanf("%d\n",&Q);

		for(int i=0; i<Q; i++) {
			fgets(tmp,255,stdin);
			while ( tmp[strlen(tmp)-1]=='\n' ) tmp[strlen(tmp)-1] = 0;
			query.PB(engine[string(tmp)]);
//			debug("%d: %s = %d\n",i,tmp,engine[string(tmp)]);
		}
		
//		debug("read %d queries\n",Q);
//		for(int i=0; i<Q; i++) debug("query[%d] = %d\n",i,query[i]);
		
		best = VVI(Q+1,VI(S,infty));

		for(int i=0; i<S; i++) best[0][i] = 0;

		for(int q=0; q<Q; q++) {
			for(int s1=0; s1<S; s1++)
				for(int s2=0; s2<S; s2++) {
					int ns = best[q][s1] + (s1==s2 ? 0 : 1);
					if ( query[q]!=s2 && ns<best[q+1][s2] ) {
//						debug("updating %d %d -> %d to %d\n",q,s1,s2,ns);
						best[q+1][s2] = ns;
					}
				}
//			for(int s=0; s<S; s++) debug("%d ",best[q+1][s]); debug("\n");
		}

		int res = infty;
		for(int s=0; s<S; s++) res <?= best[Q][s];

		printf("Case #%d: %d\n",run+1,res);
	}

	return 0;
}
