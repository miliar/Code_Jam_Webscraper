#define _CRT_SECURE_NO_WARNINGS
#include <numeric>
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <bitset>
#include <vector>
#include <map>
#include <queue>
#include <deque>
#include <set>
#include <math.h>
#include <assert.h>
#include <time.h>
#include <stdio.h>
#include <string.h>
#include <string>
#include <sstream>

#pragma comment(linker, "/STACK:256000000")
using namespace std;
typedef long long ll;
template<typename T> int size(T &a) {return (int)a.size();}
template<typename T> T sqr(T a)  { return a * a; }

#define fi first
#define se second
#define VAR(a,b) __typeof(b) a=(b)
#define FOR(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define REP(i,a,b) for(int i=(a);i<(b); ++i)
#define REPD(i,a,b)for(int i=(b)-1;i>=a;--i)
#define _(a,b) memset((a), (b), sizeof(a))
#define all(a) a.begin(), a.end()
#define mp make_pair
#define pb push_back
#define ve vector


void solve(){
	ve<string> s(4);
	REP(i,0,4) cin >> s[i];
	
	bool good1=false;
	bool good2=false;
	REP(i, 0, 4) {
		bool ok1=true;
		bool ok2=true;
		REP(j,0,4) {
			ok1 &= s[i][j] == 'X' || s[i][j] == 'T';
			ok2 &= s[i][j] == 'O' || s[i][j] == 'T';
		}
		good1|=ok1;
		good2|=ok2;
	}
	REP(j, 0, 4) {
		bool ok1=true;
		bool ok2=true;
		REP(i,0,4) {
			ok1 &= s[i][j] == 'X' || s[i][j] == 'T';
			ok2 &= s[i][j] == 'O' || s[i][j] == 'T';
		}
		good1|=ok1;
		good2|=ok2;
	}
	bool ok1=true, ok2=true;
	REP(i ,0, 4) {
		ok1 &= s[i][i] == 'X' || s[i][i] == 'T';
		ok2 &= s[i][i] == 'O' || s[i][i] == 'T';
	}
	good1|=ok1;
	good2|=ok2;
	ok1=true, ok2=true;
	REP(i ,0, 4) {
		ok1 &= s[i][4-i-1] == 'X' || s[i][4-i-1] == 'T';
		ok2 &= s[i][4-i-1] == 'O' || s[i][4-i-1] == 'T';
	}
	good1|=ok1;
	good2|=ok2;
	if(good1) {
		printf("X won");
		return;
	}
	if (good2) {
		printf("O won");
		return;
	}
	int c = 0;
	REP(i ,0, 4) c += count(all(s[i]), '.');
	if (c == 0) printf("Draw");
	else printf("Game has not completed");
	
}
int main() {
#ifdef air
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	//ios_base::sync_with_stdio(false);
	
	int test;
	cin >> test;
	REP(t, 0, test) {
		printf("Case #%d: ", t+1);
		solve();
		printf("\n");
	}
	

#ifdef air
	//printf("\n\n%lf\n", clock() * 1e-3);
#endif

	return 0;
}