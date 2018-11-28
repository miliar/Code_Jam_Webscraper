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

#define MAXN 1000

struct cl{
	int id;
	ll r;
	ll x,y;
	bool operator <(const cl &o){
		if (r == o.r)
			return id < o.id;
		return r > o.r;
	}
} cc[MAXN];

int cmp(cl &a,cl &b){
	return a.id < b.id;
}

void solve(){
	int n;
	ll w,l; cin>>n>>w>>l;
	REP(i,0,n){
		ll r0;
		cin>>r0;
		cc[i].id = i;
		cc[i].r = r0;
	}
	sort(cc,cc+n);

	ll max_l = 0;
	ll cur_w = 0;
	ll cur_l = 0;
	REP(i,0,n){
		ll r0 = cc[i].r;
		if (cur_w+r0 <= w && cur_l+2*r0 <= l){
			cc[i].x = cur_w+r0;
			cc[i].y = cur_l+r0;
			cur_w+=2*r0;
			max_l=max(max_l,cur_l+2*r0);
		}else if (cur_w+r0 <= w && cur_l==0){
			cc[i].x = cur_w+r0;
			cc[i].y = 0;
			cur_w+=2*r0;
			max_l=max(max_l,cur_l+2*r0);
		}else{
			cur_w = 0;
			cur_l = max_l;
			assert(cur_l + r0 <= l);
			if (r0 > w){
				cc[i].x = 0;
				cc[i].y = cur_l + r0;
				cur_l += 2*r0;
				max_l=max(max_l,cur_l+2*r0);
			}else{
				cc[i].x = 0;
				cc[i].y = cur_l+r0;
				cur_w+=r0;
				max_l=max(max_l,cur_l+2*r0);
			}
		}
	}

	sort(cc,cc+n,cmp);

	REP(i,0,n){
		REP(j,i+1,n){
			ll d = sqr(cc[i].x-cc[j].x)+sqr(cc[i].y-cc[j].y);
			ll d2= sqr(cc[i].r+cc[j].r);
			assert(d2<=d);
		}
		assert(cc[i].x>=0 && cc[i].y>=0);
		assert(cc[i].x<=w && cc[i].y<=l);
	}

	REP(i,0,n){
		printf("%lld %lld ",cc[i].x,cc[i].y);
	}
	puts("");
}

int test_N;

int main(){
#ifdef acm
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	freopen("error.txt", "wt", stderr);
#endif
	int t; scanf("%d\n",&t);
	for(int i=1;i<=t;i++){
		test_N = i;
		printf("Case #%d: ",i);
		solve();
	}
	//solve();

#ifdef acm
	//printf("\n\n\n\n\n%.3lf\n", clock()*1e-3);
#endif
	return 0;
}