/*BRUM BRUM BRUM*/

// input/output
#include <cstdio>
#include <iostream>
// structures
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <tuple>
// other stuff
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <utility>

using namespace std;

#define dbg if(0)
#ifdef EBUG 
    #define dbg if(1) 
#endif
#define db(x) dbg cerr << #x << "\t: " << (x) <<  endl;
#define dbv(x) dbg{ cerr << #x << "\t: "; FOREACH(it, x) cerr << *it << " "; cerr << endl;}

// vlastny assert
#define EXIT 0
#define WA 3
#define TLE 1
#define EXC 2
#define assert(x, ...) if(!(x)){ cerr << "F: " << __FUNCTION__ << "(), L: " << __LINE__ << ", (" << #x << ") isn\'t true\n"; error_exit(__VA_ARGS__); }
void error_exit(int error=EXIT){
    switch(error){
        case EXIT:   exit(0);                    break;
        case WA:     cout << "BRUM BRUM BRUM\n"; break;
        case TLE:    while(47){};                break;
        case EXC:    int *q47; q47[1000047] = 47;break;
    }
}

#define MINIM(x, y) x = min(x, (y))
#define MAXIM(x, y) x = max(x, (y))
#define iter(x) typeof((x).begin())
#define FOR(i,n) for(long long i = 0; i < (n); ++i)
#define FOR1(i, n) for(long long i = 1; i <= (n); ++i)
#define FOREACH(it, str) for(typeof((str).begin()) it = (str).begin(); it != (str).end(); ++it)
#define mp make_pair
#define mt make_tuple
#define pf printf
#define sf scanf
#define PASS
typedef long long ll;
const long long INF = 2000000000;
const double EPS = 1e-9;
typedef pair<long long, long long> pll;
typedef pair<int,int> pii;

void vyhral(int x, int t){
	if(x == 1) cout << "Case #" << t << ": O won" << endl;
	if(x == 2) cout << "Case #" << t << ": X won" << endl;
}

void solve(int t){
	db(t);
	vector<vector<int> > a(4, vector<int> (4,0));
	FOR(i, 4){
		FOR(j, 4){
			char c;
			cin >> c;
			switch(c){
				case 'O': a[i][j] = 1; break;
				case 'X': a[i][j] = 2; break;
				case 'T': a[i][j] = 3; break;
			}
		}
	}

	dbg{
		FOR(i, 4){ FOR(j, 4) cerr << a[i][j]; cerr << endl;}
	}

	// ci niekto vyhral
	for(int p = 1; p < 3; ++p){
		// rows
		FOR(i, 4){
			int amount = 0;
			FOR(j, 4) amount += (a[i][j] == p || a[i][j] == 3)?1:0;
			if(amount == 4){ vyhral(p,t); return;}
		}
		// columns
		FOR(j, 4){
			int amount = 0;
			FOR(i, 4) amount += (a[i][j] == p || a[i][j] == 3)?1:0;
			if(amount == 4){ vyhral(p,t); return;}
		}
		// diagonals
		{
			int amount = 0;
			FOR(i, 4) amount += (a[i][i] == p || a[i][i] == 3)?1:0;
			if(amount == 4){ vyhral(p,t); return;}
		}
		{
			int amount = 0;
			FOR(i, 4) amount += (a[i][3-i] == p || a[i][3-i] == 3)?1:0;
			if(amount == 4){ vyhral(p,t); return;}
		}
	}

	// ak nikto nevyhral
	int amount = 0; FOR(i, 4) FOR(j, 4) amount += (a[i][j] > 0)?1:0;
	if(amount < 16) cout << "Case #" << t << ": Game has not completed" << endl;
	else cout << "Case #" << t << ": Draw" << endl;
}

int main(){
    int T;
    cin >> T;
    FOR1(t, T){
    	solve(t);
    }
}
