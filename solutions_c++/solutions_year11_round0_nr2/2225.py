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
	//vector< pair<char,char> > opposed;
	set< pair<char,char> > opposed;
	set< pair<char,char> > combine_set;
	map< pair<char,char> , char > combine_map;
	int c,d,n;
	cin>>c;
	char t[200];
	forn(i,c){
		cin>>t;
		combine_set.insert(mp(t[0],t[1]));
		combine_map[mp(t[0],t[1])]=t[2];
		//combine.pb(mp(mp(t[0],t[1]),t[2]));
	}
	cin>>d;
	forn(i,d){
		cin>>t;
		opposed.insert(mp(t[0],t[1]));
		//opposed.pb(mp(t[0],t[1]));
	}
	vector<int> res;
	cin>>n; cin>>t;
	forn(i,n){
		res.push_back(t[i]);
		pair<int,int> last;
		bool f = true;
		while (res.size()>=2 && f){
			int sz = res.size();
			int a = res[sz-1];
			int b = res[sz-2];
			f=false;
			last = mp(a,b);
			if (combine_set.count(last))
				f=true;
			if (!f){
				last=mp(b,a);
				if (combine_set.count(last))
					f=true;
			}
			if (f){
				res.pop_back();
				res.pop_back();
				res.push_back(combine_map[last]);
			}
		}
		f=true;
		for(int j=0;j<res.size() && f;j++)
			for(int k=j+1;k<res.size() && f;k++){
				if (opposed.count(mp(res[j],res[k])) || opposed.count(mp(res[k],res[j]))){
					res.clear();
					f=false;
					break;
				}
			}
	}
	putchar('[');
	if (res.size()>0) putchar(res[0]);
	if (res.size()>1) for(int i=1;i<res.size();i++) printf(", %c",res[i]);
	putchar(']');
	putchar('\n');
}

#define TASK "B"
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
	int t; scanf("%d\n",&t);
	for(int i=1;i<=t;i++){
		printf("Case #%d: ",i);
		solve();
		fflush(stdout);
	}

	return 0;
}