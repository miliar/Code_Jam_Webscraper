#include<iostream>
#include<cstdio>

using namespace std;

int main()
{

	freopen ( "sc.in","r",stdin);
	freopen ( "sc.out","w",stdout );
	int T ;
	scanf ( "%d " ,&T);
	int KK =T ;
	while (T -- )
	{
		printf ( "Case #%d: ",KK-T);
		int N ;
		long K;
		scanf ( "%d%ld",&N,&K);
		if ( (K & ((1 <<  N )- 1)   ) == ((1 << N ) - 1 ) )
		    printf ( "ON\n");
		else printf ( "OFF\n");
	}
}
