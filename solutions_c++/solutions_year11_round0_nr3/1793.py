
#include <iostream>

#include <vector>
#include <map>

#include <algorithm>

using namespace std;

int n;
vector<int> pile;

int main()
{
	cin >> n;

	for( int i=0; i<n; ++i )
	{
		int m;
		cin >> m;

		int all = 0;
		int sum = 0;

		pile = vector<int>( m, 0 );
		for( int j=0; j<m; ++j ) { cin >> pile[j]; all^=pile[j]; sum+=pile[j]; };

		if ( all == 0 )
		{
			int ret = -1;
			sort( pile.begin(), pile.end() );
			ret = sum-pile[0];
			cout << "Case #" << (i+1) << ": " << ret << endl;
		}
		else
			cout << "Case #" << (i+1) << ": " << "NO" << endl;
	}

	return 0;
}

