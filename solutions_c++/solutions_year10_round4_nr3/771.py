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
    int T; cin>>T;
    FOR(_i,T) {
		int R; cin>>R;
		set<pI> s;
		FOR(i,R)
		{
			int x1,y1,x2,y2; cin>>x1>>y1>>x2>>y2;
			for(int i=x1; i<=x2; ++i) for(int j=y1; j<=y2; ++j) s.insert(pI(i,j));
		}

		int res=0;
		set<pI> s2;
		while(s.size() > 0)
		{
			s2.clear();
			for(set<pI>::const_iterator it=s.begin(); it !=s.end(); ++it) {
				int x = it->first, y=it->second;

				if (s.count(pI(x-1,y+1))) // new
					s2.insert(pI(x,y+1));
				if (s.count(pI(x-1,y)) != 0 || s.count(pI(x,y-1)) != 0)
					s2.insert(*it);
			}

			s.swap(s2);
			++res;
		}

        printf("Case #%d: %d\n", _i+1, res);
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
