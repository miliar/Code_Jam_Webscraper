
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

int test,a,b,result,x,y,z,p,q,r;

int main () {
	scanf("%d",&test);
	for ( int t = 0 ; t < test ; t++ ) {
		result = 0;
		scanf("%d%d",&a,&b);
		for ( int i = a ; i <= b ; i++ ) {
			z = log10(i);
			x = i % 10;
			y = i/10 + pow(10,z)*x;
			while ( y != i ) {
				if ( y > i ) {
					if ( y >= a && y <= b ) {
						result++;
					}
				}
				x = y % 10;
				y = y/10 + pow(10,z)*x;
			}			
		}
		printf("Case #%d: %d\n",t+1,result);
	}
	return 0 ;
}

