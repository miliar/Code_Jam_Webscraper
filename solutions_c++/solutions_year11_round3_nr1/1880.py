#include<iostream>
#include<cstdlib>

using namespace std;

int main()
{
	int T = 0;
	cin>>T;
	for( int k = 1; k <= T; k++ )
	{
	
		cout<<"Case #"<<k<<":\n";
		bool cor = 1;
	
	
	int r = 0,c = 0;
	cin>>r;
	cin>>c;
	char tile[ r ][ c ];
	for( int i = 0; i < r; i++ )
	{
		for( int j = 0; j < c; j++ )
		cin>>tile[ i ][ j ];
	}

	for( int i = 0; i < r; i++ )
	{
		for( int j = 0; j < c; j++ )
		{
			if( tile[ i ][ j ] == '#' )
			{
				if( ( tile[ i ][ j+ 1 ] == '#' ) && ( tile[ i+1 ][ j ] == '#' ) && ( tile[ i+ 1][ j+ 1] == '#') )
				{
					tile[ i ][ j ] = '/';
					tile[ i ][ j+1 ] = '\\';
					tile[ i+1 ][ j ] = '\\';
					tile[ i+1 ][ j+1 ] ='/';
				}
				else{
				cor = 0;
				}
			}
		}
	}
	
	if( cor == 0 )
	{
		cout<<"Impossible\n";
	}
	else{
	for( int i = 0; i < r; i++ )
	{
		for( int j = 0; j < c; j++ )
		cout<<tile[ i ][ j ];
		cout<<endl;
	}
	}
	
	}
	
	
	return 0;
}
