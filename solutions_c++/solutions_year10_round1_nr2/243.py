#include<stdio.h>
#include<string.h>

int D, I, M, N;
int a[128];

int dp[128][257];
int ins[256];

int get_dis( int v1, int v2 )
{
	return v1 > v2 ? (v1-v2): (v2-v1);
}

void read_it()
{
	scanf( "%d %d %d %d", &D, &I, &M, &N );
	for( int i = 0; i < N; ++i )
		scanf( "%d", &a[i] );
}

void make_it()
{
	for( int i = 0; i < 256; ++i )
		dp[0][i] = get_dis(i,a[0]);
	
		for( int j = 0; j < 256; ++j )
		{
			ins[j] = D+I;
			if( M > 0 )
			{
			for( int k = 0; k < 256; ++k )
			{
				int cnt = (get_dis(j,k)+M-1)/M;
				if( dp[0][k] + I*cnt < ins[j] )
					ins[j] = dp[0][k] + I*cnt;
			}
			}
		}
	for( int j = 0; j < 256; ++j )
		if( ins[j] < dp[0][j] )
			dp[0][j] = ins[j];

	dp[0][256] = D;
	
	for( int i = 1; i < N; ++i )
	{
		dp[i][256] = dp[i-1][256] + D;
		for( int j = 0; j < 256; ++j )
		{
			int now_dis = get_dis(a[i],j);
			dp[i][j] = dp[i-1][256] + now_dis;
			if( dp[i-1][j]+D < dp[i][j] )
				dp[i][j] = dp[i-1][j] + D;
			for( int k = 0; k < 256; ++k )
				if( get_dis(j,k) <= M )
				{
					if( dp[i-1][k] + now_dis < dp[i][j] )
						dp[i][j] = dp[i-1][k] + now_dis;
				}
		}

		for( int j = 0; j < 256; ++j )
		{
			ins[j] = dp[i][256] + I;
			if( M > 0 )
			{
			for( int k = 0; k < 256; ++k )
			{
				int cnt = (get_dis(j,k)+M-1)/M;
				if( dp[i][k] + I*cnt < ins[j] )
					ins[j] = dp[i][k] + I*cnt;
			}
			}
		}


		for( int j = 0; j < 256; ++j )
			if( ins[j] < dp[i][j] )
				dp[i][j] = ins[j];
	}

	int nowmin = dp[N-1][256];
	for( int i = 0; i < 256; ++i )
		if( dp[N-1][i] < nowmin )
			nowmin = dp[N-1][i];
	printf( "%d\n", nowmin );
}

int main()
{
	freopen( "B-large.in", "r", stdin );
	freopen( "out.txt", "w", stdout );
	int t;
	scanf( "%d", &t );
	for( int i = 0; i < t; ++i )
	{
		printf( "Case #%d: ", i+1 );
		read_it();
		make_it();
	}
	return 0;
}