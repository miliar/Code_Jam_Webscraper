#include <vector>
#include <map>
#include <list>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <functional>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <ctime>

using namespace std;

int dat[11][2048];
int p;
int dp[11][2048][2048];

void read_it()
{
	scanf( "%d", &p );
	for( int i = 0; i <= p; ++i )
		for( int j = 0; j < (1<<(p-i)); ++j )
			scanf( "%d", &dat[i][j] );
}

int make_it()
{
	for( int j = 0; j < (1<<p); ++j )
		for( int k = 0; k < (1<<p); ++k )
		{
			int cnt = 0;
			for( int l = 0; l < p; ++l )
				if( !( k & (1<<l) ) )
					++cnt;
			if( cnt > dat[0][j] )
			{
				dp[0][j][k*2] = -1;
				dp[0][j][k*2+1] = -1;
			}
			else
			{
				dp[0][j][k*2] = 0;
				dp[0][j][k*2+1] = 0;
			}
		}

	for( int i = 1; i <= p; ++i )
		for( int j = 0; j < (1<<(p-i)); ++j )
			for( int k = 0; k < (1<<(p-i+1)); ++k )
			{
				int left_min = -1;
				if( dp[i-1][j*2][k*2] >= 0 )
					if( dp[i-1][j*2][k*2] < left_min || left_min == -1 )
						left_min = dp[i-1][j*2][k*2];
				if( dp[i-1][j*2][k*2+1] >= 0 )
					if( dp[i-1][j*2][k*2+1] < left_min || left_min == -1 )
						left_min = dp[i-1][j*2][k*2+1];
				int right_min = -1;
				if( dp[i-1][j*2+1][k*2] >= 0 )
					if( dp[i-1][j*2+1][k*2] < right_min || right_min == -1 )
						right_min = dp[i-1][j*2+1][k*2];
				if( dp[i-1][j*2+1][k*2+1] >= 0 )
					if( dp[i-1][j*2+1][k*2+1] < right_min || right_min == -1 )
						right_min = dp[i-1][j*2+1][k*2+1];

				int base = 0;
				if( k & 1 )
					base = dat[i][j];

				if( left_min == -1 || right_min == -1 )
					dp[i][j][k] = -1;
				else
					dp[i][j][k] = base + left_min + right_min;
			}

	int nowmin = -1;
	if( dp[p][0][0] != -1 )
		nowmin = dp[p][0][0];
	if( dp[p][0][1] != -1 )
		if( dp[p][0][1] < nowmin || nowmin == -1 )
			nowmin = dp[p][0][1];
	return nowmin;
}

int main()
{
	freopen( "out.txt", "w", stdout );
	freopen( "B-large.in", "r", stdin );
	int t;
	scanf( "%d", &t );
	for( int i = 0; i < t; ++i )
	{
		read_it();
		printf( "Case #%d: %d\n", i+1, make_it() );
	}

	return 0;
}