#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>

using namespace std;

int main ()
{
	freopen("C-large.in","rt",stdin);
	freopen("C-large.out","wt",stdout);
	int t;
	cin >> t;

	for ( int tt = 1 ; tt <= t ; tt++)
	{
		int n;
		cin >> n;
		int sum = 0, mn = 1<<27, xoor = 0;
		for ( int i = 0 ; i < n ; i ++ )
		{
			int x;
			cin >> x;
			sum += x;
			mn = min (mn, x);
			xoor ^= x;
		}
		cout << "Case #"<<tt<<": ";
		if ( xoor )
			cout << "NO\n";
		else
			cout << sum - mn << endl;
	}
	return 0;
}
