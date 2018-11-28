
//C
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <math.h>
#include <time.h>
//C++
#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cctype>
#include <stack>
#include <string>
#include <list>
#include <queue>
#include <map>
#include <vector>
#include <deque>
#include <set>
using namespace std;

//*************************JUDGE**************************
#define LOCAL_HOST
#define ONLINE_JUDGE
#define TIME_OUT_PUT

//**************************CONSTANT***********************
#define INF 0x7F7F7F7F
#define eps 1e-8
#define PI acos( -1. )
#define PI2 asin ( 1. );
typedef long long LL;
//typedef __int64 LL;   //codeforces
#define MP make_pair
typedef vector<int> VI;
typedef vector<int> VS;
typedef pair<int , int> PII;
#define pb push_back
#define mp make_pair

//***************************SENTENCE************************
#define FOR(a,b,i) for ( i = a ; i < b ; i++ )
#define FORE(a,b,i) for ( i = a ; i <= b ; i++ )
#define REP(i,n) FOR(0,n,i)
#define CL(a,b) memset ( a , b , sizeof ( a ) )
#define sqr(a,b) sqrt ( (double)(a)*(a) + (b)*(b) )

//****************************FUNCTION************************
template < typename T > double DIS ( T va , T vb ) { return sqr ( va.x - vb.x , va.y - vb.y ); }
template <class T> inline T INT_LEN( T v ) { int len = 1 ; while ( v /= 10 ) ++len; return len; }

//end

#define cy 10

double p[cy] , pp[cy];

int state[cy][cy] , step[cy][cy];

int A , B;

void input (){
	scanf ( "%d%d" , &A , &B );
	int i;
	for ( i = 0 ; i < A ; i++ ){
		scanf ( "%lf" , &p[i] );
	}
}

void make_pro ( int n ){
	int i , m = 1 << n , j , k;
	double q;
	for ( i = 0 ; i < m ; i++ ){
		q = 1;
		j = i;
		for ( k = 0 ; k < n ; j >>= 1 , k++ ){
			if ( j & 1 ) q *= p[k] , state[i][k] = 1;
			else q *= ( 1 - p[k] ) , state[i][k] = 0;
		}
		pp[i] = q;
	}
}

void solve (){
	int n = 1 << A , i;
	make_pro ( A );
	// keep typing 
	for ( i = 0 ; i < n ; i++ ){
		int j;
		for ( j = 0 ; j < A ; j++ ){
			if ( state[i][j] == 0 )
				break;
		}
		if ( j >= A ) step[0][i] = B - A + 1;
		else step[0][i] = B - A + 1 + B + 1;
	}
	// enter right away
	for ( i = 0 ; i < n ; i++ ){
		step[1][i] = B + 2;
	}
	// backspace
	int k;
	for ( k = 1 ; k <= A ; k++ ){
		for ( i = 0 ; i < n ; i++ ){
			int j , C = 0 , cc = 0;
			for ( j = A - 1 ; j > A - 1 - k ; j-- ){
				if ( state[i][j] == 0 )
					C++;
			}
			for ( j = A - 1 ; j >= 0 ; j-- ){
				if ( state[i][j] == 0 )
					cc++;
			}
			if ( C == cc ) step[k + 1][i] = B - A + 2 * k + 1;
			else step[k + 1][i] = B - A + 2 * k + 1 + B + 1;
		}
	}
	int ed = k + 1;
	double sum = 0;
	// estimate
	double mn = INF;
	for ( i = 0 ; i < ed ; i++ ){
		sum = 0;
		for ( int j = 0 ; j < n ; j++ ){
			sum += pp[j] * step[i][j];
		}
		mn = min ( mn , sum );
	}
	printf ( "%.6lf\n" , mn );
}

int main (void){
	freopen ( "A-small-attempt0.in" , "r" , stdin );
	freopen ( "A-small-attempt0.out" , "w" , stdout );
	int cas , i;
	scanf ( "%d" , &cas );
	for ( i = 1 ; i <= cas ; i++ ){
		input ( );
		printf ( "Case #%d: " , i );
		solve ( );
	}
	return 0;
}