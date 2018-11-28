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

int l[1000];
int p[1000];

struct lev{
	int id;
	int l;
	int p;
} v[1000];

int cmp(lev &a,lev &b){
	if (a.p == b.p){
		if (a.l==b.l)
			return a.id < b.id;
		return a.l < b.l;
	}
	return a.p > b.p;
	//if (a.l*a.p == b.l*b.p)
	//	return a.id < b.id;
	//return a.l*a.p > b.l*b.p;
}

void solve(){
	int n; cin>>n;
	//REP(i,0,n) cin>>l[i];
	//REP(i,0,n) cin>>p[i];
	REP(i,0,n) cin>>v[i].l;
	REP(i,0,n) cin>>v[i].p;
	REP(i,0,n) v[i].id=i;
	sort(v,v+n,cmp);
	REP(i,0,n)
		cout<<v[i].id<<" ";
	cout<<endl;
}

int main(){
#ifdef acm
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	freopen("error.txt", "wt", stderr);
#endif
	int test; scanf("%d\n",&test);
	for(int i=1;i<=test;i++){
		printf("Case #%d: ",i);
		solve();
	}

#ifdef acm
	//printf("\n\n\n\n\n%.3lf\n", clock()*1e-3);
#endif
	return 0;
}