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
 
//const int INF = (int)1E9;
const int INF = INT_MAX/2-1;
const long double EPS = 1E-12;
const long double PI = 3.1415926535897932384626433832795;
//#define y1 usfogiudsogndiogbdouigfbsdlifgsdbg
typedef vector<int> vint;
typedef pair<int,int> pii;

#undef assert
#define assert(expr){if (!(expr)) { ++*(char*)0; } }

#ifdef acm
#include "deb.h"
#define dbg(...) fprintf(stderr, __VA_ARGS__)
#else
#define dbg(...) ;
#define deb(...) ;
#endif

#define MAXN 10000
int d[MAXN+1];
int l[MAXN+1];

int dp[MAXN+10];

void solve(){
	int n; scanf("%d",&n);
	REP(i,0,n) scanf("%d%d",&d[i],&l[i]);
	int d0; scanf("%d",&d0);
	_(dp,0);
	d[n]=d0;
	l[n]=d0;
	dp[0]=d[0];
	for(int i=0;i<n;i++){
		for(int j=1;i+j<=n;j++){
			int delta = d[i+j]-d[i];
			if (dp[i]>=delta){
				dp[i+j]=max(dp[i+j],min(delta,l[i+j]));
			}
		}
	}
	puts(dp[n] ? "YES" : "NO");
}

int main(){
#ifdef acm
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	freopen("error.txt", "wt", stderr);
#endif
	int t; scanf("%d\n",&t);
	for(int i=1;i<=t;i++){
		printf("Case #%d: ",i);
		solve();
	}
	//solve();

#ifdef acm
	//printf("\n\n\n\n\n%.3lf\n", clock()*1e-3);
#endif
	return 0;
}