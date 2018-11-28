#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <utility>
#include <inttypes.h>

using namespace std;

#define _inline(f...) f() __attribute__((always_inline)); f

#define REP(i,n) for(int i = 0;i < n;++i)
#define FUP(i,a,b) for(int i = (a); i <= (b);++i)
#define FDOWN(i,a,b) for(int i = (a); i >= (b);--i)

#define MAX(x,y) ((x) > (y) ? (x) : (y))
#define MIN(x,y) ((x) < (y) ? (x) : (y))

#define ABS(x) ((x) < 0 ? -(x) : (x))

#define PB push_back
#define MP make_pair

const int INF = 0x3F3F3F3F ;
const int NULO = -1 ;
const double EPS = 1e-10 ;

_inline(int cmp)(double x, double y = 0, double tol = EPS) {
	return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1;
}

//                     a  b  c   d   e  f  	g   h  i   j  k  l   m  n   o   p   q   r   s   t  u   v  w   x  y   z
//                     y  h  e   s   o  c  	v   x  d   u  i  g   l  b   k   r   z   t   n   w  j   p  f   m  a   q
int alpha[ 26 ] = { 24, 7, 4, 18, 14, 2, 21, 23, 3, 20, 8, 6, 11, 1, 10, 17, 25, 19, 13, 22, 9, 15, 5, 12, 0, 16 };

int main(){

	int T, Case = 1;
	scanf("%d\n", &T);

	while(T--){
		char str[ 150 ];
		cin.getline(str, 110);

		int len = strlen(str);

		printf("Case #%d: ", Case++);

		REP(i, len){
			if( str[ i ] != ' ' )
				printf("%c", alpha[ str[ i ] - 'a' ] + 'a' );
			else
				printf(" ");
		}
		printf("\n");
	}


	return 0 ;
}

