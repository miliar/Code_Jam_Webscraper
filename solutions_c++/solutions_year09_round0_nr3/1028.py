#include <stdio.h>
#include <assert.h>
#include <vector>

using namespace std;

#define MAX_BUFLEN	1024
#define MAX_SRCLEN	500
#define MAX_PATLEN	20
#define MOD_NUMBER	10000

int CountAppear(const char *src, const char *pattern)
{
	static int nums[MAX_SRCLEN+1][MAX_PATLEN+1];
	int n,m, i,j;
	n = (int)strlen( src );
	m = (int)strlen( pattern );
	for( i=0;i<=n;i++ ) nums[i][0] = 0;
	for( i=1;i<=m;i++ ) nums[0][i] = 0;

	for( i=1;i<=n;i++ )
	{
		nums[i][1] = 0;
		for( j=0;j<i;j++ )
		{
			if( src[j]==pattern[0] ) nums[i][1] ++;
		}
		nums[i][1] %= MOD_NUMBER;

		for( j=2;j<=m;j++ )
		{
			nums[i][j] = nums[i-1][j];
			if( src[i-1]==pattern[j-1] ) nums[i][j] += nums[i-1][j-1];
			nums[i][j] %= MOD_NUMBER;
		}
	}
	return nums[n][m];
}

void MaxSubAppear()
{
	FILE *fin, *fout;
	fin = fopen( "in.txt", "r" );
	fout = fopen( "out.txt", "w" );
	assert( fin && fout );

	char pattern[] = "welcome to code jam";
	char buf[MAX_BUFLEN];
	int n, i;

	fgets( buf, MAX_BUFLEN, fin );
	sscanf( buf, "%d", &n );
	for( i=0;i<n;i++ )
	{
		fgets( buf,MAX_BUFLEN,fin );	// 这里buf中即使有换行也没关系，因为模式中没有
		fprintf( fout, "Case #%d: %04d\n", i+1, CountAppear(buf,pattern) );
	}


	fclose( fin );
	fclose( fout );
}

int main()
{
	MaxSubAppear();
	return 0;
}