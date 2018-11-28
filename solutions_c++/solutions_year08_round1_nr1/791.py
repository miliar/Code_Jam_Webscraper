// CodeJam1.cpp: define el punto de entrada de la aplicación de consola.
//

#include "stdafx.h"

#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <list>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <complex>
#include <cstdio>
#include <cassert>
#include <cmath>

using namespace std;

#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;i++)
#define REP(i,n) FOR(i,0,(n)-1)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define sz size()
template<class T> inline int size(const T& c) { return c.sz; }
#define FORA(i,c) REP(i,size(c))

#define itype(c) __typeof((c).begin())
#define FORE(e,c) for(itype(c) e=(c).begin();e!=(c).end();e++)
#define pb push_back
#define X first
#define Y second
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define SORT(x) sort(all(x))
#define REVERSE(x) reverse(all(x))
#define CLEAR(x,c) memset(x,c,sizeof(x)) 

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
template<class T> string i2s(T x) { ostringstream o; o << x; return o.str(); }

#define pi acos(-1.)
#define eps 1e-9
#define inf numeric_limits<double>::infinity();

//ifstream fin("data.in");
//#define cin fin

typedef complex<double> point;
#define x real()
#define y imag()


int _tmain(int argc, _TCHAR* argv[])
{
	ifstream in(argv[1]);

	ofstream out(argv[2]);
	
	
	int t;

	in >> t;

	for ( int i = 0; i < t; i++ )
	{
		int n;
		in >> n;
		vector<int> v1(n);
		vector<int> v2(n);
		for ( int j = 0; j < n ; j++ )
		{
			in >> v1[j];
		}
		for ( int j = 0; j < n ; j++ )
		{
			in >> v2[j];
		}	

		sort(v1.begin(), v1.end());
		sort(v2.rbegin(), v2.rend());
		int res = 0;
		for ( int j = 0; j < n; j++ )
		{
			res += v1[j]*v2[j];
		}

		out << "Case #"<< i+1 << ": " << res << endl;
	}
	return 0;
}

