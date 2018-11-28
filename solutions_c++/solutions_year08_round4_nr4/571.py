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

int k;
string S, P;

long long fac(long long n) { return n==0 ? 1 : n*fac(n-1); }

template <class T> vector<T> perm_perm(vector<T> orig, int index)
{
	int n = orig.size();
	vector<T> perm = orig;
	VI used(n,0);
	
	for(int i=0; i<n; i++) {
		int j, pos;
		pos = (index % fac(n-i) ) / fac(n-i-1);
		for(j=0; pos>0; j++) if ( ! used[j] ) pos--;
		while ( used[j] ) j++;
		perm[j] = orig[i];
		used[j] = 1;
	}
	return perm;
}

int main()
{
	int run, nruns;
	
	scanf("%d\n",&nruns);

	for(run=0; run<nruns; run++) {

		char tmp[50010];
		
		scanf("%d %s",&k,tmp);
		S = string(tmp);
		P = S;
			
		int res = S.length();
		
		VI orig(k);
		VI perm;

		for(int i=0; i<k; i++) orig[i] = i;
		
		for(int i=0; i<fac(k); i++) {
			perm = perm_perm(orig,i);

// 			debug("perm =");
// 			for(int j=0; j<perm.size(); j++) debug(" %d",perm[j]);
// 			debug("\n");

			for(int j=0; j<S.length(); j++) {
//				debug("foo %d -> %d\n",j,k*(j/k)+perm[j%k]);
			
				P[k*(j/k)+perm[j%k]] = S[j];
			}

			char last = '#';
			int size = 0;
			for(int j=0; j<P.length(); j++) {
				if ( P[j]!=last ) {
					size++;
					last = P[j];
				}
			}

//			debug("%s -> %s = %d\n",S.c_str(),P.c_str(),size);

			res <?= size;
		}

		printf("Case #%d: %d\n",run+1,res);
	}

	return 0;
}
