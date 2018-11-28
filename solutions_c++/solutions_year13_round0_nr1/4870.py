#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <cctype>
#include <string>
#include <vector>
#include <sstream>
#include <iterator>
#include <numeric>
#include <cmath>
using namespace std;

typedef vector <int > VI;
typedef vector < VI > VVI;
typedef long long LL;
typedef vector < LL > VLL;
typedef vector < double > VD;
typedef vector < string > VS;
typedef pair<int,int> PII;
typedef vector <PII> VPII;
typedef istringstream ISS;

#define REP(i,n) for (int i(0),_n(n); i < _n; ++i)
#define FOR(i,a,b) for (int i(a),_b(b); i < _b; ++i)
#define FORD(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define FOREACH(it, X) for(__typeof((X).begin()) it = (X).begin(); it != (X).end(); ++it)
#define ALL(x) (x).begin(),(x).end()
#define PB push_back
#define PF push_front
#define MP(a,b) make_pair((a),(b))
#define ST first
#define ND second
#define SIZE(x) (int)x.size()
#define debug if(1)printf

int TCases;
int N;
int A, B;


void read_case() {
	cin >> N >> A >> B;
}

void solve_case() {
	bool win_r[4][2], win_c[4][2], win_d[4][2];
	FOR(i,0,4) {
		FOR(j,0,2) {
			win_r[i][j] = true;
			win_c[i][j] = true;
			win_d[i][j] = true;
		}
	}
	bool unfinished = false;
	char ch;
	
	FOR(r,0,4) {
		FOR(c,0,4) {
			scanf(" %c", &ch);
			//cout << ch;
			int d = (r==c?0:(r==3-c?1:2));
			if (ch=='.') {
				unfinished=true;
				win_r[r][0] = win_r[r][1] = false;
				win_c[c][0] = win_c[c][1] = false;
				win_d[d][0] = win_d[d][1] = false;
			}
			else if (ch=='O') {
				win_r[r][1] = false;
				win_c[c][1] = false;
				win_d[d][1] = false;
			}
			else if (ch=='X') {
				win_r[r][0] = false;
				win_c[c][0] = false;
				win_d[d][0] = false;
			}
		}
	}
	
	int winner = 0;
	FOR(i,0,4) {
		if (win_r[i][0] || win_c[i][0]) winner=1;
		if (win_r[i][1] || win_c[i][1]) winner=-1;
	}
	FOR(i,0,2) {
		if (win_d[i][0]) winner=1;
		if (win_d[i][1]) winner=-1;
	}
	
	if (winner) printf("%c won\n", winner==1?'O':'X');
	else if (unfinished) printf("Game has not completed\n");
	else printf("Draw\n");
}

	

int main() {
	cin >> TCases;
	for (int nCase=1; nCase<=TCases; nCase++) {
		read_case();
		cout <<"Case #" << nCase << ": " ;
		solve_case();
	}
	return 0;
}