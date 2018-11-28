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
const int NMAX = 60;   
                 
int n, k;
char s[NMAX][NMAX], str[NMAX][NMAX];

int calc (){

	int ans = 0;
	forn (i, n)
		forn (j, n){
			
			if (j - k + 1 >= 0){
				bool f = true;
				forn (h, k)
					if (s[i][j] != s[i][j - h])
						f = false;
				if (f){
					if (s[i][j] == 'R')
						ans |= 2;
					else if (s[i][j] == 'B')
						ans |= 1;
				}
			}
			if (i - k + 1 >= 0){
				bool f = true;
				forn (h, k)
					if (s[i][j] != s[i - h][j])
						f = false;
				if (f){
					if (s[i][j] == 'R')
						ans |= 2;
					else if (s[i][j] == 'B')
						ans |= 1;
				}
			}

			if (i - k + 1 >= 0 && j - k + 1 >= 0){
				bool f = true;
				forn (h, k)
					if (s[i][j] != s[i - h][j - h])
						f = false;
				if (f){
					if (s[i][j] == 'R')
						ans |= 2;
					else if (s[i][j] == 'B')
						ans |= 1;
				}
			}
			if (i - k + 1 >= 0 && j + k - 1 < n){
				bool f = true;
				forn (h, k)
					if (s[i][j] != s[i - h][j + h])
						f = false;
				if (f){
					if (s[i][j] == 'R')
						ans |= 2;
					else if (s[i][j] == 'B')
						ans |= 1;
				}
			}

						
		}

	return ans;

}

void Rotate (){

	int y = -1;
	int x = n - 1;
	forn (i, n){
		y++;
		x = n - 1;
		forn (j, n){
			str[i][j] = s[x][y];
			x--;
		}
	}

	forn (i, n)
		forn (j, n)
			s[i][j] = str[i][j];

}

void Gravity (){

	forn (i, n)
		forn (j, n)
			str[i][j] = '.';

	forn (j, n){
	
		int cur = n - 1;
		ford (i, n)
			if (s[i][j] != '.'){
				str[cur][j] = s[i][j];
				cur--;
			}

	}

	forn (i, n)
		forn (j, n)
			s[i][j] = str[i][j];

}

 
int main (){

	freopen ("input.txt","rt",stdin);
	freopen ("output.txt","wt",stdout);

	int tests;
	scanf ("%d", &tests);
	        
	forn (test, tests){

		printf ("Case #%d: ", test + 1);

		scanf ("%d%d", &n, &k);
		forn (i, n)
				forn (j, n)
					cin >> s[i][j];

		int ans = 0;
		ans |= calc ();

		Rotate ();
		Gravity ();

		ans |= calc ();

		if (ans == 3)
			puts ("Both");
		if (ans == 2)
			puts ("Red");		
                if (ans == 1)
			puts ("Blue");
		if (ans == 0)
			puts ("Neither");

	}      

		        
	return 0;
}
