#include <cstdlib>
#include <cstdio>

int T , N , K;

int main()
{
	int i ;
	freopen("A-small.in","r" , stdin);
	freopen("A-small.out","w" , stdout);
	
	scanf("%d" , &T);
	
	for( i = 0 ; i < T ; i++ )
	{
		scanf("%d%d" , &N , &K );
		int mod = ( 1 << N ) - 1;
		if( ( K & mod ) == mod )
		{
			printf("Case #%d: ON\n" , i+1 );
		}else
		{
			printf("Case #%d: OFF\n" , i+1 );
		}
	}
	
	return 0;
}
