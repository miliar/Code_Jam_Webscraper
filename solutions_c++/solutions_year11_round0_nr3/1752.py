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

class GCJ
{
public:
	ll solve( int N, vector<ll> & values )
	{
		ll ret = 0;
		ll sum_binary = 0;
		for( int i = 0; i < N; i++ ){
			sum_binary ^= values[i];
		}
		if( sum_binary != 0 ) return -1;// This case "No"

		// sort
		sort( values.begin(), values.end() );

		for( int i = N - 1; i >= 1; i-- ){
			ret += values[i];
		}
		return ret;
	}
};

int main()
{
	GCJ obj;
	vector<ll> ans;
	int T = 0;

	cin >> T;

	for( int t = 0; t < T; t++ ){
		int N = 0;

		cin >> N;
		vector<ll> values(N);

		for( int i = 0; i < N; i++ ){
			int tmp = 0;
			cin >> tmp;
			values[i] = tmp;
		}
		ans.push_back( obj.solve(N, values) );
	}

	// output
	for( int i = 0; i < T; i++ ){
		ll answer = ans[i];
		if( answer == -1 ){
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

