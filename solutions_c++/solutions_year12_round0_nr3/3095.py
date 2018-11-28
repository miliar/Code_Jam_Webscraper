////////////////////////////////////////////////////////////////////
// This source code is for Visual C++ 2010 Express
////////////////////////////////////////////////////////////////////
#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <sstream>
#include <iterator>
#include <stack>
#include <functional>
#include <iomanip>
#include <string>
#include <cstring>
#include <deque>
#include <math.h>
#include "UnionFind.h"

#define	numberof(a)	(sizeof(a) / sizeof(a[0]))
#define	INF		(1000000)
#define Rep(i,n) for(int i = 0; i < (n); i++ )

using namespace std;

typedef vector< vector<int> > mat;
typedef pair<int, int> P;
typedef long long ll;
struct Point{
	ll x;
	ll y;
	Point() {};
	Point( ll xx, ll yy ) : x(xx), y(yy) {};
};

//constant
//--------------------------------------------
const double EPS = 1e-10;
const double PI  = acos(-1.0);

string itoa( int n )
{
	string ret = "";

	while( n > 0 ){
		ret = static_cast<char>( (n % 10) + '0' ) + ret;
		n /= 10;
	}

	return ret;
}

ll solve( ll A, ll B )
{
	ll ret = 0;

	if( B < 10 ) return 0;

	for( ll n = A; n <= B; n++ ){
		for( ll m = n + 1; m <= B; m++ ){
			if( B < 100 ){
				// 2 keta
				int n0 = n / 10;
				int n1 = n % 10;
				int m0 = m / 10;
				int m1 = m % 10;
				if( n0 == m1 && n1 == m0 ) ret++;
			}
			else if( B < 1000 ){
				// 3 keta
				int n0 = n / 100;
				int n1 = n % 100 / 10;
				int n2 = n % 10;
				int m0 = m / 100;
				int m1 = m % 100 / 10;
				int m2 = m % 10;

				if( (n2 == m0 && n1 == m2 && n0 == m1) 
				||	(n1 == m0 && n2 == m1 && n0 == m2) ){
					ret++;
				}
			}
		}
	}

	return ret;
}

int main()
{
	int T = 0;
	ll A = 0;
	ll B = 0;
	vector< ll > ans;

	cin >> T;

	for( int t = 0; t < T; t++ ){
		cin >> A >> B;
		ans.push_back( solve(A, B) );
	}

	Rep(i, ans.size()){
		cout << "Case #" << i + 1 << ": " << ans[i] << endl;
	}

	// stop
	cin >> T;

	return 0;
}



