/*{{{*/
/*includes e defines*/
#include <iostream>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <sstream>
using namespace std;
typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef pair<int,int> pii;
#define sz(A) (int)(A).size()
#define FOR(A,B) for(int A=0; A < (int) (B);A++)
#define FOREACH(A,B) for((__typeof (B).begin) A = (B).begin(); A != (B).end(); A++)
#define pb push_back
#define all(x) x.begin() , x.end()
#define mp make_pair
/*}}}*/
/*{{{*/
/*main*/
void solveCase();
int main() {
	int TESTES; scanf("%d", &TESTES);
	for(int TESTE = 1; TESTE <= TESTES; TESTE++) {
		printf("Case #%d: ", TESTE);
		solveCase();
	}
    return 0;
}
/*}}}*/

int p;
vector<int> g;
map< pii, int > pd;
#define inf 1000

int solve(int at, int pode) {
	if(pode < 0) return -inf;
	if(at < 0) {
		if(pode) return -inf;
		return 0;
	}
	if( pd.count( mp(at,pode) ) ) return pd[ mp(at,pode) ];

	int ans = -inf;
	int v = g[at];

	int t = v/3;

	if(v % 3 == 0) {
		if(v == 30 || v == 0) ans = solve(at-1, pode) + (t >= p);
		else {
			int a = solve(at-1, pode) + (t >= p);
			int b = solve(at-1, pode-1) + (t+1 >= p);
			ans = max(a,b);
		}
	} else if( v % 3 == 1 ) {
		if(v == 1) ans = solve(at-1, pode) + (1 >= p);
		else {
			int a = solve(at-1, pode) + (t+1 >= p);
			int b = solve(at-1, pode-1) + (t+1 >= p);
			ans = max(a,b);
		}
	} else {
		if(v == 29) ans = solve(at-1, pode) + 1;
		else {
			int a = solve(at-1, pode) + (t+1 >= p);
			int b = solve(at-1, pode-1) + (t+2 >= p);
			ans = max(a,b);
		}
	}

	return pd[ mp(at,pode) ] = ans;
}

void solveCase() {
	int n,s;
	cin >> n >> s >> p;
	g.clear();
	g.resize(n);
	FOR(i, n) cin >> g[i];
	pd.clear();

	cout << solve(n-1, s) << endl;
}

