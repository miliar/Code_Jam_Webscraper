/* autor: Marek Rogala */
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
#include <map>
#include <queue>
#include <set>

using namespace std;
#define VAR(a,b) typeof(b) a=(b)
#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define ALL(x) x.begin(),x.end()
#define PB push_back
#define ST first
#define ND second
#define MP make_pair
#define SIZE(x) ((int)x.size())
typedef long long LL;
const int INF = 1000000000;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;

int const MAXN=1000010;

int n;
int a[MAXN], b[MAXN];

void zrob(int tc){
	int wyn=0;
	scanf("%d", &n);
	REP(i,n) scanf("%d%d",a+i,b+i);
	REP(i,n) FOR(j,i+1,n-1){
		if(a[i]<a[j]&&b[i]>b[j]) wyn++;
		else if(a[i]>a[j]&&b[i]<b[j]) wyn++;
	}
	printf("Case #%d: %d\n", tc, wyn);
}

int main() {
	int t;
	scanf("%d", &t);
	FOR(i,1,t) zrob(i);

	return 0;
}

