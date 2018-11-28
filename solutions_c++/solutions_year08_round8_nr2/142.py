#include <iostream>
#include <algorithm>

const int MAX = 10;
const int MAX_L = 15;

int N;
char S[MAX][MAX_L];
int SCnt;
int A[MAX], B[MAX], C[MAX];

int FindColor( const char *c )
{
	for( int i = 0; i<SCnt; ++i )
	{
		if( strcmp( c, S[i] )==0 )
			return i;
	}
	strcpy( S[SCnt], c );
	return SCnt++;
}

void ReadData()
{
	SCnt = 0;
	char str[MAX_L];
	std::cin >> N;
	for( int i = 0; i<N; ++i )
	{
		std::cin >> str >> A[i] >> B[i];
		C[i] = FindColor( str );
	}
}

int CountBits( int k )
{
	int res = 0;
	for( ; k; k >>= 1 )
		if( k&1 )
			++res;
	return res;
}

bool IsOk( int k )
{
	int L[10001];
	std::fill( L, L+10001, -1 );
	int U = 0;
	for( int i = 0; i<N; ++i )
		if( k&(1<<i) )
		{
			std::fill( &L[A[i]], &L[B[i]]+1, C[i] );
			U |= (1<<C[i]);
		}
	if( CountBits( U )>3 )
		return false;
	for( int i = 1; i<=10000; ++i )
	{
		if( L[i]==-1 )
			return false;
	}
	return true;
}

int Work()
{
	int res = -1;
	for( int i = 0; i<(1<<N); ++i )
	{
		if( IsOk( i ) )
		{
			if( res==-1 || CountBits( i )<res )
				res = CountBits( i );
		}
	}
	return res;
}

void Output( int t, int res )
{
	std::cout << "Case #" << t << ": ";
	if( res >=0 )
		std::cout << res << std::endl;
	else
		std::cout << "IMPOSSIBLE" << std::endl;
}

int main()
{
	int n;
	std::cin >> n;
	for( int i = 1; i<=n; ++i )
	{
		ReadData();
		Output( i, Work() );
	}
	return 0;
}
