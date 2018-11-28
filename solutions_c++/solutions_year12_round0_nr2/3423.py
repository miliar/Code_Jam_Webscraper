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

int t[200];

void solve(){
	int n,s,p;
	cin>>n>>s>>p;
	REP(i,0,n) cin>>t[i];
	int ans = 0;
	REP(i,0,n){
		int v = t[i];
		int x = v/3;
		if ((v%3) == 0){
			if (x>=p) ans++;
			else if (v>=3 && x+1>=p && s>0){
				ans++;
				s--;
			}
		}else if ((v%3)==1){
			if (x+1>=p) ans++;
		}else if ((v%3)==2){
			if (x+1>=p) ans++;
			else if (v>=2 && x+2>=p && s>0){
				ans++;
				s--;
			}
		}else assert(false);
	}
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