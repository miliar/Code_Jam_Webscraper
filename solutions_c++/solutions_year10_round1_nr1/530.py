#include <string>
#include <string.h>
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
#define PB push_back
#define CS c_str()

#define REP(i,n) for(int i=0,_n=(n); i<_n; ++i)
#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b; ++i)
#define FORD(i,a,b) for(int i=(a),_b=(b); i>=_b; --i)
#define ALWAYS(f,p) (({bool _wyn=true;f if(!(p)){_wyn=false;break;}_wyn;})) 


typedef vector<string> VS;
/*PREWRITTEN CODE ENDS HERE*/
inline int RI() { int xx; scanf("%d",&xx); return xx; }
typedef long double LD;
const int INF = 1010000000;
const double EPS = 1e-9;
/*SOLUTION BEGINS HERE*/

const int MAX = 60;
const int RED = 0, BLUE = 1;

char buf[2000];
int N, K;
void rot(VS &v)
{
	VS tmp = v;
	REP(i, N) REP(j, N) v[i][j] = tmp[N-1-j][i];
	
}

bool look(VS v, char val)
{
	
	REP(r, N) REP(c, N) {
		
		if(c + K-1 < N && ALWAYS( REP(i,K), v[r][c+i] == val)) return 1;
		if(r + K-1 < N && ALWAYS( REP(i,K), v[r+i][c] == val)) return 1;
		if(r + K-1 < N && c + K-1 < N && ALWAYS( REP(i, K), v[r+i][c+i] == val)) return 1;
		if(r + K-1 < N && c - K+1 >= 0 && ALWAYS( REP(i, K), v[r+i][c-i] == val)) return 1;
	}

	return 0;
}

void down(VS &vec) {
	

	FORD(r, N-1, 0) {
		
		REP(c, N) if(vec[r][c] == 'R' || vec[r][c] == 'B') {
			
			int x = r;
			while(x < N-1 && vec[x+1][c] == '.') ++x;

			swap(vec[r][c], vec[x][c]);
		}
	}
}
int solve() {
	scanf("%d %d\n", &N, &K);
	
	vector<string> vec;
	vec.clear();
	REP(i, N)  {
		scanf("%s\n", buf);
		vec.PB( string(buf));
	}
	
	rot(vec);
	down(vec);	
	//REP(i, N) printf("%s\n", vec[i].CS) ;

	int ret = 0;
	if( look(vec, 'R') ) ret |= 1<<RED;
	if( look(vec, 'B') ) ret |= 1<<BLUE;
	return ret;
}

char *wyn[] = { "Neither", "Red", "Blue", "Both" };
int main(void)
{
	int T = RI();
	FOR(i,1,T) {
		int x = solve();
		printf("Case #%d: %s\n", i, wyn[x]);
	}
	return (0);
}
