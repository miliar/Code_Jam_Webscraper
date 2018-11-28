
#include <iostream>

#include <vector>
#include <string>

using namespace std;

int tests;


int main()
{
	cin >> tests;

	for( int curTest=0; curTest<tests; ++curTest )
	{
		int n;
		cin >> n;
		vector<string> a( n, string() );
		for( int i=0; i<n; ++i )
			cin >> a[i];
		vector<double> wp, owp, oowp;
		vector<vector<double>> ewp;
		for( int i=0; i<n; ++i )
		{
			int w = 0, all = 0;
			for( int j=0; j<n; ++j )
				if ( a[i][j] == '1' || a[i][j] == '0' )
				{
					all++;
					w += ( a[i][j]=='1'?1:0 );
				}
			wp.push_back( 1.0*w/all );
			ewp.push_back( vector<double>() );
			for( int j=0; j<n; ++j )
			{
				if ( a[i][j] == '.' )
					ewp[i].push_back( 1.0*w/all );
				else if ( a[i][j] == '0' )
					ewp[i].push_back( (all==1?0.0:1.0*w/(all-1)) );
				else
					ewp[i].push_back( (all==1?0.0:1.0*(w-1)/(all-1)) );
			}
		}
		for( int i=0; i<n; ++i )
		{
			double w = 0;
			int all = 0;
			for( int j=0; j<n; ++j )
				if ( a[i][j] != '.' )
				{
					all++;
					w += ewp[j][i];
				}
			owp.push_back( 1.0*w/all );
		}
		for( int i=0; i<n; ++i )
		{
			double w = 0;
			int all = 0;
			for( int j=0; j<n; ++j )
				if ( a[i][j] != '.' )
				{
					all++;
					w += owp[j];
				}
			oowp.push_back( 1.0*w/all );
		}

		cout << "Case #" << (curTest+1) << ": " << endl;
		for( int i=0; i<n; ++i )
			cout << ( 0.25*wp[i]+0.5*owp[i]+0.25*oowp[i] ) << endl;
		cout << endl;
	}

	return 0;
}

