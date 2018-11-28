#pragma comment(linker, "/STACK:64000000")
#include <iostream>
#include <string.h>
#include <cstdio>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <map>
#include <deque>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <sstream>
#include <cassert>
#include <ctime>

using namespace std;

typedef long long li;
typedef long double ld;
typedef pair <int,int> pt;

#define mp make_pair 
#define fs first
#define sc second
#define pb push_back
#define pf push_front
#define all(a) a.begin(),a.end()
#define sz(a) (int)a.size()
#define len(a) (int)a.length()
#define forn(i, n) for (int i = 0; i < (int)n; i++)
#define forn1(i, n) for (int i = 1; i <= (int)n; i++)
#define ford(i, n) for (int i = (int)n-1; i >= 0; i--)
#define fore(i, l, r) for (int i = (int)l; i <= (int)r; i++)               
#define sqr(x) ((x) * (x))
#define abs(x) ((x) < 0 ? -(x) : (x))
                                                                       
const int INF = (int)1E8;
const ld EPS = 1E-9;
const ld PI = 3.1415926535897932384626433832795;
const int NMAX = 1010;   
  
int r, k, n, a[NMAX], to[NMAX];
li d[NMAX];

void solve (int from){

	li ans = 0;
	int pos = from;
	int cnt = 0;
	while (1){
		
		if (ans + a[pos] > k){
			d[from] = ans;
			to[from] = pos;
			break;
        	}
		
		ans += a[pos];
		pos++;
		if (pos == n)
			pos = 0;
		cnt++;
		if (cnt == n){
			d[from] = ans;
			to[from] = from;
			break;
		}

	}

}
 
int main (){

	freopen ("input.txt","rt",stdin);
	freopen ("output.txt","wt",stdout);

	int tests;
	scanf ("%d", &tests);
	        
	forn (test, tests){

		printf ("Case #%d: ", test + 1);

		scanf ("%d%d%d", &r, &k, &n);
		forn (i, n)
			scanf ("%d", &a[i]);
		
		forn (i, n)
			solve (i);	

		li ans = 0;
		int pos = 0;
		forn (i, r){
			ans += d[pos];
			pos = to[pos];
		}

		printf ("%I64d\n", ans);

	}      

		        
	return 0;
}
