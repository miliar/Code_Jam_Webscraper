#include <stdio.h>
#include <string.h>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <sstream>
using namespace std;
#define PB		push_back
#define ALL(v)		(v).begin() , (v).end()
#define SZ(v)		( (int) v.size() )
#define Set(v,x)	memset(  v , x , sizeof(v))
#define two(n)		( 1 << (n) )
#define contain(Set,i)	( ( (Set) & two(i) ) !=0 )
typedef long long LL;

int v[2000] , nv , dp[1010][110] , N;

int solve( int i , int s ) {
	int & r = dp[i][s];
	if (r != -1)		return r;
	if ( i == nv )		return r = 0;

	if ( s != v[i] )
		r = solve( i+1 , s );
	else
		r = 10000000;
	for ( int j = 0 ; j < N ; j++ )
		if ( j != v[i] && s != j )
			r = min( r , 1 + solve( i , j ) );
	return r;
}
int main() {
	int C , nc , Q;
	
	scanf("%d\n", &C);
	for ( nc = 1 ; nc <= C ; nc++) {
		map<string,int> nomes;
		string x;

		scanf("%d\n", &N);
		for ( int i = 0 ; i < N;  i++) {
			getline( cin , x );
			nomes[x] = i;
		}
		scanf("%d\n", &Q);
		nv = 0;
		for (int i = 0 ; i < Q ; i++)
		{
			getline( cin , x );
			v[nv++] = nomes[x];
		}
		Set( dp , -1 );
		int res = solve( 0 , 0 );
		for (int i = 1 ; i < N ; i++)
			res = min( solve( 0 , i ) , res );

		printf("Case #%d: %d\n", nc , res );
	}
	return 0;
}
