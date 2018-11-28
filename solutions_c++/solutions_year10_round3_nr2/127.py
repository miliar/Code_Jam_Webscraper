#include<algorithm>
#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<queue>
#include<set>
#include<map>
#include<cstdio>
#include<cstdlib>
#include<cctype>
#include<cmath>

#define FOR(i,a,b) for(int i=(a),_n=(b); i<=_n; i++)
#define REP(i,n) FOR(i,0,(n)-1)
#define FORD(i,a,b) for(int i=(a),_n=(b);i>=_n; i--)
#define FILL(i,v) memset((i),(v),sizeof((i)))
#define DEBUG(x) cout <<"  >> "<<#x<<" => "<<x <<endl
#define ABS(x) ((x<0) ? –x : x)
#define ALL(x) x.begin(),x.end()
#define MAX(a,b) ((a<b) ? b : a)
#define MIN(a,b) ((a<b) ? a : b)
#define MP make_pair
#define PB push_back
#define INF 1000000000


using namespace std;
typedef long long LL;
const double EPS = 1.e-9;

void OPEN(string name) {
	string in = name + ".in";
	freopen(in.c_str(), "r", stdin);
	string out = name + ".out.txt";
	freopen(out.c_str(), "w", stdout);
}

int count( int P, int add, int lo, int d ) {
	int ret = 0;
	while( P > lo ) ret++, P = (P+add)/d;
	return ret;
}
int main() {
	OPEN("Blarge");
	int ntc;
	scanf("%d", &ntc);
	for(int TC=1, L, P, C; TC <= ntc; TC++) {
		scanf("%d %d %d", &L, &P, &C);
		printf("Case #%d: %d\n", TC, count( count(P,C-1,L, C), 1, 1, 2) );
	}
	return 0;
}
