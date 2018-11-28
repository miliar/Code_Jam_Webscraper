#include <cstdio>
using namespace std;

int main()
{
	unsigned long K, N, T;
	scanf("%u",&T);
	for( int i=1; i<=T; ++i )
	{
		scanf("%u%u",&N,&K);
		K %= (0x01UL << N);

		bool on = (K == (0x01UL << N) - 1);
		
		printf( "Case #%d: %s\n", i, on ? "ON" : "OFF" );
	}
}