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
    int n; cin>>n;
    FOR(_i,n) {
		int p; cin>>p;
		int m[1<<10];
		FOR(i,(1<<p)) cin>>m[i];

		vector<vi> v;
		vector<vi> info;
		FOR(i,p) {
			v.push_back(vi());
			info.push_back(vi());
			vi &cv = v.back();
			vi &cinfo = info.back();
			FOR(j,(1<<(p-i-1)))
			{
				int x; cin>>x; cv.push_back(x);
				cinfo.push_back(0);
			}
		}

		FOR(i,(1<<p)) {
			int idx = i;
			int mm = m[i];
			FOR(j,p)
			{
				idx /= 2;
				if (info[j][idx] == 0 && mm > 0)
				{
					info[j][idx] = -1;
					--mm;
				}
				else if (info[j][idx] != 1 && mm <= 0)
					info[j][idx] = 1;
				else if (info[j][idx] == -1)
					--mm;

			}
		}

        int64 res=0;
		FOR(j,p)
		{
			FOR(i,info[j].size())
				if (info[j][i] == 1) ++res;
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
