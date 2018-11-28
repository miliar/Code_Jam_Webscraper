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

int64 N , Fd , Fg;

int main(){
	
	int t;
	scanf( "%d" ,&t );
	
	for( int tt = 1 ; tt <= t ; tt++ ){
		scanf( "%lld%lld%lld" ,&N ,&Fd ,&Fg );
		/*
		if( Fd + Fg == 0 || (Fd == 0 && Fg != 0) ){
			printf( "Case #%d: Possible\n" ,tt );
			continue;
		}
		if( Fd != 0 && Fg == 0 ){
			printf( "Case #%d: Broken\n" ,tt );
			continue;
		}*/
		
		bool good = 0;
		
		for( int D = 1 ; D <= N ; D++ ){
			for( int G = D ; G <= 100000 ; G++ ){
				int WD = D * Fd / 100;
				int WG = G * Fg / 100;
				if( WD * 100 == D * Fd && WG * 100 == G * Fg && WD <= WG && D - WD <= G - WG ){
					good = 1;
					goto end;
				}
			}
		}
		end:;
		if( good ) printf( "Case #%d: Possible\n" ,tt );
		else printf( "Case #%d: Broken\n" ,tt );
	}	
	
	return 0;
}
