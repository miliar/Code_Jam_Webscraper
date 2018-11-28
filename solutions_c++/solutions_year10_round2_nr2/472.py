#include <algorithm>
#include <fstream>
#include <string>
#include <queue>
#include <set>
#include <stack>
#include <map>
#include <sstream>
#include <iostream>
#include <cmath>
using namespace std;

typedef unsigned int uint;
typedef long long int64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pI;
typedef pair<string,int> pSI;
typedef pair<int,string> pIS;

#define FOR(i,n) for(int i=0, upTo##i=n; i<upTo##i; ++i)
#define REVFOR(i,n) for(int i=(n)-1; i>=0; --i)
#define FOR2(i,b,n) for(int i=b; i<(n); ++i)
#define REVFOR2(i,b,n) for(int i=(n)-1; i>=b; --i)
#define SC(i) scanf("%d", i)
#define ALL(C) (C).begin(), (C).end()
#define RALL(C) (C).rbegin(), (C).rend()
#define MIN(C) *min_element(ALL(C))
#define MAX(C) *max_element(ALL(C))
#define A first
#define B second

void start() {
    int c; cin>>c;
    FOR(_i,c) {
		int n,k,b,t; cin>>n>>k>>b>>t;
		vi x(n);
		FOR(i,n) cin >> x[i];
		vi v(n);
		FOR(i,n) cin >> v[i];
		
        int64 res=0;

		REVFOR(i,n)
		{
			if (x[i] + v[i]*t >= b)
			{
				res += x.size() - i - 1;

				--k;
				x.erase(x.begin() + i);
				v.erase(v.begin() + i);
			} 

			if (k == 0)
				break;
		}

		if (k > 0)
			printf("Case #%d: IMPOSSIBLE\n", _i+1);
		else
			printf("Case #%d: %lld\n", _i+1, res);
    }
}

int main(void) {
#ifdef LOCAL
	extern void runtest();
	runtest();
#else
	start();
#endif

	return 0;
}
