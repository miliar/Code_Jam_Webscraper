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
#define SIZE(x) (int)((x).size())

#define REP(i,n) for(int i=0,_n=(n); i<_n; ++i)
#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b; ++i)
#define RESET(a,c) memset(a,(c),sizeof(a))


/*PREWRITTEN CODE ENDS HERE*/
inline int RI() { int xx; scanf("%d",&xx); return xx; }
typedef long double LD;
const int INF = 1010000000;
const double EPS = 1e-9;
/*SOLUTION BEGINS HERE*/

char combine[200][200], opposed[200][200];

void print_vec(vector<char> v) {
	printf("[");
	REP(i, SIZE(v)) 
		printf( (i==SIZE(v)-1) ? "%c" : "%c, ", v[i]);
	printf("]\n");

}
void solve()
{
	RESET(combine, 0); RESET(opposed, 0);
	int C, O, N;
	char buf[300];
	scanf("%d", &C);
	REP(i, C) {
		scanf("%s", buf);
		combine[buf[0]][buf[1]] = combine[buf[1]][buf[0]] = buf[2];
	}
	scanf("%d", &O);
	REP(i, O) {
		scanf("%s", buf);
		opposed[buf[0]][buf[1]] = opposed[buf[1]][buf[0]] = true;
	}
	scanf("%d", &N);
	scanf("%s", buf);
	
	vector<char> v;
	REP(i, N) {
		v.PB(buf[i]);
		
		while(SIZE(v) > 1) {
			char a = v[SIZE(v)-1], b = v[SIZE(v)-2];
			if(combine[a][b]) {
				v.pop_back(); v.pop_back();
				v.PB(combine[a][b]);
			}
			else break;
		}
		
		REP(i, SIZE(v)) REP(j, i) if(opposed[v[i]][v[j]]) {
			v.clear();
			goto hell;
		}
		//printf("i:%d buf:'%c' list:",i, buf[i]);
		//print_vec(v);
		hell:
		continue;
	}
	print_vec(v);
}

int main(void)
{
	int T = RI();
	FOR(i,1,T) {
		printf("Case #%d: ", i);
        solve();
	}
	return (0);
}
