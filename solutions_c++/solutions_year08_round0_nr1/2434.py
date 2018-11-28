#include <cstdio>
#include <climits>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <cctype>
#include <string>
#include <vector>
#include <sstream>
#include <iterator>
#include <numeric>
#include <cmath>
using namespace std;

vector< string > engines;
vector< string > queries;
vector< int > first;

int checkEngines ( int from )
{
	for ( int i = 0; i < engines.size(); i++ )
		for ( int j = from; j < queries.size(); j++ )
			if ( engines[i] == queries[j] && first[i] > j )
				first[i] = j;
}

int getPos ()
{
	int max = 0;
	for ( int i = 0; i < engines.size(); i++ )
		if ( max < first[i] )
			max  = first[i];
	return max;
}

int main ()
{

    freopen( "A-large.in",  "r", stdin ); 
    freopen( "A-large.out", "w", stdout );

	int n = 0;
	cin >> n;
	for ( int i = 1; i <= n; i++ )
	{
        engines.clear();
        queries.clear();
        first.clear();
        
        int num = 0;
	    cin >> num;
	    for ( int j = 0; j <= num; ++j )
	    {
		    string s;
		    getline( cin, s );
		    if ( j != 0 )
		      engines.push_back( s );
	    }
	    cin >> num;
	    for ( int j = 0; j <= num; ++j )
	    {
		    string s;
		    getline( cin, s );
		    if ( j != 0 )
  	          queries.push_back( s );
	    }
	
		for ( int j = 0; j < engines.size(); j++ )
  		  first.push_back( INT_MAX );
		
		int pos   = 0;
		int count = 0;
		while ( 1 )
		{
		  for ( int j = 0; j < first.size(); j++ )
		      first[j] = INT_MAX;
		
		  checkEngines( pos );
		  pos = getPos();
		  if ( pos >= queries.size() )
		    break;
		  count++;
		}

		cout << "Case #" << i << ": " << count << "\n";
	}

	exit(0);
}
