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
#include <sstream>
#include <ctime>
#include <cassert>

using namespace std;

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

#define mp make_pair 
#define fs first
#define sc second
#define pb push_back
#define pf push_front
#define all(a) a.begin(),a.end()
#define rz(a) resize(a)
#define sz(a) (int)a.size()
#define len(a) (int)a.length()
#define forn(i, n) for (int i = 0; i < (int)n; i++)
#define forn1(i, n) for (int i = 1; i <= (int)n; i++)
#define ford(i, n) for (int i = (int)n-1; i >= 0; i--)
#define fore(i, l, r) for (int i = (int)l; i <= (int)r; i++)               
#define abs(x) ((x) > 0 ? (x) : -(x))
#define sqr(x) ((x) * (x))
                                                   
const int INF = (int)1E8;
const ld EPS = 1E-9;
const ld PI = 3.1415926535897932384626433832795;
const int NMAX = 1010;   
        
                
li l, p, c;

int main (){
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);

	int tests;
	scanf ("%d", &tests);  
	forn (test, tests){
 		printf ("Case #%d: ", test + 1);

		cin >> l >> p >> c;
		
		li cur = l * c;
		vector <li> v;
		while (cur < p){
			v.pb (cur);
			cur *= c;
		}

		li ans = 0;
		li cnt = 1;
		while (cnt <= sz(v)){
			ans ++;
			cnt *= 2;
		}
		
                cout << ans;

 		printf ("\n");            
	}                                 

	

	return 0;
}
