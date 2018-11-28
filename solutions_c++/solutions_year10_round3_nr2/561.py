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

int const MAXN=1010;

int n;
int c;

void tab(int k){
	REP(i,k) printf(" ");
}

int mem[11][MAXN][MAXN];

/* zaklada: a ok, b nie ok, a<b */
int oblicz_zgrubne(int a, int b){
	if(a*c>=b) return 0;
	int s=b/c+(b%c!=0?1:0);
	//printf("[%d,%d]: %d\n", a,b,s);
	return 1+((a<s)?oblicz_zgrubne(a,s):0);
}

int oblicz(int a, int b){
	if(a*c>=b) return 0;
	if(mem[c][a][b]==0){
		int wyn=2000000000;
		FOR(i,a+1,b-1){
			wyn=min(wyn,1+max(oblicz(a,i),oblicz(i,b)));
		}
		mem[c][a][b]=wyn;
	}
	return mem[c][a][b];
}

void zrob(int tc){
	int a,b;
	scanf("%d%d%d", &a,&b,&c);
	int wywy;
	printf("Case #%d: %d\n", tc,oblicz(a,b));

}

int main() {
	int t;
	
	
	scanf("%d", &t);
	FOR(i,1,t) zrob(i);

	return 0;
}

