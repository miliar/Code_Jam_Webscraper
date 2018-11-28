
#include<cstdlib>
#include<cstring>
#include<cstdio>

int r , m , n;
int a[1000];
int b[1000];
int c[1000];
int pos[1000];
int main()
{
	freopen("C-large.in" , "r" , stdin);
	freopen("C-large.out" , "w" , stdout);
	int T;
	int cas = 0;
	for ( scanf("%d" , &T) ; T-- ; )
	{
		scanf("%d%d%d" , &r , &m , &n);	
		for ( int i=0 ; i < n ; ++i ) scanf("%d" , &a[i]);
		memset(b , 0 , sizeof(b));
		for ( int i=0 ; i < n ; ++i ) 
		{
			c[i] = i;
			for ( int j=0 ; j < n ; ++j ) 
			{
				if ( b[i] + a[(i + j) % n] > m ) 
				{
					c[i] = (i + j) % n;
					break;
				}
				b[i] += a[(i+j) % n];
			}
		}
		memset(pos , -1 , sizeof(pos));
		long long tot = 0;
		for ( int i=0 , k=0 ; k < r ; ++k ) 
		{
			if ( -1==pos[i] ) 
			{
				pos[i] = k;
				tot += b[i];
				i = c[i];
			}
			else
			{
				long long s = b[i];
				for ( int j=c[i] ; j != i ; j = c[j] )
					s += b[j];
				tot += s * ((r - k - 1) / (k - pos[i]));
				k += (r - k - 1) / (k - pos[i]) * (k - pos[i]);
				memset(pos , -1 , sizeof(pos));
				--k;
			}
		}
		printf("Case #%d: %lld\n" , ++cas , tot);
	}
	return 0;
}
