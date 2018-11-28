/*******************************************************************************************************************************************
* File Name   : b.cpp
* Development : Saturday 14 April 2012 10:45:09 AM IST
* Author      : Xeronix
*******************************************************************************************************************************************/

#include <iostream>
#include <cstdio>
#include <vector>
#include <math.h>
#include <algorithm>
#include <string>
#include <cstring>
#include <string.h>
#include <cstdlib>
#include <sstream>
#include <stack>
#include <queue>
#include <numeric>
#include <utility>
#include <cctype>
#include <list>
#include <limits.h>
#include <signal.h>
#include <time.h>
#include <map>
#include <set>
#include <float.h>

//#include ".prettyprint.hpp"

#define TR(c, i) for ( typeof((c).begin()) i = (c).begin(); i != (c).end(); i++ ) 
#define FOR(i, a, b) for ( i = a; i <= b; i++ )
#define ROF(i, a, b) for ( i = a; i >= b; i-- )
#define ALL(v) (v).begin(), (v).end()
#define SORT(v) sort( ALL(v) )
#define MAX(a, b) ((a) >= (b) ? (a) : (b))
#define MIN(a, b) ((a) <= (b) ? (a) : (b))
#define ABS(a) ((a) < (0) ? (a)*(-1) : (a))
#define SWAP(a, b) {typeof(a) T; T=a; a=b; b=T;}
#define SET(x,a) memset(x,a,sizeof(x))

//#define LIM
#ifdef LIM
	int S, D, Y;
	char *inp, *out, *ipos, *opos, DIG[30];
	#define FRMI inp=( char * )malloc( LIM*sizeof( char ) );fread_unlocked( inp,1,LIM,stdin );ipos=inp;
	#define FWM out=( char * )malloc( LIM*sizeof( char ) );opos=out;
	#define FWO fwrite_unlocked( out,opos-out,1,stdout );
        #define GETI(n) n=0;while(*ipos<33){ipos++;}if(*ipos=='-'){S=-1;ipos++;}else{S=1;}while(*ipos>='0'){n=10*n+(*ipos-'0');ipos++;}n*=S;
	#define PUTI(n) D=0;if(n<0){*opos++='-';n*=-1;}if(!n)*opos++='0';else{while(n){Y=n/10;DIG[D++]=n-Y*10+'0';n=Y;}\
	while(D--)*opos++=DIG[D];}
	#define PUTC(c) *opos++=c;
#endif

using namespace std;

int main()
{	
	int t, s, p, n, a, cnt;
	int i, j, k;

	scanf( "%d", &t ); 

	FOR( i,1,t ) {
		scanf( "%d%d%d", &n, &s, &p );
		vector<bool> f(n+1);

		cnt = 0;

		FOR( j,1,n ) {
			scanf( "%d", &a );
			
			if( a % 3 == 0 && a/3 >= p ) {
				cnt++;
			} else if( (a-1) >= 0 && (a-1) % 3 == 0 && ( (1 + (a-1)/3) >= p ) ) {
				cnt++;
			} else if( (a-2) >= 0 && (a-2) % 3 == 0 && ( (1 + (a-2)/3) >= p ) ) {
				cnt++;
			} else if( (a-2) >= 0 && (a-2) % 3 == 0 && ( (2 + (a-2)/3) >= p ) ) {
				f[j] = true;
			} else if( (a-3) >=0 && (a-3) % 3 == 0 && (2 + (a-3)/3 ) >= p ) { 
				f[j] = true;
			} else if( (a-4) >=0 && (a-4) % 3 == 0 && ( (2+ (a-4)/3 ) >= p ) ) {
				f[j] = true;
			}
		}

		FOR( j,1,s ) {
			FOR( k,1,n ) {
				if( f[k] ) {
					f[k] = false;
					cnt++;
					break;
				}
			}
		}

		printf( "Case #%d: %d\n", i, cnt );
	}

	return 0;
}
