#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <set>
#include <iomanip>
#include <utility>

#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <cstring>

using namespace std;

#define fori(i, n) for ( int i = 0; i < (n); ++i )
#define forr(i, a, b) for ( int i = (a); i <= (b); ++i )
#define tr(T, i) for (typeof(T.begin()) i = T.begin(); i != T.end(); ++i )
#define sz size()
#define all(x) (x).begin(),(x).end()
#define _sort(x) sort(all(x))
#define pb push_back

template<class T> string a2s(T x) { ostringstream o; o << x; return o.str(); }
template<class T> T s2a(string s) { istringstream i(s); T x; i >> x; return x; }

const double EPS = 1e-9;

int cmp(double x, double y = 0, double tol = EPS)
{
    return ( x <= y + tol ) ? ( x + tol < y ) ? -1 : 0 : 1;
}

int main()
{
	int T, C;

	cin >> T;

	for( C = 1; C <= T; C++ ) {
		string str;
		cin >> str;
		
		int f2 = 1;
		int n;
		int count = 1;
		map< char, int > cs;
		for(int i = 0; i < str.length(); i++) {
			if( cs.find(str[i]) == cs.end() ) {
				if( count == 2 && f2 ) {
					cs[str[i]] = 0;
					f2 = 0;
				}
				else
					cs[str[i]] = count++;
			}
		}

		long long int number = 0;
		long long int cbase = 1;
		long long int base = cs.size();
		if( base == 1 ) base++;
		for(int i = str.length()-1; i >= 0; i--) {
			long long int value = cs[str[i]];
			number += cbase*value;
			cbase *= base;
		}

		cout << "Case #" << C << ": " << number << endl;
	}
    return 0;
}
