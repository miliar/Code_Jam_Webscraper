#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/STACK:200000000")

#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <algorithm>
#include <utility>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <queue>
#include <iostream>
#include <sstream>
#include <stack>
#include <limits>
#include <cassert>
#include <ctime>
#include <list>
#include <bitset>
#include <stdlib.h>
#include <string.h>
#include <limits.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned uint;
 
template<typename T> inline T Abs(T a){ return a>0 ? a : -a; }
template<typename T> inline T sqr(T a){ return a*a; }
template<typename T> inline void relaxMin(T &a,T b){ if (b<a) a=b; }
template<typename T> inline void relaxMax(T &a,T b){ if (b>a) a=b; }

#define _(a,val) memset(a,val,sizeof a);
#define REP(i, a, b) for(int i(a),_bb(b); i < _bb; ++i)
//#define REP(i, a, b) for(int i = (a); i < (b); ++i)
#define REPD(i, a, b) for(int i = (b) - 1; i >= a; --i)
#define pb push_back
#define mp make_pair
#define all(a) a.begin(), a.end()
 
const int INF = (int)1E9;
//const int INF = INT_MAX/2-1;
const long double EPS = 1E-9;
const long double PI = 3.1415926535897932384626433832795;
#define y0 idfgosfgdgdfgd
#define y1 idfgoseincdjkg
typedef vector<int> vint;
typedef pair<int,int> pii;

#undef assert
#define assert(expr){if (!(expr)) { ++*(char*)0; } }

char f[10][10];

void solve(){
	REP(i,0,4) cin>>f[i];

	bool found = false;
	REP(tt,0,2){
		char c = tt==0 ? 'X' : 'O';
		bool win = false;
		bool ok;
		REP(i,0,4){
			ok = true;
			REP(j,0,4) if (f[i][j]!=c && f[i][j]!='T')
				ok = false;
			if (ok) win = true;
			ok = true;
			REP(j,0,4) if (f[j][i]!=c && f[j][i]!='T')
				ok = false;
			if (ok) win = true;
		}
		ok = true;
		REP(i,0,4) if (f[i][i]!=c && f[i][i]!='T')
			ok = false;
		if (ok) win = true;
		ok = true;
		REP(i,0,4) if (f[i][3-i]!=c && f[i][3-i]!='T')
			ok = false;
		if (ok) win = true;
		if (win){
			assert(!found);
			printf("%c won\n",c);
			found = true;
			//return;
		}
	}
	if (found) return;
	bool ok = true;
	REP(i,0,4) REP(j,0,4) if (f[i][j]=='.') ok = false;
	if (ok) puts("Draw"); else puts("Game has not completed");
}


int main(){
#ifdef acm
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	freopen("error.txt", "wt", stderr);
#endif
	srand(time(0));
	//srand(0xA1B2C3D4);
	int t; cin>>t;
	REP(i,0,t){
		printf("Case #%d: ",i+1);
		solve();
	}

#ifdef acm
	//printf("\n\n\n\n\n%.3lf\n", clock()*1e-3);
#endif
	return 0;
}