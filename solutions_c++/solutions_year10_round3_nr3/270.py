#include <stdio.h>
#include <math.h>
#include <memory.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;
int m , n;
struct S
{
	int size , count;
};

int answers[ 100 ];
int num;

int matr[ 42 ][ 42 ];
int right[ 42 ][ 42 ];
int down[ 42 ][ 42 ];

void read()
{
	scanf( "%d%d" , &m , &n );
	int i , j;
	char str[ 100 ];
	for(i = 0;i < m;++i)
	{
		scanf( "%s" , str );
		for(j = 0;str[ j ];++j)
		{
			int a;
			if( str[ j ] >= '0' && str[ j ] <= '9' )	a = str[ j ] - '0';
			else										a = str[ j ] - 'A' + 10;
			matr[ i ][ j * 4 + 0 ] = a / 8;
			matr[ i ][ j * 4 + 1 ] = (a / 4) % 2;
			matr[ i ][ j * 4 + 2 ] = (a / 2) % 2;
			matr[ i ][ j * 4 + 3 ] = (a / 1) % 2;
		}

	}
}

bool tryFind(int a,int b,int c)
{
	if( matr[ a ][ b] == 2 ) return false;
	int i , j;
	for(i = a;i < a + c;++i)
	{
		int need = matr[ i ][ b ];
		for(j = b + 1;j < b + c;++j)
		{
			if( need + matr[ i ][ j ] != 1 ) return false;
			need = matr[ i ][ j ];
		}
	}
	for(i = b;i < b + c;++i)
	{
		int need = matr[ a ][ i ];
		for(j = a + 1;j < a + c;++j)
		{
			if( need + matr[ j ][ i ] != 1 ) return false;
			need = matr[ j ][ i ];
		}
	}
	return true;
}

void erase(int a,int b,int c)
{
	for(int i = 0;i < c;++i)
		for(int j = 0;j < c;++j)
			matr[ a + i ][ b + j ] = 2;
}

void work()
{
	num = 0;
	memset( answers , 0 , sizeof( answers ) );
	int i , j , size;
	int Max = min( m , n );
	for(size = Max;size >= 1;--size)
		for(i = 0;i + size - 1 < m;++i)
			for(j = 0;j + size - 1 < n;)
			{
				if( tryFind( i , j , size ) )
				{
					if( answers[ size ] == 0 )
						num++;
					answers[ size ]++;
					erase( i , j , size );
					j += size;
				}
				else
					j++;
			}
}

void write(int test)
{
	printf( "Case #%d: %d\n" , test , num );
	for(int i = 99;i >= 1;--i)
		if( answers[ i ] )
			printf( "%d %d\n" , i , answers[ i ] );
}

int main()
{
	freopen(  "C-small-attempt0.in" , "r" , stdin  );
	freopen( "out.txt" , "w" , stdout );

	int t;
	scanf( "%d" , &t );
	for(int test = 1;test <= t;++test)
	{
		read();
		work();
		write( test );
	}

	return 0;
}