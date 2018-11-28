#include <cstdlib>
#include <cstdio>

__int64 T , R , K , N;
__int64 G[2000];
__int64 p[2000];
__int64 s[2000];
int main()
{
	freopen("C-small.in" , "r" , stdin );
	freopen("C-small.out" , "w" , stdout );
	
	__int64 i , j , t;
	
	scanf("%I64d",&T);
	
	for( t = 1 ; t <= T ; t++ )
	{
		scanf("%I64d%I64d%I64d",&R , &K , &N );
		__int64 ans = 0;
		for( i = 1 ; i <= N ; i++ ) scanf("%I64d",G+i);	
		
		for( i = 1 ; i <= N ; i++ )
		{
			__int64 sum = G[i];
			p[i] = ((i+1)>N)?1:i+1;
			if( G[i] > K )
			{
				p[i] = i;
				s[i] = 0;
				continue;
			}
			for( j = ((i+1)>N)?1:i+1 ; j != i ; j= ((j+1)>N)?1:j+1 )
			{			
				if( sum + G[j] <= K )
				{
					p[i] = ((j+1)>N)?1:j+1;
					sum += G[j];
					
				}else{		
					p[i] = j;		
					break;
				}
			}
			s[i] = sum;
		}
		
		__int64 cur = 1;
		for( i = 1 ; i <= R ; i++ )
		{
			ans = ans + s[cur];
			cur = p[cur];
		}
		printf("Case #%I64d: %I64d\n" , t , ans );
		
	}
	
	
	return 0;
}
