#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int n;

int main()
{
	int T; cin >> T;
	for (int C = 1; C <= T; ++C)
	{
		cin >> n;
		vector< pair<char,int> > a;
		char c; int d;
		for (int i = 0; i < n; ++i)
		{
			cin >> c >> d;
			a.push_back( make_pair(c,d) );
		}
	
		pair<int,int> p1(1,0), p2(1,0);
		int ret = 0;
		for ( int i = 0; i < n; ++i )
		{
			if (a[i].first == 'O')
			{
				int k = abs( 1.0*p1.first - a[i].second );
				p1.second = max( p1.second+k+1, p2.second+1 );
				p1.first = a[i].second;
			}
			else
			{
				int k = abs( 1.0*p2.first - a[i].second );
				p2.second = max( p2.second+k+1, p1.second+1 );
				p2.first = a[i].second;
			}
		}
	
		cout << "Case #" << C << ": " << max(p1.second, p2.second) << endl;
	}
}
