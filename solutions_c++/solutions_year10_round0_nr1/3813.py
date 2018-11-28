#include <string>
#include <iostream>
#include <sstream>
#include <vector>
#include <cmath>
#include <cctype>
#include <cstdio>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <cassert>
using namespace std;

/*PREWRITTEN CODE BEGINS HERE*/
#define MP make_pair
#define PB push_back
#define F first
#define S second
#define SIZE(x) ( (int)((x).size()) )
#define CS c_str()
#define EL printf("\n")

#define ALL(v) (v).begin(), (v).end()
#define REP(i,n) for(int i=0,_n=(n); i<_n; ++i)
#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b; ++i)
#define FORD(i,a,b) for(int i=(a),_b=(b); i>=_b; --i)
#define VAR(a,b) __typeof (b) a=b
#define FORE(i,a)  for(VAR(i,(a).begin()); i!=(a).end(); ++i)

typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<long long> VLL; 
typedef vector<vector<int> > VVI;
typedef vector<vector<string> > VVS;
/*PREWRITTEN CODE ENDS HERE*/
inline int RI() { int xx; scanf("%d",&xx); return xx; }
typedef long double LD;
const int INF = 1010000000;
const double EPS = 1e-9;
/*SOLUTION BEGINS HERE*/

bool solve()
{
	int N, K;
	scanf("%d %d", &N, &K);
	int pot = 1<<N;
	K %= pot;
	return K == pot-1;
}
int main(void)
{
	int T;
	scanf("%d", &T);
	FOR(i,1,T) 
		printf("Case #%d: %s\n", i, solve() ? "ON" : "OFF");
	return (0);
}
