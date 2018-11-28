/*
 * =====================================================================================
 *
 *       Filename:  B.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  2012/04/14 10時37分20秒
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  YOUR NAME (), 
 *   Organization:  
 *
 * =====================================================================================
 */
#include <iostream>
#include <cstdlib>
#include <queue>
#include <cstdio>
using namespace std;

#define MAXN 110
int avg[ MAXN ], remain[ MAXN ], score[ MAXN ];

int main() {

	int test, n, s, p;

	scanf( "%d", &test );

	for ( int t = 0; t < test; ++t ) {

		scanf( "%d %d %d", &n, &s, &p );

		for ( int i = 0; i < n; ++i ) {
			scanf( "%d", &score[ i ] );
		}


		int ret = 0;
		priority_queue< pair< int, int > > PQ;

		for ( int i = 0; i < n; ++i ) {
			avg[ i ] = score[ i ] / 3;
			remain[ i ] = score[ i ] % 3;

			PQ.push( pair< int, int >( remain[ i ], avg[ i ] ) );

		}

		int cnt = s;

		pair< int, int > now;

		while ( !PQ.empty() ) {

			now = PQ.top(), PQ.pop();


			if ( now.second >= p ) {
				++ret;
				continue;

			}


			if ( now.first == 1 ) {
				if ( now.first + now.second >= p ) {
					++ret;
				}
				continue;
			}
			else if ( now.first == 2 ) {
				if ( now.second + 1 >= p ) {
					++ret;
					continue;
				}

			}

			if ( cnt ) {

				if ( now.first == 2 && now.second + now.first >= p ) {

					++ret, --cnt;
				}
				else if ( !now.first ) {
					if ( now.second < p && ( now.second - 1 >= 0 && now.second + 1 <= 10 && now.second + 1 >= p ) ) 
						++ret, --cnt;
				}
			}
			
			

		}

		printf( "Case #%d: %d\n", t + 1, ret );

		
	}


	return 0;
}

