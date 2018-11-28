#include<stdio.h>
#include<string.h>

#define MAXN 1024 * 2

__int64 total[ MAXN], sel[ MAXN ], val[ MAXN ];
int g[ MAXN ];

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	int TT, N,R, k;
	scanf("%d",&TT);
	
	for( int ii = 1; ii <= TT; ++ii)
	{
		scanf("%d %d %d", &R, &k, &N);
		
		int sum = 0;
		for( int j = 0; j < N; ++j)
		{
			scanf("%d", &g[ j ]);
			if( sum <= k)
			{
				sum += g[ j ];
			}
		}
		if( sum <= k )
		{
			printf("Case #%d: %I64d\n",ii, (__int64) sum * R);
			continue;
		}
		for( int j = 0; j < N; ++j)
			sel[ j ] = -1;
		memset( val,0, sizeof(val));
		sel[ N - 1 ] = 0;
		val[ 0 ] = 0;
		int last = N - 1, len_ciclu;
		bool ciclu = 0;
		__int64 val_ciclu = 0;
		for( int i = 1; i<= 2* N + 1; i++)
		{
			int sum = 0;
			for( int j = last + 1; j <= last + N; ++j)
				if( sum + g[ j % N ] <= k )
					sum += g[ j % N]; 
				else {
					last = (j - 1) % N;
					break;
				}
			total[ i ] = total[ i - 1] + sum;
			
			if( sel[ last ] != -1 && !ciclu)
			{
				ciclu = 1;
				val_ciclu = total[ i ] - val[ last ];
				len_ciclu = i - sel[ last ];
			}
			if( sel[ last ] == -1 )
			{
				sel[ last ] = i;
				val[ last ] = total[ i ];
			}
				
			
		}
		int nr_ciclu = R / len_ciclu;
		if( nr_ciclu == 0)
		{
			printf("Case #%d: %I64d\n", ii, total[ R ]);
			continue;
		}
		nr_ciclu--;
		__int64 rezultat = ( nr_ciclu * val_ciclu) + total[ R % len_ciclu + len_ciclu] ;
		printf("Case #%d: %I64d\n", ii, rezultat);
	}	
	return 0;
}
