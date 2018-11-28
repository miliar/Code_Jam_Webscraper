#include <cstdio>
#include <cstring>

#include <algorithm>

using namespace std;

struct trip {
	int start, finish;

	trip() {}
	trip( int start, int finish ): start( start ), finish( finish ) {}

	friend bool operator < ( const trip &A, const trip &B ) {
		return A.start < B.start;
	}
};

int nA, nB, T;
trip A[105], B[105];
bool bioA[105], bioB[105];

int rtime()
{
	char S[10]; scanf( "%s", S );

	int h = (S[0] - '0') * 10 + (S[1] - '0');
	int m = (S[3] - '0') * 10 + (S[4] - '0');

	return h * 60 + m;
}

void dfsA( int x );
void dfsB( int x );

void dfsA( int x )
{
	bioA[x] = true;

	for( int y = 0; y < nB; ++y )
		if( !bioB[y] && A[x].finish + T <= B[y].start ) { dfsB( y ); break; }
}

void dfsB( int x )
{
	bioB[x] = true;

	for( int y = 0; y < nA; ++y )
		if( !bioA[y] && B[x].finish + T <= A[y].start ) { dfsA( y ); break; }
}

int main( void )
{
	freopen( "pB.in", "r", stdin );
	freopen( "pB.out", "w", stdout );

	int nround; scanf( "%d", &nround );

	for( int round = 0; round < nround; ) {
		scanf( "%d", &T );
		scanf( "%d %d", &nA, &nB );
		for( int i = 0; i < nA; ++i ) {
			int start = rtime(), finish = rtime();
			A[i] = trip( start, finish );
		}
		for( int i = 0; i < nB; ++i ) {
			int start = rtime(), finish = rtime();
			B[i] = trip( start, finish );
		}

		sort( A, A + nA );
		sort( B, B + nB );
		memset( bioA, false, sizeof bioA );
		memset( bioB, false, sizeof bioB );
		
		int retA, retB; retA = retB = 0;

		while( true ) {
			int i, j;

			for( i = 0; i < nA; ++i )
				if( !bioA[i] ) break;
			for( j = 0; j < nB; ++j )
				if( !bioB[j] ) break;

			if( i < nA ) {
				if( j < nB ) {
					if( A[i].start < B[j].start ) {
						dfsA( i );
						++retA;
					} else {
						dfsB( j );
						++retB;
					}
				} else {
					dfsA( i );
					++retA;
				}
			} else {
				if( j < nB ) {
					dfsB( j );
					++retB;
				} else break;
			}
		}

		printf( "Case #%d: %d %d\n", ++round, retA, retB );
	}

	return 0;
}
