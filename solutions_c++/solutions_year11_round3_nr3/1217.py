////////////////////////////////////////////////////////////////////
// Written by Hisaki Niikura
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
#include <deque>
#include <stack>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <fstream>

#define	numberof(a)	(sizeof(a) / sizeof(a[0]))
#define	INF		(1000000)
#define Rep(i,n) for(int i = 0; i < (n); i++ )

//clear memory
#define CLR(a) memset((a), 0 ,sizeof(a))

//debug
#define dump(x)  cout << #x << " = " << (x) << endl;
#define debug(x) cout << #x << " = " << (x) << " (L" << __LINE__ << ")" << " " << __FILE__ << endl;
#define	show(x)	 copy( (x).begin(), (x).end(), ostream_iterator<int>(cout, ",") );

using namespace std;

typedef vector< vector<int> > mat;
typedef pair<int, int> P;
typedef long long ll;

//constant
//--------------------------------------------
const double EPS = 1e-10;
const double PI  = acos(-1.0);

ll gcd( ll x, ll y )
{
	// x <= y
	if( x > y ){
		ll tmp = x;
		x = y;
		y = tmp;
	}

	if( x == 0 ) return y;
	return gcd( y % x, x );
}

ll lcm( ll x, ll y )
{
	return x * y / gcd(x, y);
}

class GCJ
{
public:
	ll solve( ll N, ll L, ll H, vector<ll> other_notes )
	{
		ll ret = -1;

		sort( other_notes.begin(), other_notes.end() );

		for( ll i = L; i <= H; i++ ){
			int cnt = 0;
			for( ll j = 0; j < N; j++ ){
				ll harmony = lcm(i, other_notes[j]);
				if( harmony == i || harmony == other_notes[j] ){
					cnt++;
				}
			}
			if( cnt == N ) return i;
		}

		return ret;
	}
};

int main()
{
	GCJ obj;
	vector< ll > ans;
	int T = 0;

	cin >> T;

	for( int i = 0; i < T; i++ ){
		ll L = 0;
		ll H = 0;
		ll N = 0;

		cin >> N >> L >> H;

		vector<ll> other_notes(N);

		Rep(j, N){
			cin >> other_notes[j];
		}

		ans.push_back( obj.solve(N, L, H, other_notes) );
	}

	// output
	for( int i = 0; i < T; i++ ){
		if( ans[i] == - 1 ){
			cout << "Case #" << i + 1 << ": NO" << endl;
		}
		else{
			cout << "Case #" << i + 1 << ": " << ans[i] << endl;
		}
	}

	// wait
	cin >> T;

	return 0;
}


