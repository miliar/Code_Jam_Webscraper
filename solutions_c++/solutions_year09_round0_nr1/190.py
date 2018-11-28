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
#include <queue> 
#include <cctype> 
#include <cstring>

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

int l,d,n;
char dt[5005][32];
string da;

int main()
{
	scanf("%d%d%d",&l,&d,&n);

	REP(i,d) scanf("%s",dt[i]);

	scanf("%d",&n);
	FOR(qq,1,n+1) {
		int dp=0;
		cin>>da;
		REP(i,d) {
			int k=0;
			bool possible = true;
			REP(j,l) {
				char data = dt[i][j];
				char s;
				if (da[k]!='(')	{
					s=da[k];
					if (s != data) {
						possible = false;
						break;
					}
					k++;
				}
				else {
					int q=k+1;
					possible = false;
					while (da[q]!=')') {
						s=da[q];
						if (data == s) possible = true;
						q++;
					}
					k=q+1;
					if (!possible) break;
				}
			}
			if (possible) dp++;
		}
		printf("Case #%d: %d\n",qq,dp);
	}
	return 0;
}
