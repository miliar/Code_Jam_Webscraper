#include <cstdio>
#include <memory.h>
#include <cctype>

//#ifndef _DEBUG
//static const int MAX = 8;
//static const int BASE = 100000000;
//static const int BASELEN = 8;
//#else
static const int MAX = 20;
static const int BASE = 1000;
static const int BASELEN = 3;
//#endif

struct sLong
{
	long A[ MAX ];
	
	sLong( int a = 0 )
	{
		for( int i = 0; i < MAX; ++i )
		{
			A[ i ] = a % BASE;
			a /= BASE;
		}
	}
	sLong &operator +=( const sLong &x )
	{
		int r = 0;
		for( int i = 0; i < MAX; ++i )
		{
			r += A[ i ] + x.A[ i ];
			A[ i ] = r % BASE;
			r /= BASE;
		}
		return *this;
	}
	sLong &operator -=( const sLong &x )
	{
		int r = 0;
		for( int i = 0; i < MAX; ++i )
		{
			r += A[ i ] - x.A[ i ];
			A[ i ] = ( r + BASE ) % BASE;
			r = ( r - A[ i ] ) / BASE;
		}
		return *this;
	}
	sLong &operator %=( const sLong &x )
	{
		return *this = *this % x;
	}

	sLong operator *( const sLong &x ) const
	{
		sLong res;
		long long r = 0;
		for( int i = 0; i < MAX; ++i )
		{
			for( int j = 0; j <= i; ++j )
			{
				r += ( long long )A[ j ] * x.A[ i - j ];
			}
			res.A[ i ] = ( long )( r % BASE );
			r /= BASE;
		}
		return res;
	}
	sLong operator /( const sLong &x ) const
	{
		return Div( *this, x );
	}
	sLong operator %( const sLong &x ) const
	{
		sLong d = Div( *this, x );
		return *this - d * x;
	}

	sLong operator +=( int x )
	{
		int r = x;
		for( int i = 0; r != 0 && i < MAX; ++i )
		{
			r += A[ i ];
			A[ i ] = r % BASE;
			r /= BASE;
		}
		return *this;
	}
	sLong operator -=( int x )
	{
		int r = -x;
		for( int i = 0; r != 0 && i < MAX; ++i )
		{
			r += A[ i ];
			A[ i ] = ( r % BASE + BASE ) % BASE;
			r = ( r - A[ i ] ) / BASE;
		}
		return *this;
	}
	sLong operator *=( int x )
	{
		long long r = 0;
		for( int i = 0; i < MAX; ++i )
		{
			r += ( long long )A[ i ] * x;
			A[ i ] = ( long )( r % BASE ); 
			r /= BASE;
		}
		return *this;
	}
	sLong operator /=( int x )
	{
		long long r = 0;
		for( int i = MAX - 1; i >= 0; --i )
		{
			r = ( r * BASE ) + A[ i ];
			A[ i ] = ( long )( r / x );
			r %= x;
		}
		return *this;
	}

	sLong operator -() const
	{
		return 0 - *this;
	}

private:
	bool IsNegative() const
	{
		return A[ MAX - 1 ] >= BASE / 2;
	}
public:
	bool operator <( const sLong &x ) const
	{
		return ( *this - x ).IsNegative();
	}
	bool operator >( const sLong &x ) const 
	{
		return ( x - *this ).IsNegative();
	}
	bool operator <=( const sLong &x ) const 
	{
		return !operator >( x );
	}
	bool operator >=( const sLong &x ) const
	{
		return !operator <( x );
	}
	bool operator ==( const sLong &x ) const
	{
		return operator <=( x ) && operator >=( x );
	}
	bool operator !=( const sLong &x ) const 
	{
		return !operator ==( x );
	}

	void Input()
	{
		int c;
		memset( A, 0, sizeof( A ) );
		while( isdigit( c = getchar() ) )
		{
			*this *= 10;
			*this += c - '0';
		}
		ungetc( c, stdin );
	}
	void Output()
	{
		int i;
		if( IsNegative() )
		{
			putchar( '-' );
			( -*this ).Output();
			return;
		}
		for( i = MAX - 1; i > 0; --i )
		{
			if( A[ i ] != 0 )
				break;
		}
		printf( "%d", A[ i-- ] );
		for( ; i >= 0; --i )
		{
			printf( "%0*d", BASELEN, A[ i ] );
		}
	}

	friend sLong Div( const sLong &x, const sLong &y );
	friend sLong operator +( sLong x, const sLong &y );
	friend sLong operator -( sLong x, const sLong &y );
	friend sLong operator *( sLong x, int y );
	friend sLong operator /( sLong x, int y );
};

sLong operator +( sLong x, const sLong &y )
{
	return x += y;
}

sLong operator -( sLong x, const sLong &y )
{
	return x -= y;
}

sLong Div( const sLong &x, const sLong &y )
{
	sLong left = 0, right = 1;
	sLong leftres = 0, rightres = y;
	while( rightres <= x )
	{
		right *= 2;
		rightres *= 2;
	}

	while( right - left > 1 )
	{
		sLong middle = ( right + left ) / 2;
		sLong middleres = ( rightres + leftres ) / 2;

		if( middleres <= x )
		{
			left = middle;
			leftres = middleres;
		}
		else
		{
			right = middle;
			rightres = middleres;
		}
	}
	return left;
}

sLong operator *( sLong x, int y )
{
	return x *= y;
}

sLong operator /( sLong x, int y )
{
	return x /= y;
}

static const int MAXN = 1011;

int N;
sLong T[ MAXN ];

void Read()
{
	int i;
	scanf( "%d", &N );
	for( i = 0; i < N; ++i )
	{
		scanf( " " );
		T[ i ].Input();
	}
}

sLong GCD( sLong x, sLong y )
{
	while( true )
	{
		if( x == 0 )
			return y;
		y %= x;
		if( y == 0 )
			return x;
		x %= y;
	}
}

sLong Result;

void Work()
{
	int i;
	sLong gcd = 0;
	for( i = 1; i < N; ++i )
	{
		if( T[ i ] > T[ i - 1 ] )
			gcd = GCD( gcd, T[ i ] - T[ i - 1 ] );
		else
			gcd = GCD( gcd, T[ i - 1 ] - T[ i ] );
//#ifdef _DEBUG
//		( T[ i ] - T[ i - 1 ] ).Output();
//		puts( "" );
//		gcd.Output();
//		puts( "" );
//#endif
	}

	Result = gcd - ( ( T[ 0 ] - 1 ) % gcd + 1 );
}

void Write( int test )
{
	printf( "Case #%d: ", test );
	Result.Output();
	puts( "" );
}

int main()
{
	int i, t;
	scanf( "%d", &t );
	for( i = 0; i < t; ++i )
	{
		Read();
		Work();
		Write( i + 1 );
	}
	return 0;
}
