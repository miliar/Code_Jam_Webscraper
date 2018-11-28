#include <stdio.h>
#include <memory.h>
#include <vector>

using namespace std;
int mass[ 2000 ];
int matches[ 1000 ][ 15 ];
int p;
int P;
int d;
int answer;
void read()
{
	scanf( "%d" , &p );
	P = p;
	p = 1 << p;
	for(int i = 0;i < p;++i)
		scanf( "%d" , mass + i );
	int s = p / 2;
	d = 0;
	while( s )
	{
		for(int i = 0;i < s;++i)
			scanf( "%d" , matches[ d ] + i );
		d++;
		s /= 2;
	}
}

bool test( int start , int length )
{
	for(int i = start;i < start + length;++i)
		if( mass[ i ] != P )
			return true;
	return false;
}
void doit( int start , int length )
{
	for(int i = start;i < start + length;++i)
		if( mass[ i ] != P ) mass[ i ]++;
}
void work()
{
	answer = 0;
	int width = p;
	for(int i = d - 1;i >= 0;--i)
	{
		for(int j = 0;j < p;j += width)
		{
			if( test( j , width ) ) { doit( j , width ); answer++; }
		}
		width /= 2;
	}
}

int main()
{
	freopen( "B-small-attempt0.in" , "r" , stdin );
	freopen( "out" , "w" , stdout );
	int t;
	scanf( "%d" , &t );
	for(int test = 1;test <= t;++test)
	{
		read();
		work();
		printf( "Case #%d: %d\n" , test , answer );
	}
	return 0;
}

/*
int matr[ 200 ][ 200 ];
vector<int> matr2[ 200 ];
vector<int> matr3[ 200 ];

int n , answer , k;

-1 -1  1 -1 -1				
-1  1 -1  2 -1				
 1 -1  1 -1  1			
-1  2 -1  1 -1							
-1 -1  1 -1 -1				

void read()
{
	int c = 0;
	scanf( "%d" , &k );
	for(int i = 0;i < k;++i)
	{
		for(int j = 0;j < i + 1;++j)
			scanf( "%d" , &matr[ c ][ j ] );
		c++;
	}
	for(int i = k - 2;i >= 0;--i)
	{
		for(int j = 0;j < i + 1;++j)
			scanf( "%d" , &matr[ c ][ j ] );
		c++;
	}
	c = 0;
	for(int i = 0;i < k;++i)
	{
		for(int j = 0;j < k - i - 1;++j)
			matr2[ c ].push_back( -1 );
		for(int j = 0;j < i + 1;++j)
		{
			if( j )
				matr2[ c ].push_back( -1 );
			matr2[ c ].push_back( matr[ c ][ j ] );
		}
		for(int j = 0;j < k - i - 1;++j)
			matr2[ c ].push_back( -1 );
		c++;
	}
	for(int i = k - 2;i >= 0;++i)
	{
		for(int j = 0;j < k - i - 1;++j)
			matr2[ c ].push_back( -1 );
		for(int j = 0;j < i + 1;++j)
		{
			if( j )
				matr2[ c ].push_back( -1 );
			matr2[ c ].push_back( matr[ c ][ j ] );
		}
		for(int j = 0;j < k - i - 1;++j)
			matr2[ c ].push_back( -1 );
		c++;
	}
	for(int i = 0;i < 2 * k - 1;++i)
	{
		for(int j = 2 * k - 2;j >= 0;--j)
			matr3[ i ].push_back( matr2[ j ][ i ] );
	}
}
void work()
{
	int add1 = 0;
	int add2 = 0;
	int c = 0;
	int j;
	for(int i = 0;i < k;++i)
	{
		for(j = 0;j < i + 1;++j)
		{
			bool have = true;
			for(int k = j,s = 0;k <= i;++k,++s)
				if( matr[ c ][ k ] != matr[ c ][ i - s ] )
				{
					have = false;
					break;
				}
			if( have ) break;
		}
		if( add1 < j ) add1 = j;
		c++;
	}
	for(int i = k - 2;i >= 0;--i)
	{
		for(j = 0;j < i + 1;++j)
		{
			bool have = true;
			for(int k = j,s = 0;k <= i;++k,++s)
				if( matr[ c ][ k ] != matr[ c ][ i - s ] )
				{
					have = false;
					break;
				}
			if( have ) break;
		}
		if( add1 < j ) add1 = j;
		c++;
	}

}


int main()
{
	//freopen( "C-large.in"  , "r" , stdin  );
	//freopen( "C-large.out" , "w" , stdout );
	int t;
	scanf( "%d" , &t );
	for(int test = 1;test <= t;++test)
	{
		read();
		work();
		printf( "Case %d:%d\n" , test , answer );
	}

	return 0;
}*/