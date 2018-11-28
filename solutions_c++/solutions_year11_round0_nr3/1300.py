#include <vector>
#include <map>
#include <set>
#include <stack>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>
#include <cctype>
#include <cstring>
#include <queue>
#include <cassert>

using namespace std;

typedef long long LL;
typedef long double LD;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;

#define MP make_pair
#define ST first
#define ND second
#define PB push_back
#define FOR(i,a,b) for( int i=(a); i<(b); ++i)
#define FORD(i,a,b) for( int i=(a); i>(b); --i)
#define REP(i,n) for(int i=0; i<(n); ++i)
#define ALL(X) (X).begin(),(X).end()
#define SZ(X) (int)(X).size()
#define FORE(it,X) for(__typeof((X).begin()) it=(X).begin(); it!=(X).end();++it)

int dt[1024];

int main()
{
	int tn;
	cin>>tn;

	while (tn--) {
		int n,b=0;
		cin>>n;
		REP(i,n) {
			cin>>dt[i];
			b^=dt[i];
		}

		static int qq=1;
		printf("Case #%d: ",qq++);

		if (b) {
			printf("NO\n");
			continue;
		}

		sort(dt,dt+n);
		LL dp=0;
		FOR(i,1,n)
			dp+=dt[i];
		cout<<dp<<endl;
	}
	return 0;
}
