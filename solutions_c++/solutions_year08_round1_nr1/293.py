#include <cstdio>
#include <algorithm>
#include <vector>
#include <iostream>
#include <string>

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
#define FORE(it,X) for(__typeof((X).begin()) it=(X).begin(); it!=(X).end(); ++it)

int main()
{
	int tn,qq;

	qq=0;
	cin>>tn;
	while (tn--) {
		int n;
		cin>>n;
		VI x(n),y(n);
		REP(i,n) cin>>x[i];
		REP(i,n) cin>>y[i];

		sort(ALL(x));
		sort(ALL(y));
		reverse(ALL(y));
		
		LL dp=0;
		REP(i,n)
			dp+=(LL)x[i]*y[i];

		printf("Case #%d: ",++qq);
		cout<<dp<<endl;
	}
	return 0;
}
