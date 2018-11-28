#include <iostream>
#include <string>

using namespace std;

int main()
{
	freopen( "A-small-attempt0.in", "rt", stdin );
	freopen( "output.txt", "wt", stdout );

	int T = 0;
	cin >> T;

	string garbage;
	getline( cin, garbage );

	for( int i = 0; i < T; i++ )
	{
		string G = "\0";
		getline( cin, G );

		string norm = "\0";
		for( int j = 0; j < G.size(); j++ )
		{
			char c = G[j];

			if( c == ' ' ) goto here;
			if( c == 'a' )
			{
				c = 'y';
				goto here;
			}
			if( c == 'b' )
			{
				c = 'h';
				goto here;
			}
			if( c == 'c' )
			{
				c = 'e';
				goto here;
			}
			if( c == 'd' )
			{
				c = 's';
				goto here;
			}
			if( c == 'e' )
			{
				c = 'o';
				goto here;
			}
			if( c == 'f' )
			{
				c = 'c';
				goto here;
			}
			if( c == 'g' )
			{
				c = 'v';
				goto here;
			}
			if( c == 'h' )
			{
				c = 'x';
				goto here;
			}
			if( c == 'i' )
			{
				c = 'd';
				goto here;
			}
			if( c == 'j' )
			{
				c = 'u';
				goto here;
			}
			if( c == 'k' )
			{
				c = 'i';
				goto here;
			}
			if( c == 'l' )
			{
				c = 'g';
				goto here;
			}
			if( c == 'm' )
			{
				c = 'l';
				goto here;
			}
			if( c == 'n' )
			{
				c = 'b';
				goto here;
			}
			if( c == 'o' )
			{
				c = 'k';
				goto here;
			}
			if( c == 'p' )
			{
				c = 'r';
				goto here;
			}
			if( c == 'q' )
			{
				c = 'z';
				goto here;
			}
			if( c == 'r' )
			{
				c = 't';
				goto here;
			}
			if( c == 's' ) 
			{
				c = 'n';
				goto here;
			}
			if( c == 't' ) 
			{
				c = 'w';
				goto here;
			}
			if( c == 'u' ) 
			{
				c = 'j';
				goto here;
			}
			if( c == 'v' ) 
			{
				c = 'p';
				goto here;
			}
			if( c == 'w' ) 
			{
				c = 'f';
				goto here;
			}
			if( c == 'x' )
			{
				c = 'm';
				goto here;
			}
			if( c == 'y' )
			{
				c = 'a';
				goto here;
			}
			if( c == 'z' )
			{
				c = 'q';
				goto here;
			}
here:
			norm.push_back( c );
		}

		cout << "Case #" << i+1 << ": " << norm << endl;
	}
	
	return 0;
}