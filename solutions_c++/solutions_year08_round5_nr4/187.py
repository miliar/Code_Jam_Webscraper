#include<iostream>
#include<string>
#include<vector>
#include<cstdio>
#include<map>
#include<set>
#include<queue>
#include<algorithm>
using namespace std;
#define MOD 10007

int invtable[MOD];

int AAV   [100000000];
int AACMOD[100000000];

int solve( int x1, int y1, int x, int y )
{
	x -= x1;
	y -= y1;

	long long ret = 1;

//	printf( "%d %d\n", x, y );
	if( x == 0 && y == 0 ) ret = 1;
	else if( x <= 0 || y <= 0 ) ret = 0;
	else{
		int d1 = (2 * x -     y);
		int d2 = ( -  x + 2 * y);
		if( d1 < 0 || d2 < 0 || d1 % 3 != 0 || d2 % 3 != 0 ) ret = 0;
		else{
			d1 /= 3, d2 /= 3;
			// (d1+d2)Cd1 % 10007
			int aaA   = AAV[d1+d2];
			int cmodA = (d1+d2) % MOD;
			int aaB   = (long long)AAV[d1] * AAV[d2] % MOD;
			int cmodB = d1 % MOD + d2 % MOD;
			if( cmodA > cmodB )
				ret = 0;
			else
				ret = (long long)aaA * invtable[aaB] % MOD;
		}
	}
//	printf( "%d,%d = %lld\n", x, y, ret );
	return ret;
}

int main( void )
{
	AAV[0] = 1;
	for( long long i = 1, CMOD = 0, V = 1; i <= 100000000; i ++ ){
		if( i % MOD != 0 )
			V = V * i % MOD;
		AAV[i] = V;
	}
	cerr << "Table 1" << endl;

	for( int i = 1; i < MOD; i ++ ){
		for( int j = i; j < MOD; j ++ ){
			if( i * j % MOD == 1 ){
				invtable[i] = j;
				invtable[j] = i;
			}
		}
	}
	cerr << "Table 2" << endl;

	int N;
	cin >> N;
	for( int CC = 0; CC < N; CC ++ ){
		int Y, X, R;
		cin >> Y >> X >> R;
		vector< pair<int,int> > rr;
		for( int i = 0; i < R; i ++ ){
			int x, y;
			cin >> y >> x;
			rr.push_back( pair<int,int>(x,y) );
		}
		sort( rr.begin(), rr.end() );
		int ret = 0;
		for( int i = (1<<R)-1; i >= 0; -- i ){
	//		printf( "%d\n", i );
			int cr = 0;
			int x0 = 1, y0 = 1;
			long long v = 1;
			for( int j = 0; j < R; j ++ ){
				if( i & (1<<j) ){
					v = v * solve( x0, y0, rr[j].first, rr[j].second ) % MOD;
					x0 = rr[j].first, y0 = rr[j].second;
					cr ++;
				}
			}
			v = v * solve( x0, y0, X, Y ) % MOD;
			if( cr % 2 == 0 )
				ret += v + MOD;
			else
				ret += -v + MOD;
		}

		printf( "Case #%d: %d\n", CC + 1, ret % MOD );
	}
	return 0;
}
