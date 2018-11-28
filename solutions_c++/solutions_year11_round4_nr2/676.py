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

char a[600][600];

void solve(){
	int r,c,d; scanf("%d %d %d\n",&r,&c,&d);
	forn(i,r)
		gets(a[i]);
	int k=5;
	int x=1,y=1;
	for(int k=min(r,c);k>=3;k--){
		for(int x=0;x<=r-k;x++){
			for(int y=0;y<=c-k;y++){
				double qx=0,qy=0;
				forn(i,k){
					forn(j,k){
						if (i==0 && j==0) continue;
						if (i==0 && j==k-1) continue;
						if (i==k-1 && j==0) continue;
						if (i==k-1 && j==k-1) continue;
						double dy = (k-1.0)/2.0-i;
						double dx = (k-1.0)/2.0-j;
						qx+=dx*(a[i+y][j+x]-'0'+d);
						qy+=dy*(a[i+y][j+x]-'0'+d);
					}
				}
				if (fabs(qx)<EPS && fabs(qy)<EPS){
					cout<<k<<endl;
					return;
				}
			}
		}
	}
	cout<<"IMPOSSIBLE"<<endl;
	//printf("%.5f %.5f\n",qx,qy);
}

#define TASK "B"
int main(){
	freopen("B-small-attempt0.in", "rt", stdin);
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