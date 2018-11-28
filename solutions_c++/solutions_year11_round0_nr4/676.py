#include<iostream>
#include<cmath>
#include<stdio.h>
#include<cstring>
#include<map>
#include<algorithm>
using namespace std;
const int N = 1510 ;
const int M = 10001 ;
const int INF = 10005 ;
const double eps = 1e-8 ;
#define ll __int64
int n , m ;
typedef pair<int,int> P;

int a[N], b[N];

int main()
{
	int i, j, k, tmp, cas = 1, t ,ans, state ;
	int s, mn ;

	for( scanf("%d" , &t ), cas = 1 ; cas <= t ; cas++ )
	{
		scanf("%d", &n ) ;
		for( i = 0 ; i < n ; ++i ){
			scanf("%d", &a[i] ) ;
			b[i] = a[i] ;
		}
		sort( b, b+n ) ;
		ans = 0 ;
		for( i = 0 ; i < n ; ++i ){
			if ( a[i] != b[i] ) ans++ ;
		}
		printf("Case #%d: ", cas ) ;
		printf("%.6f\n" , double(ans) ) ;
	}

	return 0;
}