#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>

using namespace std;

bool able( int m, int n )
{
	string sm, sn;
	stringstream ssm, ssn;

	ssm << m;
	sm = ssm.str();

	ssn << n;
	sn = ssn.str();

	for ( unsigned i = 0; i < sm.length(); i++ )
	{
		char buf = sm[0];
		sm.erase( sm.begin() );
		sm += buf;

		if ( sm == sn )
		{
			return true;
		}
	}

	return false;
}

int main()
{
	int t;

	cin >> t;

	for ( int i = 0; i < t; i++ )
	{
		int a, b, count = 0;

		cin >> a >> b;

		for ( int n = a; n <= b; n++ )
		{
			for ( int m = n + 1; m <= b; m++ )
			{
				if ( able( m, n ) )
				{
					count++;
				}
			}
		}

		cout << "Case #" << i + 1 << ": " << count << endl;
	}

	return 0;
}