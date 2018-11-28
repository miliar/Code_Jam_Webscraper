//============================================================================
// Name        : Dancing.cpp
// Author      : Shahab
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

// @BEGIN_OF_SOURCE_CODE

#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cctype>
#include <stack>
#include <queue>
#include <list>
#include <vector>
#include <map>
#include <sstream>
#include <cmath>
#include <bitset>
#include <utility>
#include <set>
#include <numeric>
#include <ctime>

#define Inf 2147483647
#define Pi acos(-1.0)
#define N 1000000
#define LL long long

const double EPS = 1e-9;
inline LL Power(int b, int p) { LL ret = 1; for ( int i = 1; i <= p; i++ ) ret *= b; return ret; }
const int dr [] = {-1, -1, 0, 1, 1, 1, 0, -1};
const int dc [] = {0, 1, 1, 1, 0, -1, -1, -1};

#define F(i, a, b) for( int i = (a); i < (b); i++ )
#define Fs(i, sz) for( size_t i = 0; i < sz.size (); i++ )
#define Fe(i, x) for(typeof (x.begin()) i = x.begin(); i != x.end (); i++)
#define Set(a, s) memset(a, s, sizeof (a))
#define max(a, b)  (a < b ? b : a)
#define min(a, b)  (a > b ? b : a)

using namespace std;


int main ()
{
	freopen ("in.txt", "r", stdin);
	freopen ("out.txt", "w", stdout);

	int testCase; scanf ("%d", &testCase);
	int cases = 0;

	while ( testCase-- ) {
		int n, s, p; scanf ("%d %d %d", &n, &s, &p);
		int cnt = 0;

		for ( int i = 0; i < n; i++ ) {
			int t; scanf ("%d", &t);

			int maxi = 0;
			int val [] = {28, 25, 22, 19, 16, 13, 10, 7, 4, 1};

			for ( int i = 0; i < 10; i++ ) {
				if ( t >= val [i] ) {
					maxi = 10 - i;
					break;
				}
			}

			if ( maxi >= p ) {
				cnt++;
			} else if (s) {
				maxi = 0;
				int nVal [] = {26, 23, 20, 17, 14, 11, 8, 5, 2};

				for ( int i = 0; i < 9; i++ ) {
					if ( t >= nVal [i] ) {
						maxi = 10 - i;
						break;
					}
				}

				if ( maxi >= p ) { cnt++; s--; }
			}
		}

		printf ("Case #%d: %d\n", ++cases, cnt);
	}
	return 0;
}

// @END_OF_SOURCE_CODE
