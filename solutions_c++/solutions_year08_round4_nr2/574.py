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

int X, Y, A;

class p {
public:
	int x,y;

	p() { x = y = 0; }
	p(int x_, int y_) { x = x_; y = y_; }
};

int main()
{
	int run, nruns;
	
	scanf("%d\n",&nruns);

	for(run=0; run<nruns; run++) {
		scanf("%d %d %d",&X,&Y,&A);

		map<int,p> prods;
		
		int x,y;
		for(x=0; x<=X; x++)
			for(y=0; y<=Y; y++)
				prods[x*y] = p(x,y);

		int x1,y1,x2,y2;
		FOR(it,prods) {
			int res = it->first - A;
//			debug("prod = %d: %d,%d\n",it->first,it->second.x,it->second.y);
			if ( prods.count(res) ) {
// 				debug("prod1 = %d: %d,%d\n",it->first,it->second.x,it->second.y);
// 				debug("prod2 = %d: %d,%d\n",res,prods[res].x,prods[res].y);
				x1 = it->second.x;
				y2 = it->second.y;
				x2 = prods[res].x;
				y1 = prods[res].y;
				goto sol;
			}
		}
		printf("Case #%d: IMPOSSIBLE\n",run+1);
		continue;
		
	  sol:
//		debug("area = %d =? %d\n",x1*y2-x2*y1,A);
		printf("Case #%d: 0 0 %d %d %d %d\n",run+1,x1,y1,x2,y2);
	}

	return 0;
}
