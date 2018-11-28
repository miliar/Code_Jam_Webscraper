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

void solve(){
	int k; cin>>k;
	int px,py; px=py=1;
	int tx,ty; tx=ty=0;
	int time = 0;
	forn(i,k){
		char A[10]; int b; cin>>A>>b;
		if (*A=='O'){
			int dt = abs(b-px);
			tx=time=max(tx+dt,ty)+1;
			px=b;
		}else if (*A=='B'){
			int dt = abs(b-py);
			ty=time=max(tx,ty+dt)+1;
			py=b;
		}else assert(false);
	}
	cout<<time<<endl;
}

#define TASK "A"
//#define INPUTSIZE "small"
#define INPUTSIZE "large"
int main(){
	freopen(TASK"-"INPUTSIZE".in", "rt", stdin);
	freopen(TASK"-"INPUTSIZE".out", "wt", stdout);
#ifndef ONLINE_JUDGE
	//freopen("input.txt", "rt", stdin);
	//freopen("output.txt", "wt", stdout);
//#else
//	freopen("A-small-practice.in", "rt", stdin);
//	freopen("A-small-practice.out", "wt", stdout);
#endif
	//while(!feof(stdin))
	int n; scanf("%d\n",&n);
	for(int i=1;i<=n;i++){
		printf("Case #%d: ",i);
		solve();
		fflush(stdout);
	}

	return 0;
}