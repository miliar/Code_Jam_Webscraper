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

int main()
{
	int tn;
	cin>>tn;
	while (tn--) {
		int n;
		cin>>n;
		VI dt(n);
		REP(i,n) {
			cin>>dt[i];
			dt[i]--;
		}

		double dp=0;
		VI chk(n,0);
		REP(i,n) if (!chk[i]) {
			int p=i;
			int h=1;
			chk[p]=true;
			p=dt[p];
			while (p!=i) {
				chk[p]=true;
				p=dt[p];
				h++;
			}
			if (h>1)
				dp+=h;
		}

		static int pp=0;
		printf("Case #%d: %.6lf\n",++pp,dp);
	}
	return 0;
}
