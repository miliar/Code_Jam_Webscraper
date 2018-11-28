#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cstdlib>
#include <cstring>
#include <functional>
#include <algorithm>
#include <cmath>
#include <sstream>
using namespace std;

#define vi vector<int>
#define pb push_back
#define forn(i,a,b) for(int i = (int)a; i < (int)b; i++)
#define forn1(i,a,b) for(int i = (int)a; i >= (int)b; i--)
#define sz(a) (int)(a).size()
#define all(c) c.begin(), c.end()

string s[100];
int a[100][100],b[100][100],c[100][100];
// BEGIN CUT HERE 
int main()
{
	freopen("E:\\3.txt","rt",stdin);
	freopen("E:\\4.txt","wt",stdout);	
	int T;
	int n,k;
	cin >> T;
	forn(numt,1,T+1)
	{
		cin >> n >> k;
		forn(i,0,n) cin >> s[i];
		forn(i,0,n) forn(j,0,n) { a[i][j] = 0; b[i][j] = 0; c[i][j] = 0; }		
		forn(i,0,n) forn(j,0,n) 
		{
			if ( s[i][j] == '.' ) a[j][n-1-i] = 0;
			if ( s[i][j] == 'R' ) a[j][n-1-i] = 1;
			if ( s[i][j] == 'B' ) a[j][n-1-i] = 2;
		}
		forn(i,0,n)
		{
			int lev = 0;
			for(int j = n - 1; j >= 0; j--)
			{
				if ( a[j][i] > 0 ) { b[j][i] = lev; lev++; }
			}
		}
		forn(i,0,n)
		{
			for(int j = n - 1; j >= 0; j--) if ( a[j][i] > 0 ) 
				c[n - 1- b[j][i] ] [ i ] = a[j][i];
		}
		forn(i,0,n)
		{			
			forn(j,0,n) 
			{
				if ( c[i][j] == 0 ) s[i][j] = '.';
				if ( c[i][j] == 1 ) s[i][j] = 'R';
				if ( c[i][j] == 2 ) s[i][j] = 'B';
		//		cout << s[i][j];
			}
		//	cout << endl;
		}
		//cout << endl;
		int res = 0;
		forn(i,0,n) forn(j,0,n)
		{
			int f;
			f = 1;
			if ( i + k - 1 >= n || j+ k - 1 >= n ) f = 0;
			else forn(d,1,k) if ( c[i+d][j+d] != c[i][j] ) { f = 0; break; }
			if ( f == 1 ) res |= c[i][j];
			f = 1;
			if ( i + k - 1 >= n  ) f = 0;
			else forn(d,1,k) if ( c[i+d][j] != c[i][j] ) { f = 0; break; }
			if ( f == 1 ) res |= c[i][j];
			f = 1;
			if ( i + k - 1 >= n || j - k + 1 < 0 ) f = 0;
			else forn(d,1,k) if ( c[i+d][j-d] != c[i][j] ) { f = 0; break; }
			if ( f == 1 ) res |= c[i][j];
			f = 1;
			if ( j + k - 1 >= n ) f = 0;
			else forn(d,1,k) if ( c[i][j+d] != c[i][j] ) { f = 0; break; }
			if ( f == 1 ) res |= c[i][j];			
		}
		if ( res == 3 ) cout <<"Case #" << numt << ": " << "Both";
		if ( res == 2 ) cout <<"Case #" << numt << ": " << "Blue";
		if ( res == 1 ) cout <<"Case #" << numt << ": " << "Red";
		if ( res == 0 ) cout <<"Case #" << numt << ": " << "Neither";
		cout << endl;
	}
} 
// END CUT HERE
