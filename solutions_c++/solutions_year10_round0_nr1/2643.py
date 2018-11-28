#include <cstdio>

int power2[31];

void init( void ){

	power2[0] = 1;
	for( int i = 1 ; i < 31 ; i ++ )
		power2[i] = power2[i-1]*2;

	return;
}

bool judge( int n , int k ){

	if( k < power2[n]-1 )
		return false;

	if( k == power2[n]-1 )
		return true;

	return (k-(power2[n]-1))%power2[n] == 0;
}

int main( void ){

	//freopen( "A-small-attempt0.in" , "r" , stdin );
	//freopen( "A-small-attempt0.out" , "w" , stdout );

	freopen( "A-large.in" , "r" , stdin );
	freopen( "A-large.out" , "w" , stdout );

	init();

	int testcases;
	scanf("%d",&testcases);
	for( int cases = 1 ; cases <= testcases ; cases ++ ){

		int n,k;
		scanf("%d%d",&n,&k);

		printf("Case #%d: %s\n",cases,(judge(n,k)?"ON":"OFF"));
	}

	//system("pause");

	return 0;
}