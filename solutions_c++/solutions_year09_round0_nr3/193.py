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

char dt[1024];
char str[30]="welcome to code jam";
int dy[1024][32]; // 18°¡ ³¡

int main()
{
	int tn,qq=1;

	gets(dt); sscanf(dt,"%d",&tn);
	while (tn--) {
		gets(dt);

		memset(dy,0,sizeof(dy));
		int n=strlen(dt);
		REP(i,n) {
			if (i) dy[i][0]=dy[i-1][0];
			if (dt[i]==str[0]) dy[i][0]++;
			FOR(j,1,19) {
				dy[i][j]=dy[i-1][j];
				if (dt[i]==str[j]) dy[i][j]+=dy[i-1][j-1];
				dy[i][j]%=10000;
			}
		}

		printf("Case #%d: %04d\n",qq++,dy[n-1][18]);
	}
	return 0;
}
