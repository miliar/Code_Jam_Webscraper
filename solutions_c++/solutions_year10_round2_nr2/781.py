#include<stdio.h>

int n , k , b , t;
int massX[ 1000 ];
int massV[ 1000 ];
int ans;
bool impos;

void read()
{
	scanf( "%d%d%d%d" , &n , &k , &b , &t );
	int i;
	for(i = 0;i < n;++i)
		scanf( "%d" , massX + i );
	for(i = 0;i < n;++i)
		scanf( "%d" , massV + i );
	ans = 0;
}

void work()
{
	int already = 0;
	int i;
	int right = 0;
	impos = false;
	for(i = n - 1;i >= 0;--i)
	{
		if( already == k )
			return;
		int range = b - massX[ i ];
		if( range <= t * massV[ i ] )
		{
			ans += right;
			already++;
		}
		else
		{
			right++;
		}
	}
	if( already == k )
		return;
	impos = true;
}

int main()
{
	freopen( "B-large.in" , "r" , stdin );
	freopen( "ans.txt" , "w" , stdout );
	int t;
	scanf( "%d" , &t );
	for(int test = 1;test <= t;++test)
	{
		read();
		work();
		if( impos )
			printf( "Case #%d: IMPOSSIBLE\n" , test );
		else
			printf( "Case #%d: %d\n" , test , ans );
	}

	return 0;
}