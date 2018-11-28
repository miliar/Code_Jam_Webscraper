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
               
int a[NMAX][NMAX], n, b[NMAX][NMAX];  

 
int main (){

	freopen ("input.txt","rt",stdin);
	freopen ("output.txt","wt",stdout);

	int tests;
	scanf ("%d", &tests);
	        
	forn (test, tests){

		printf ("Case #%d: ", test + 1);

		cin >> n;
		memset (a, 0, sizeof(a));

		forn (i, n){
			
			int x, y, xx, yy;
			cin >> x >> y >> xx >> yy;
			x--; y--;
			xx--; yy--;

			fore (xxx, x, xx)
				fore (yyy, y, yy)
					a[xxx][yyy] = 1;

		}		

		int ans = 0;

		while (1){

		bool has = false;
		forn (i, 100)
			forn (j, 100)
				if (a[i][j] == 1)
					has = true;

		if (!has)
			break;

		ans++;
		
		memset (b, 0, sizeof(b));
		forn (i, 100)
			forn (j, 100){

				if (a[i][j] == 1){

					bool f = true;
					if (i - 1 >= 0 && a[i - 1][j] == 1)
						f = false;
					if (j - 1 >= 0 && a[i][j - 1] == 1)
						f = false;

					if (!f)
						b[i][j] = 1;

				}

				if (a[i][j] == 0 && i - 1 >= 0 && j - 1 >= 0 && a[i - 1][j] == 1 && a[i][j - 1] == 1)
					b[i][j] = 1;

			}

		forn (i, 100)
			forn (j, 100)
				a[i][j] = b[i][j];

		}

		cout << ans << endl;;


	
	}      

		        
	return 0;
}
