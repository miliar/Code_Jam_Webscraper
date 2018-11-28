#include<iostream>
#include<cmath>
#include<stdio.h>
#include<cstring>
#include<map>
#include<algorithm>
using namespace std;
const int N = 200010 ;
const int M = 10001 ;
const int INF = 10005 ;
const double eps = 1e-8 ;
#define ll __int64
int n , m ;
typedef pair<int,int> P;

int main()
{
	int i, j, k, tmp, cas = 1, t ,ans, state ;
	int s, mn ;

	for( scanf("%d" , &t ), cas = 1 ; cas <= t ; cas++ )
	{
		scanf("%d", &n ) ;
		mn = 10000005 ;
		s = 0 ;
		ans = 0 ;
		for( i = 0 ; i < n ; ++i ){
			scanf("%d", &k ) ;
			s ^= k ;
			ans += k ;
			if ( k < mn ) mn = k ;
		}
		printf("Case #%d: ", cas ) ;
		if ( s != 0 ) puts("NO"); 
		else printf("%d\n" , ans-mn ) ;
	}

	return 0;
}