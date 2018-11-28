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
#include <ctime>

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

char str[100];

int main()
{
	int tn;
	cin>>tn;

	while (tn--) {
		int a,b;
		cin>>a>>b;

		int dp=0;
		FOR(i,a,b+1) {
			itoa(i,str,10);
			int len = strlen(str);
			set<int> s;
			FOR(j,1,len) if (str[j]!='0') {
				int c=0;
				FOR(k,j,len) c*=10, c+=str[k]-48;
				REP(k,j) c*=10, c+=str[k]-48;

				if (i<c && c<=b) {
//					cout<<i<<", "<<c<<endl;
					s.insert(c);
				}
			}
			dp += SZ(s);
		}

		static int qq=0;
		printf("Case #%d: ",++qq);
		cout<<dp<<endl;
	}
	return 0;
}
