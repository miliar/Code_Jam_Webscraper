#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <set>
#include <map>
#include <queue>
#include <climits>
#include <cmath>
#include <cstdlib>
#include <sstream>
#include <utility>
#include <complex>
#include <valarray>
#include <deque>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;

#define RI( i, o ) for(typeof(o.begin()) i= (o).begin(); i!=(o).end(); ++i)
#define RP3( x, y, z ) RP( i, 0, x ) RP( j, 0, y ) RP( k, 0, z )
#define RP( i, s, e ) for(typeof(s) i=(s); i<(e); ++i)
#define R( i, x ) RP(i,0,(x).size())
#define pB push_back


int main()
{
	int N;
	cin >> N;
	for(int cn=1; cn<=N; ++cn)
	{
		ll n,a=0;
		cin >> n;
		vector<ll> x(n),y(n);
		
		RP(i,0,n) cin >> x[i];
		RP(i,0,n) cin >> y[i];
		
		sort(x.begin(),x.end());
		sort(y.begin(),y.end());
		reverse(y.begin(),y.end());
		
		RP(i,0,n) a+=x[i]*y[i];
		
		cout << "Case #" << cn << ": " << a << endl;
	}
	return 0;
}
