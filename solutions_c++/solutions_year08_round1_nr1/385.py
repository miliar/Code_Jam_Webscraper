#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <numeric>
using namespace std;



__int64 solve(vector<__int64>& x,  vector<__int64>& y)
{
	sort(x.begin(), x.end());
	sort(y.rbegin(), y.rend());
	return inner_product( x.begin(), x.end(), y.begin(), 0LL );
/* slow
	sort(y.begin(), y.end());
	__int64 minip = 0x7fffffffffffffffLL;
	do
	{
		__int64 ip = inner_product( x.begin(), x.end(), y.begin(), 0LL );
		minip = min(minip, ip);
	} while( next_permutation(y.begin(), y.end()) );
	return minip;
*/
}

int main()
{
	int nCase; cin >> nCase;
	for(int T=1; T<=nCase; ++T)
	{
		cout << "Case #" << T << ": ";
		int n; cin >> n;
		vector<__int64> x(n), y(n);
		for(int i=0; i!=n; ++i) cin >> x[i];
		for(int i=0; i!=n; ++i) cin >> y[i];
		cout << solve(x, y) << endl;
	}
}
