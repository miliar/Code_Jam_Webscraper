#include <iostream>
#include <cstdio>
#include <string>
#include <cstdlib>
#include <cctype>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

/*
int main()
{
	int n, s, q;
	string cad;
	
	getline( cin, cad );
	n = atoi( cad.c_str() );
	
	for ( int caso = 1; caso <= n; ++caso )
	{
		getline( cin, cad );
		s = atoi( cad.c_str() );
		
		vector < string > v;
		map < string, int > m;
		for ( int i = 0; i < s; ++i )
		{
			getline( cin, cad );
			v.push_back( cad );
			m[ cad ] = 0;
		}
		
		getline( cin, cad );
		q = atoi( cad.c_str() );
		
		for ( int i = 0; i < q; ++i )
		{
			getline( cin, cad );
			if ( m.find( cad ) != m.end() )
				m[ cad ]++;
		}
		
		for ( int i = 0; i < s; ++i )
			cout << v[i] << ' ' << m[v[i]] << endl;
		
		map < int, string > ord;
		for ( int i = 0; i < s; ++i )
			ord[ m[v[i]] ] = v[i];
		
		printf( "Case #%d: ", caso );
		
		if ( ord.begin()->first == 0 )
		{
			printf( "0\n" );
			continue;
		}
		
		printf( "1\n" );
	}

	return 0;
}
*/

int main()
{
	int n, s, q;
	string cad;
	
	getline( cin, cad );
	n = atoi( cad.c_str() );
	
	for ( int caso = 1; caso <= n; ++caso )
	{
		getline( cin, cad );
		s = atoi( cad.c_str() );
		
		vector < string > v;
		for ( int i = 0; i < s; ++i )
		{
			getline( cin, cad );
			v.push_back( cad );
		}
		
		getline( cin, cad );
		q = atoi( cad.c_str() );
		
		vector < string > w;
		for ( int i = 0; i < q; ++i )
		{
			getline( cin, cad );
			w.push_back( cad );
		}
		
		int posAct = 0;
		int sol = 0;
		while ( true )
		{
			int i, j, cont, maxi;

			//vector < int > cant( v.size(), 0 );
			
			for ( i = 0, maxi = -1; i < v.size(); ++i )
			{
				for ( j = posAct, cont = 0; j < w.size() && w[j] != v[i]; ++j )
					cont++;
				
				maxi = max( maxi, cont );
			}
			
			posAct += maxi;
			
			if ( posAct >= q || maxi <= 0 )
				break;
			
			sol++;
		}
		
		printf( "Case #%d: %d\n", caso, sol );
	}

	return 0;
}

