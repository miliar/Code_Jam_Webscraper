#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <set>
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

inline int ones( int n ){  int sum = 0;  while (n)  {    sum += (n & 1);    n >>= 1;  }  return sum;	}

int can[10010];
int v[10010] , N , V , nos , folhas;

int go(int i , int mask) {
//	printf("%d    %d\n", i , mask );
	int g = v[i];
	if (can[i] && contain(mask,i) )
		g = !v[i];
	if ( i >= nos )
		return v[i];
	else {
		if ( g == 1 )
			return go(2*(i+1)-1 , mask ) && go(2*(i+1) , mask );
		else
			return go(2*(i+1)-1 , mask ) || go(2*(i+1) , mask );
	}
//	printf("wrong\n\n");
	return -1;
}
int eval( int mask ) {
	int val = go(0 , mask);
//	printf("mask: %d  ---    %d\n", val , mask );
	return val == V ? ones(mask) : -1;
}
int main() {
	int C , nc , res , i , j ;
	
	scanf("%d\n", &C);
	for ( nc = 1 ; nc <= C ; nc++) {
		cin >> N >> V;
		Set( can , 0 );
		nos = (N-1)/2;
		for (i = 0 ; i < nos ; i++) {
			cin >> v[i] >> j;
			can[i] = j;
		}

		folhas = (N+1)/2;
		for (j = 0 ; j < folhas ; j++) {
			cin >> v[i++];
//			printf("folha %d ,  %d\n", i-1 , v[i-1]);
		}
		res = -1;
		for ( i = 0 ; i < two(nos) ; i++) {
			j = eval(i);
			if ( j != -1 )
				if ( res == -1 || res > j )
					res = j;
//			printf(" mask : %d    %d     %d\n", i , j , res );
		}
		printf("Case #%d: ", nc );
		if (res == -1)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", res );
	}	
	return 0;
}
