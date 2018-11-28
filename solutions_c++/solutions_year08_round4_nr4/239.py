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
#define FORE(i,a)  for(VAR(i,a.begin()); i!=a.end(); ++i)

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

int calc(string s) {
	
	int N = SIZE(s);
	char last = '#';
	int ret = 0;
	REP(i, N+1) {
		if(i < N && s[i] == last) continue;
		else {
			if(i < N) ++ret;
			last = s[i];
		}
	}
	return ret;
}
void solve(void)
{
	
	int perm[5];
	int k;
	scanf("%d\n", &k);

	REP(i, k) perm[i] = i;
	
	char buff[2000];
	gets(buff);
	
	int ret = INF;
	do {
		string s = string(buff);
		for(int i = 0; i < SIZE(s); i += k) {
			REP(j, k) s[i + j ] = buff[i + perm[j]];
		}
		
		ret = min(ret, calc(s));
	}while(next_permutation(perm, perm+k));
	
	printf("%d\n", ret);
}

int main(void)
{
	int T, C = 1;
	scanf("%d", &T);
	while(T--) { printf("Case #%d: ",C++); solve(); }
	return (0);
}
