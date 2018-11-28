#include <stdio.h>
#include <memory.h>
#include <vector>

using namespace std;

bool matr1[ 103 ][ 103 ];
bool matr2[ 103 ][ 103 ];
int answer;
void read()
{
	answer = 0;
	memset( matr1 , 0 , sizeof( matr1 ) );
	memset( matr2 , 0 , sizeof( matr2 ) );
	int r;
	scanf( "%d" , &r );
	for(int i = 0;i < r;++i)
	{
		int x1,x2,y1,y2;
		scanf( "%d%d%d%d" , &x1 , &y1 , &x2 , &y2 );
		for(int j = x1 - 1;j < x2;++j)
			for(int k = y1 - 1;k < y2;++k)
				matr1[ k ][ j ] = true;
	}
}

bool done()
{
	for(int i = 103;i >= 0;--i)
		for(int j = 103;j >= 0;--j)
			if( matr1[ i ][ j ] ) return false;
	return true;
}
void step()
{
	memset( matr2 , 0 , sizeof( matr2 ) );
	for(int i = 0;i < 103;++i)
		for(int j = 0;j < 103;++j)
		{
			int how = 0;
			if( i && matr1[ i - 1 ][ j ] ) how++; 
			if( j && matr1[ i ][ j - 1 ] ) how++; 
			if( how == 0 )
				matr2[ i ][ j ] = false;
			if( matr1[ i ][ j ] && how )
				matr2[ i ][ j ] = true;
			if( how == 2 )
				matr2[ i ][ j ] = true;
		}
	for(int i = 0;i < 103;++i)
		for(int j = 0;j < 103;++j)
			matr1[ i ][ j ] = matr2[ i ][ j ];
}

void work()
{
	
	while( !done() )
	{
		answer++;
		step();
	}
}

int main()
{
	freopen( "C-small-attempt1.in" , "r" , stdin );
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