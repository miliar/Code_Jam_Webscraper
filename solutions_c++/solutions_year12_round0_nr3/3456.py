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
#define assert(expr){if (!(expr)) {char *a = 0; *a = 10;} }

#ifdef acm
#include "deb.h"
#define dbg(...) fprintf(stderr, __VA_ARGS__)
#else
#define dbg(...) ;
#define deb(...) ;
#endif

int shift;
inline bool ok(int v){
	return v>=shift;
}
inline int v_next(int v){
	int u = v%10;
	v/=10;
	v+=shift*u;
	return v;
}
set<pii> used;

void solve(){
	int a,b; cin>>a>>b;
	//if (b<10){ cout<<0<<endl; return; }
	shift=1;
	int k=0;
	while (shift <= a){
		shift*=10;
		k++;
	}
	k--;
	shift/=10;
	int ans = 0;
	for (int i=a;i<=b;i++){
		int x = i;
		REP(j,0,k){
			x = v_next(x);
			if (ok(x) && x>=a && x<=b && x!=i){
				if (used.find(mp(i,x))==used.end() && used.find(mp(x,i))==used.end()){
					ans++;
					used.insert(mp(i,x));
				}
				//cout<<i<<" "<<x<<endl;
			}
		}
	}
	used.clear();
	cout<<ans<<endl;
}


int main(){
#ifdef acm
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	freopen("error.txt", "wt", stderr);
#endif
	int t; scanf("%d\n",&t);
	REP(i,0,t){
		printf("Case #%d: ",i+1);
		solve();
	}
	
#ifdef acm
	//printf("\n\n\n\n\n%.3lf\n", clock()*1e-3);
#endif
	return 0;
}