#include "stdio.h"
#include <vector>
#include <set>
#include <strstream>
#include <string>
using namespace std;

char str[1000];


void create( istrstream& in, vector<string> &f, vector<double> &w, vector<int> &yes, vector<int>& no )
{
	int k = f.size();
	f.push_back( "" );
	w.push_back( 0 );
	yes.push_back( -1 );
	no.push_back( -1 );

	char c;
	double weight;
	
	in >> c;
	in >> weight;

	w[k] = weight;

	in >> c;
	if( c == ')' )
	{
		return;
	}
	else
	{
		in.putback( c );

		string feature;
		in >> feature;	
		f[k] = feature;

		yes[k] = f.size();
		create( in, f, w, yes, no );

		no[k] = f.size();
		create( in, f, w, yes, no );

		in >> c; // ')'
	}

	return;
}

int main()
{
	freopen( "test.in", "r", stdin );
	freopen( "test.out", "w", stdout );

	int n;
	scanf( "%d", &n );
	for( int cn = 1; cn <= n; ++cn )
	{
		int l;
		scanf( "%d", &l );
		getchar();
		string input;
		while( l-- )
		{
			gets( str );
			input += str;
		}
		vector<string> f;
		vector<double> w;
		vector<int> yes, no;
		istrstream in( input.c_str(), input.size() );
		create( in, f, w, yes, no );

		int m;
		scanf( "%d", &m );

		printf( "Case #%d:\n", cn );
		for( int i=0; i<m; ++i )
		{
			scanf( "%*s" );
			set<string> fs;

			int fn;
			scanf( "%d", &fn );
			for( int i=0; i<fn; ++i )
			{
				scanf( "%s", str );
				fs.insert( str );
			}

			double p = 1;
			int pos = 0;
			while( pos >= 0 )
			{
				p *= w[pos];
				if( f[pos] == "" )
					break;
				if( fs.find( f[pos] ) != fs.end() )
				{
					pos = yes[pos];
				}
				else
				{
					pos = no[pos];
				}
			}
			printf( "%lf\n", p );
		}
	}
	return 0;

}