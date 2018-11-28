
#include <iostream>
#include <algorithm>
#include <climits>

using namespace std;

int main()
{
	int TC;
	cin >> TC;
	for ( int tc = 1; tc <= TC; ++tc ) {
		int n;
		cin >> n;
		int es = 0, ys = 0;
		int minv = INT_MAX;
		for ( int i = 0; i < n; ++i ) {
			int v;
			cin >> v;
			minv = min( minv, v );
			es += v;
			ys ^= v;
		}
		cout << "Case #" << tc << ": ";
		if ( ys != 0 )
			cout << "NO";
		else
			cout << es - minv;
		cout << endl;
	}
}
