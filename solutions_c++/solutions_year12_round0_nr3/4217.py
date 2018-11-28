/*
 * =====================================================================================
 *
 *       Filename:  C-small.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  2012/04/14 11時37分37秒
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  YOUR NAME (), 
 *   Organization:  
 *
 * =====================================================================================
 */
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <deque>
#include <algorithm>
#include <vector>
using namespace std;


vector< pair< int, int > > ret;

deque< int > digitalize( int x ) {
	deque< int > ret;

	while ( x ) {
		ret.push_front( x % 10 );
		x /= 10;
	}
	return ret;
}

int numberize( deque< int > x ) {
	int ret = 0;
	while ( !x.empty() ) {
		ret = ret * 10 + x.front();
		x.pop_front();
	}
	return ret;
}

int main() {


	int test;

	scanf( "%d", &test );

	for ( int t = 0; t < test; ++t ) {

		int a, b;

		ret.clear();

		scanf( "%d %d", &a, &b );

		if ( a > b )
			swap( a, b );

		for ( int i = a; i <= b; ++i ) {

			deque< int > now = digitalize( i );

			for ( int j = 0; j < now.size(); ++j ) {
				now.push_front( now.back() );
				now.pop_back();

				int temp = numberize( now );

				if ( digitalize( temp ).size() != now.size() )
					continue;

				if ( a <= i && temp > i && temp <= b ) {
					ret.push_back( pair< int, int >( min( i, temp ), max( i, temp ) ) );
				}

			}

		}

		sort( ret.begin(), ret.end() );

		ret.erase( unique( ret.begin(), ret.end() ), ret.end() );

		printf( "Case #%d: %d\n", t + 1, ret.size() );

	}

	return 0;
}

