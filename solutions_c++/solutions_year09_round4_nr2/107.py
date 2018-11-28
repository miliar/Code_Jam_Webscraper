#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <ctype.h>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <sstream>
#include <queue>
#include <list>
#include <stack>
using namespace std;
#define PB			push_back
#define ALL(v)			(v).begin() , (v).end()
#define SZ(v)			( (int) v.size() )
#define Set(v,x)		memset(  v , x , sizeof(v))
#define two(n)			( 1 << (n) )
#define contain(S,i)		( (S) & two(i) ) 
#define SQR(v)			( (v) * (v) )
#define ABS(x)			( ( (x) >= 0 ) ? (x) : -(x) )
#define foreach(v,it)		for( typeof((v).begin()) it = (v).begin() ; it != (v).end() ; it++ )

int R , C, F , dp[12][10][two(7)][two(7)];
int vm[50];
char mat[60][60];

int go(int a , int b , int cur , int next ) {
	int & r = dp[a][b][cur][next];
	if (r != -1)
		return r;
	if ( a == R )
		return r = 0;

/*
	printf("\n%d,%d\n", a,b);
	for (int i = 0 ; i < C ; i++)
		printf("%c", contain(cur,i) > 0 ? '.' : '#');
	printf("\n");
	for (int i = 0 ; i < C ; i++)
		printf("%c", contain(next,i) > 0 ? '.' : '#');
	printf("\n");
*/
	int j , i , k;
	r = 10000000;
	// right
	for (j = b ; j < C ; j++) {
		if ( !contain( cur, j) ) break;

		if ( contain( next , j) ) {
			// fall
			k = 1;
			for (i = a+2 ; mat[i][j] == '.' ; i++)
				k++;
			if ( k <= F ) {
				if (k == 1 )
					r = min( r , go(i-1 , j , next , vm[i]));
				else
					r = min( r , go(i-1 , j , vm[i-1] , vm[i]));
			}
			break;
		} else {
		       	if ( j+1 < C && contain( cur , j+1) && !contain( next , j+1 ) ) {
				
				r = min( r , go( a , j , cur , next | two(j+1) ) + 1);
			}
			if ( j > 0 && contain( cur , j-1) && !contain( next , j-1 ) ) {
				
				r = min( r , go( a , j , cur , next | two(j-1) ) + 1);
			}
		}
	}

	// left
	for (j = b ; j >= 0 ; j--) {
		if ( !contain( cur, j) ) break;

		if ( contain( next , j) ) {
			// fall
			k = 1;
			for (i = a+2 ; mat[i][j] == '.' ; i++)
				k++;
			if ( k <= F ) {
				if (k == 1 )
					r = min( r , go(i-1 , j , next , vm[i]));
				else
					r = min( r , go(i-1 , j , vm[i-1] , vm[i]));
			}
			break;
		} else {
			if ( j+1 < C && contain( cur , j+1) && !contain( next , j+1 ) ) {
				
				r = min( r , go( a , j , cur , next | two(j+1) ) + 1);
			}
		       	if ( j > 0 && contain( cur , j-1) && !contain( next , j-1 ) ) {
			
				r = min( r , go( a , j , cur , next | two(j-1) ) + 1);
			}
		}
	}
	/*
	printf("\n%d,%d = %d\n", a,b , r);
	for (int i = 0 ; i < C ; i++)
		printf("%d", contain(cur,i) > 0);
	printf("\n");
	for (int i = 0 ; i < C ; i++)
		printf("%d", contain(next,i) > 0);
	printf("\n");
	*/

	return r;
}
void solve() {
	int i , res = 0;
	scanf("%d %d %d\n", &R,	 &C , &F);
	for (i = 1 ; i <= R ; i++)
		scanf("%s\n", mat[i]);

	for (i = 0 ; i <= C+1 ; i++)
		mat[R+1][i] = mat[R+2][i] = '#';

	Set(dp,-1);
	Set(vm,0);
	int j;
	for (j = 1 ; j <= R ; j++)
	for (i = 0 ; i < C ; i++)
		if ( mat[j][i] == '.' )
			vm[j] |= two(i);

	res = go(1,0 , vm[1], vm[2] );
	if ( res < 1000000 )
		printf("Yes %d\n", res );
	else
		printf("No\n");
}

int main() {
	int C , nc;
	
	scanf("%d\n", &C);
	for ( nc = 1 ; nc <= C ; nc++) {
		cout << "Case #" << nc << ": ";
		solve();
	}	
	return 0;
}
