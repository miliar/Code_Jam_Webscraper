#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/STACK:64000000")
 
#include <cstdio>
#include <cstdlib>
#include <ctime>
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
#include <time.h>
#include <assert.h>
#include <cstring>
#include <list>
#include <bitset>
using namespace std;
 
typedef long long int64;
typedef long long lint;
 
//template<typename T> inline T abs(T a){ return a>0 ? a : -a }
template<typename T> inline T sqr(T a){ return a*a; }
template<typename T> inline void relax_min(T &a,T b){ if (b<a) a=b; }
template<typename T> inline void relax_max(T &a,T b){ if (b>a) a=b; }
 
//#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define forn(i, n) for(int i=0,_n(n); i < _n; i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define pb push_back
#define mp make_pair
#define all(a) a.begin(), a.end()
#ifdef _DEBUG
#define DEB(x) x
#define _assert(k) _ASSERT((k))
#else
#define _assert(expr) if (!(expr)) exit(1);
#define DEB(x) ;
#endif
 
const int INF = (int)1E9;
//const int INF = INT_MAX/2;
const int64 INF64 = (int64)1E18;
const long double EPS = 1E-8;
//#define M_PI PI
const long double PI = 3.1415926535897932384626433832795;
typedef vector<int> vint;
typedef vector <pair<int,int> > vpint;
typedef vector<vint> vvint;

//int b[1000],e[1000],w[1000];
vpint a;

int cmp(pair<int,int> a,pair<int,int> b){
	return a.second<b.second;
}

void solve(){
	int x,s,r,t,n; cin>>x>>s>>r>>t>>n;
	assert(s>=0 && r>=0);
	int l = x;
	forn(i,n){
		//cin>>b[i]>>e[i]>>w[i];
		int b,e,w;
		cin>>b>>e>>w;
		if (w>0){
			a.pb(mp(e-b,w));
			l-=e-b;
		}
	}
	a.pb(mp(l,0));
	/*double ans = 0;
	int d = min(l,(s+r)*t);
	ans += double(d)/(s+r);
	ans += double(l-d)/(s);
	double tt = t - double(d)/(s+r);*/
	double tt=t;
	double ans = 0;
	sort(all(a),cmp);
	forn(i,a.size()){
		double ll = a[i].first;
		double sp = a[i].second + r;
		double d = min(double(ll),sp*tt);
		ans += d/sp;
		ans += (ll-d)/(a[i].second + s);
		tt -= d/sp;
	}
	printf("%.9f\n",ans);
	a.clear();
}

#define TASK "A"
int main(){
	freopen("A-large.in", "rt", stdin);
	//freopen(TASK"-small.in", "rt", stdin);
	freopen(TASK".out", "wt", stdout);
#ifdef acm
	//freopen("input.txt", "rt", stdin);
	//freopen("output.txt", "wt", stdout);
#endif
	//while(!feof(stdin))
	int t; scanf("%d\n",&t);
	for(int i=1;i<=t;i++){
		printf("Case #%d: ",i);
		solve();
		fflush(stdout);
	}

	return 0;
}