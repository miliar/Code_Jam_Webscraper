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

#define MAX 1000100
int p[MAX],rank[MAX] ;
char conj[MAX];

void init(int s){
	for (int i = 0; i < s; i++) 
	{p[i]=i; rank[i]=0; }
}

void link(int x, int y) {
	if (rank[x] <= rank[y]) {
		p[x] = y;
		if (rank[x] == rank[y])
			rank[y]++;
	} else link(y, x);
}

int find_set(int x) {
	if (x != p[x]) p[x] = find_set(p[x]);
	return p[x];
}

void union_set(int x,int y) {
	link(find_set(x), find_set(y));
}

#define MAXIMO		1000100
char isp[MAXIMO];
long long primos[MAXIMO] , np = 0 , P;

void crivo() {
	Set( isp , 1 );
	isp[0] = isp[1] = 0;
	long long i , j;
	for (i = 2 ; i*i < MAXIMO ; i++)
		if (isp[i]) {
			for (j = i+i ; j < MAXIMO ; j+= i)
				isp[j] = 0;
		}
	for ( i = 2 ; i < MAXIMO ; i++)
		if (isp[i])  {
			primos[np++] = i;
		}
//	printf("num %lld\n", np );
}
bool have( long long a , long long b ) {
	long long i;
//	printf(" test %lld -  %lld   %lld\n", a , b , P );
	for (i = 0 ; i < np ; i++) {
		if ( primos[i] >= P && primos[i] <= a ) {
			if ( (a % primos[i] == 0) && (b % primos[i] == 0 ))
				return true;
		}
	}
//	printf("false\n");
	return false;
}
int main() {
	int C , nc , res;
	long long A , B ;

	crivo();

	scanf("%d\n", &C);
	for ( nc = 1 ; nc <= C ; nc++) {
		cin >> A >> B >> P;
		long long i , j ;
		init( B - A + 1 );

		for (i = 0 ; i < np && primos[i] <= B ; i++) {
			if ( primos[i] < P ) continue;

			vector<long long> v;
			for ( j = (A / primos[i]) * primos[i] ; j <= B;  j+=primos[i])
				if ( j >= A )
					v.PB(j);
	/*		printf("testa %lld , tamanho %d\n", primos[i] , v.size() );
			for ( int k = 0; k < SZ(v) ; k++ )
				printf("%lld " , v[k]);
			printf("\n");
*/
			for ( int k = 1 ; k < SZ(v) ; k++ )
				union_set( (int) (v[0]-A) , (int) (v[k]-A) );
		}
		/*
		for (i = A ; i <= B ; i++)
			for (j = i+1 ; j <= B ; j++) {
				if ( have( i , j ) )
					union_set( (int) (i-A) , (int) (j-A) );
			}

*/
		res = 0;
		Set(conj , 0 );
		for (i = A ; i <= B ; i++)
		{
			j = find_set( (int)(i - A) );
			if (conj[j] == 0) {
				res++;
				conj[j] = 1;
			}
		}
		printf("Case #%d: %d\n", nc , res );
	}	
	return 0;
}
