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
    int t; cin>>t;
    FOR(_i,t) {
		int n,m; cin >>n>>m;
		set<string> dirs;
		FOR(i,n) {
			string d; cin >> d;
			dirs.insert(d);
		}

        int64 res=0;
		FOR(i,m)
		{
			string create;
			cin >> create;

			int idx=0;
			while((idx = create.find('/', idx + 1)) != -1) {
				string curr = create.substr(0,idx);
				if (dirs.count(curr) == 0) 
				{
					++res;
					dirs.insert(curr);
				}
			}
			if (create.back() != '/' && dirs.count(create) == 0)
			{
				++res;
				dirs.insert(create);
			}
		}

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
