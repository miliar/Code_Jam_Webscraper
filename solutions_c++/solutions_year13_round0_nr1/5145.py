#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <list>
#include <ctime>
#include <sstream>
#include <queue>
#include <stack>
#include <bitset>
using namespace std;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef long long LL;
#define FOR(x, b, e) for(int x=b; x<=(e); ++x)
#define FORD(x, b, e) for(int x=b; x>=(e); --x)
#define REP(x, n) for(int x=0; x<(n); ++x)
#define VAR(v,n) typeof(n) v=(n)
#define ALL(c) c.begin(),c.end()
#define SIZE(x) (int)x.size()
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define PB push_back
#define ST first
#define ND second
#define mp(x,y) make_pair(x,y)
typedef short int sint;

const int N = 4;

char tab[N+1][N+1];

bool win(char playa) {
	REP(i, N) {
		bool won = true;
		REP(j, N) if (tab[i][j] != playa && tab[i][j] != 'T') won = false;
		if (won) return true;
	}
	REP(i, N) {
		bool won = true;
		REP(j, N) if (tab[j][i] != playa && tab[j][i] != 'T') won = false;
		if (won) return true;
	}
	bool won = true;
	REP(i, N) if (tab[i][i] != playa && tab[i][i] != 'T') won = false;
	if (won) return true;
	won = true;
	REP(i, N) if (tab[i][N - i - 1] != playa && tab[i][N-i-1] != 'T') won = false;
	if (won) return true;
	return false;
}

int solve() {
	REP(i, N)
		scanf("%s", tab[i]);
	int empty = 0;
	REP(i,N)REP(j,N) if (tab[i][j] == '.') empty++;
	if (win('X')) return 0;
	if (win('O')) return 1;
	if (empty == 0) return 2;
	return 3;
}

int main(){
	int t;
	scanf("%d", &t);
	REP(q, t) {
		string res;
		switch (solve()) {
			case 0: 
				res = "X won";
				break;
			case 1:
				res = "O won";
				break;
			case 2:
				res = "Draw";
				break;
			default:
				res = "Game has not completed";
		}
		cout << "Case #" << q+1 << ": " << res << endl;
	}
}