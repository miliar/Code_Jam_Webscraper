// {{{
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <list>
#include <complex>
#include <stack>
#include <cmath>
#include <iostream>
#include <sstream>
#include <cctype>
#include <cstdlib>
#include <utility>
#include <bitset>
#include <assert.h>
using namespace std;

typedef vector<int> VI;
typedef vector<VI> VII;
typedef vector<string> VS;
typedef long long LL;
typedef long double LD;
typedef pair<int,int> PI;
typedef pair<LD,LD> PD;

#define VAR(v,n) __typeof(n) v=(n)
#define REP(i,n) for(int i=0; i<(n); i++)
#define FOR(i,a,b) for(int i=(a); i<=(b); i++)
#define FORD(i,a,b) for(int i=(a); i>=(b); i--)
#define FORE(i,c) for(VAR(i,(c).begin()); i!=(c).end(); i++)
#define CLR(A,v) memset((A),v,sizeof((A)))

#define PB push_back
#define MP make_pair
#define FI first
#define SE second
#define ALL(x) x.begin(),x.end()
#define SIZE(x) ((int)(x).size())
// }}}

#define M 205

int n;
int xx1,yy1,xx2,yy2;
int T[M][M],R[M][M];


int main() {
	int test,number=0;
	scanf("%d",&test);
	while (test--) {
		printf("Case #%d: ",++number);

		FOR(i,1,100) FOR(j,1,100) T[i][j]=0;
		scanf("%d",&n);
		REP(z,n) {
			scanf("%d%d%d%d",&xx1,&yy1,&xx2,&yy2);
			FOR(i,xx1,xx2) FOR(j,yy1,yy2) T[i][j]=1;
		}

		int res=0;
		while (1) {
			FOR(i,1,100) FOR(j,1,100)
				if (T[i][j]==1) R[i][j]=(T[i-1][j]==1 || T[i][j-1]==1);
				else R[i][j]=(T[i-1][j]==1 && T[i][j-1]==1);
			int ile=0;
			FOR(i,1,100) FOR(j,1,100) T[i][j]=R[i][j],ile+=T[i][j];
			res++;
			if (!ile) break;
		}
	
		printf("%d\n",res);
	}
	return 0;
}
