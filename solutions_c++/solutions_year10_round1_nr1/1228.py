#include <iostream>
using namespace std;

void permute( char &a, char &b, char &c, char &d )
{
	char	tmp = a;
	a=b;
	b=c;
	c=d;
	d=tmp ;
}

void rotate( string	*grid, int n, int numRotate )
{
	char c;
	
	for( int r = 0 ; r < numRotate ; r++ )
	{
		for( int i = 0 ; i < n/2 ; i++ )
		{
			for( int j = 0 ; j < (n+1)/2 ; j++ )
			{
				permute( grid[ i ][ j ], grid[ n-1-j ][ i ], grid[ n-i-1 ][ n-j-1 ], grid[ j ][ n-i-1 ] ) ;
			}
		}
	}
}

void gravity( string	*grid, int n )
{
	for( int j = 0 ; j < n ; j++ )
	{
		for( int i = n-1 ; i >= 0 ; i-- )
		{
			int k = i ;
			while( k < n-1 && grid[ k ][ j ] != '.' && grid[ k+1 ][ j ] == '.' )
			{
				//cout << k << "\t" << j << "\t" << grid[ k ][ j ] << "\t" << grid[ k+1 ][ j ] << endl ;
				swap( grid[ k ][ j ], grid[ k+1 ][ j ] ) ;
				k++ ;
			}
		}
	}
}

int count( string const*const grid, int n, char ch )
{
	int	c = 0 ;
	
	// vertically
	for( int i = 0 ; i < n ; i++ )
	{
		int		p = 0 ;
		for( int j = 0 ; j < n ; j++ )
		{
			if( grid[ i ][ j ] == ch )
			{
				p+=1;
			}
			else
			{
				p=0;
			}
			
			c=max(c,p);
		}
	}
	// horizontally
	for( int j = 0 ; j < n ; j++ )
	{
		int		p = 0 ;
		for( int i = 0 ; i < n ; i++ )
		{
			if( grid[ i ][ j ] == ch )
			{
				p+=1;
			}
			else
			{
				p=0;
			}
			
			c=max(c,p);
		}
	}
	
	// diagonally
	for( int i = 0 ; i < n ; i++ )
	{
		int		p = 0 ;
		for( int k = 0 ; i+k<n ; k++ )
		{
			if( grid[ 0+k ][ i+k ] == ch )
			{
				p+=1;
			}
			else
			{
				p=0;
			}
			
			c=max(c,p);
		}
	}
	for( int i = 1 ; i < n ; i++ )
	{
		int		p = 0 ;
		for( int k = 0 ; i+k < n ; k++ )
		{
			if( grid[ i+k ][ 0+k ] == ch )
			{
				p+=1;
			}
			else
			{
				p=0;
			}
			
			c=max(c,p);
		}
	}
	
	
	//diagonally
	for( int i = 0 ; i < n ; i++ )
	{
		int		p = 0 ;
		for( int k = 0 ; i-k>=0 ; k++ )
		{
			if( grid[ i-k ][ 0+k ] == ch )
			{
				p+=1;
			}
			else
			{
				p=0;
			}
			
			c=max(c,p);
		}
	}
	for( int i = 1 ; i < n ; i++ )
	{
		int		p = 0 ;
		for( int k = 0 ; i+k<n ; k++ )
		{
			if( grid[ n-i-k ][ i+k ] == ch )
			{
				p+=1;
			}
			else
			{
				p=0;
			}
			
			c=max(c,p);
		}
	}
	
	return c ;
}

void print( string const*const grid, int n )
{
	for( int i = 0 ; i < n ; i++ )
	{
		cout << grid[ i ] << endl ;
	}
	cout << endl ;
}

void copyGrid( string const*const grid, string *buffer, int n )
{
	for( int i = 0 ; i < n ; i++ )
	{
		buffer[ i ] = grid[ i ] ;
	}
}

int main()
{
	string	grid[ 50 ] ;
	string	buffer[ 50 ] ;
	int		t = 0 ;
	int		n = 0 ;
	int		k = 0 ;
	int		lenR=0;
	int		lenB=0;
	
	cin >> t ;
	for( int casenum = 1 ; casenum <= t ; casenum++ )
	{
		cin >> n >> k ;
		lenR=0;
		lenB=0;
		
		for( int i = 0 ; i < n ; i++ )
		{
			cin >> grid[ i ] ;
		}
		
		copyGrid( grid, buffer, n ) ;
		rotate( buffer, n, 1 ) ;
		gravity( buffer, n ) ;
		lenR = max(lenR, count(buffer,n,'R') ) ;
		lenB = max(lenB, count(buffer,n,'B') ) ;
		
		cout << "Case #" << casenum << ": " ;
		if( lenR >= k )
		{
			if( lenB >= k )
			{
				cout << "Both" ;
			}
			else
			{
				cout << "Red" ;
			}
		}
		else
		{
			if( lenB >= k )
			{
				cout << "Blue" ;
			}
			else
			{
				cout << "Neither" ;
			}
		}
		cout << endl ;
	}
	
	return 0 ;
}
