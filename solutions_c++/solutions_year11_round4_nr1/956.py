#include <iostream>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <queue>
#include <cstdlib>
#include <sstream>
#include <cstdio>
#include <algorithm>
#include <iomanip>
using namespace std;

bool comp( const pair< pair<double,double>, double > &a, const pair< pair<double,double>, double > &b )
{
	return a.second < b.second;
}

int main()
{
	int T; cin >> T;
	for (int C = 1; C <= T; ++C)
	{
		double x, r, s, t, n;
		cin >> x >> s >> r >> t >> n;
		vector< pair< pair<double,double>, double > > v(n);
		double sum = 0;
		for (int i = 0; i < n; ++i)
		{
			cin >> v[i].first.first >> v[i].first.second >> v[i].second;
			sum += v[i].second;
		}
		v.push_back( make_pair( make_pair(x,x), 0 ) );
		v.push_back( make_pair( make_pair(0,0), 0 ) );
		sort( v.begin(), v.end() );
		
		vector< pair< pair<double,double>, double > > vv;
		for (int i = 1; i < v.size(); ++i)
			vv.push_back( make_pair( make_pair( v[i-1].first.second, v[i].first.first ), 0 ) );
		v.insert( v.end(), vv.begin(), vv.end() );
		sort( v.begin(), v.end(), comp );
		
		double ret = 0, d, dist, a;
		for (int i = 0; i < v.size(); ++i)
		{
			d = (r + v[i].second) * t;
			dist = v[i].first.second-v[i].first.first;
			//cout << "f: " << d << " " << dist << endl;
			if ( d >= dist )
			{
				a = dist / (r+v[i].second);
				ret += a;
				t -= a;
			}
			else
			{
				a = t;
				ret += a;
				t = 0;
				
				a = (dist-d) / (s+v[i].second);
				ret += a;
			}
		}
		
		cout << "Case #" << C << ": " << fixed << setprecision(10) << ret << endl;
	}
}

