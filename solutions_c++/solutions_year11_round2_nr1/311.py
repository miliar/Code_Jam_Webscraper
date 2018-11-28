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

char s[110][110];
int win[110];
int cnt[110];

double wp[110];
double owp[110];
double oowp[110];

void solve(){
	int n; scanf("%d\n",&n);
	forn(i,n) gets(s[i]);
	forn(i,n){
		win[i]=0;
		cnt[i]=0;
		forn(j,n){
			if (s[i][j]=='1'){
				win[i]++;
				cnt[i]++;
			}else if (s[i][j]=='0'){
				cnt[i]++;
			}
		}
		wp[i]=(win[i]+0.0)/cnt[i];
	}
	forn(i,n){
		owp[i]=0;
		forn(j,n) if (s[i][j]!='.'){
			owp[i]+=(win[j]-(s[j][i]-'0'))/(cnt[j]-1.0);
		}
		if (cnt[i]>0)
		owp[i]/=(cnt[i]);
	}
	forn(i,n){
		oowp[i]=0.0;
		forn(j,n)
			if (s[i][j]!='.')
				oowp[i]+=owp[j];
		if (cnt[i]>0)
		oowp[i]/=(cnt[i]);
	}
	putchar('\n');
	forn(i,n){
		double res = 0.25*wp[i]+0.5*owp[i]+0.25*oowp[i];
		printf("%.8lf\n",res);
	}
}

#define TASK "A"
int main(){
	//freopen(TASK"-small-attempt1.in", "rt", stdin);
	freopen(TASK"-large.in", "rt", stdin);
	freopen(TASK"2.out", "wt", stdout);
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