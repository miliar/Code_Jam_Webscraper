#include <stdio.h>
#include <functional>
#include <bitset>
#include <math.h>
#include <time.h>
#include <stdlib.h>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <sstream>
#include <queue>
#include <string.h>
using namespace std;

typedef vector<int> vi;
typedef vector<vi> vii;
typedef vector<string> vs;
typedef long long int64;

#define forit(a,b) for(typeof((b).end()) a=(b).begin();a!=(b).end();a++)
#define clr(a,b) memset(a,b,sizeof a)
#define all(a) a.begin(),a.end()
#define sorta(a) sort(all(a))

int64 N , L , t , C , a[ 1001000 ] , inp[ 1001000 ];
pair< int64 , int > sor[ 1001000 ];

int main(){
	int test;
	scanf( "%d" ,&test );
	for( int ttest = 1 ; ttest <= test ; ttest++ ){
		scanf( "%lld%lld%lld%lld" ,&L ,&t ,&N ,&C );
		for( int q = 0 ; q < C ; q++ ){
			scanf( "%lld" ,&inp[ q ] );
		}
		for( int q = 0 ; q < N ; q++ ){
			a[ q ] = inp[ q % C ];
			sor[ q ].first = -a[ q ];
			sor[ q ].second = q;
		}
		sort( sor , sor + N );
		int64 ret1 = 0 , L2 = L , ret2 = 0 , end = N;
		for( int q = 0 ; q < N ; q++ ){
			if( ret1 + a[ q ] * 2ll >= t ){
				int64 r = (t - ret1) / 2ll;
				if( L ){
					ret1 += r * 2ll + a[ q ] - r;
					L --;
				}
				else{
					ret1 += a[ q ] * 2ll;
				}
				ret2 += a[ q ] * 2ll;
				end = q + 1;
				break;
			}
			ret1 += a[ q ] * 2ll;
			ret2 += a[ q ] * 2ll;
		}
		for( int q = 0 ; q < N ; q++ ){
			sor[ q ].first *= -1;
			if( sor[ q ].second >= end ){
				if( L ){
					ret1 += sor[ q ].first;
					L --;
				}
				else{
					ret1 += sor[ q ].first * 2ll;
				}
				if( L2 ){
					ret2 += sor[ q ].first;
					L2 --;
				}
				else{
					ret2 += sor[ q ].first * 2ll;
				}
			}
		}
		printf( "Case #%d: %lld\n" ,ttest ,min( ret1 , ret2 ) );
	}
	return 0;
}
