#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cassert>
#include <numeric>
#include <boost/foreach.hpp> // www.boost.org
#define foreach BOOST_FOREACH
using namespace std;
typedef long long LL;


void solve(int N, int M, int A)
{
	if( N*M < A ) {
		cout << "IMPOSSIBLE";
		return;
	}
	int x1 = (A/M)+(A%M?1:0);
	assert( x1 <= N );
	int y2 = M;
	int y1 = x1*y2 - A;
	assert( y1 <= M );
	int x2 = 1;
	assert( x1*y2-x2*y1 == A );
	cout << 0 << " " << 0 << " " << x1 << " " << y1 << " " << x2 << " " << y2;
}


int main()
{
	int nCase; cin >> nCase;
	for(int caseNo=1; caseNo<=nCase; ++caseNo)
	{
		int N, M, A;
		cin >> N >> M >> A;
		cout << "Case #" << caseNo << ": ";
		solve(N,M,A);
		cout << endl;
	}
}
