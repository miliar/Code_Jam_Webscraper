
#include <iostream>

#include <vector>
#include <string>
#include <map>

#include <algorithm>

using namespace std;

int n;


int main()
{
	cin >> n;

	for( int i=0; i<n; ++i )
	{
		int ret = 0;
		int c, d, n;
		vector< string > oppos;
		map< string, string > comb;
		string s;
		vector< string > lis;

		cin >> c;
		for( int j=0; j<c; ++j )
		{
			string temp, label, to;
			cin >> temp;
			label = temp.substr( 0, 2 );
			to = temp.substr( 2, 1 );
			sort( label.begin(), label.end() );
			comb[label] = to;
		}

		cin >> d;
		oppos = vector<string>( d, string( "" ) );
		for( int j=0; j<d; ++j ) cin >> oppos[j];

		cin >> n;
		cin >> s;

		for( int j=0; j<s.size(); ++j )
		{
			lis.push_back( s.substr( j, 1 ) );
			if ( lis.size() < 2 )
				continue;
			string las = lis[lis.size()-2]+lis[lis.size()-1];
			sort( las.begin(), las.end() );
			if ( comb.find( las ) != comb.end() )
			{
				lis.pop_back(); lis.pop_back();
				lis.push_back( comb[las] );
			}
			else
			{
				for( int k=0; k<oppos.size(); ++k )
					if ( find( lis.begin(), lis.end(), oppos[k].substr(0,1) )!=lis.end() && find( lis.begin(), lis.end(), oppos[k].substr(1,1) )!=lis.end() )
					{
						lis.clear();
						break;
					}
			}
		}

		cout << "Case #" << (i+1) << ": [";
		for( int j=0; j<lis.size(); ++j )
		{
			if ( j>0 )
				cout << ", ";
			cout << lis[j];
		}
		cout << "]" << endl;
	}

	return 0;
}

