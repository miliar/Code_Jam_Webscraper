
/*
 * Author: ajay0221
 * Email: ajay0221@gmail.com
 */
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <cassert>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <cmath>

using namespace std ;

int test,n,S,p,x,result;

int main () {
	scanf("%d",&test);
	for ( int t = 0 ; t < test ; t++ ) {
		result = 0;
		scanf("%d%d%d",&n,&S,&p);
		for ( int i = 0 ; i < n ; i++ ) {
			scanf("%d",&x);
			if ( p == 0 ) result++;			
			if ( p > 0 && x >= 3*p - 2 ) result++;
			else if ( p > 1 && S > 0 && x >= 3*p - 4 ) {
				S--;
				result++;
			} 		
		}
		printf("Case #%d: %d\n",t+1,result);
	}
	return 0 ;
}

