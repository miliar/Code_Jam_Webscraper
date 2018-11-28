#include <stdio.h>
#include <memory.h>
#include "vector"
#include "iostream"
#include <algorithm>
#include <string>

using namespace std;


int main()
{
	freopen("d://in.txt", "r", stdin);
	freopen("d://out.txt", "w", stdout);
	
	int n;
	cin >> n;
	for ( int in=0; in<n; ++in )
	{
		string str;
		cin >> str;
		int pos = str.size()-1;
		for ( ; pos-1>=0; --pos )
		{
			if ( str[pos-1] < str[pos] )
			{
				char m = '9'+1;
				int c = -1;
				for ( int i=str.size(); i>pos-1; --i )
				{
					if ( str[i] < m && str[i] > str[pos-1] )
					{
						c = i;
						m = str[i];
					}					
				}
				vector<char> vec;
				vec.push_back( str[pos-1] );
				str[pos-1] = str[c];
				for ( int i=pos; i<str.size(); ++i )
				{
					if ( i != c )
					{
						vec.push_back( str[i] );
					}
				}
				sort( vec.begin(), vec.end() );
				for ( int i=0; i<vec.size(); ++i )
				{
					str[pos+i] = vec[i];
				}
				break;
			}
		}
		if ( pos-1 < 0 )
		{
			char m = '9' + 1;
			int c = -1;
			for ( int i=0; i<str.size(); ++i )
			{
				if ( str[i] < m && str[i] != '0' )
				{
					m = str[i];
					c = i;
				}
			}
			vector<char> vec;
			for ( int i=0; i<str.size(); ++i )
			{
				if ( i != c )
				{
					vec.push_back( str[i] );
				}
			}
			vec.push_back( '0' );
			sort( vec.begin(), vec.end() );
			str = m;
			for ( int i=0; i<vec.size(); ++i )
			{
				str += vec[i];
			}
		}
	    cout << "Case #" << in+1 << ": " << str << endl;
	}


	return 0;
}