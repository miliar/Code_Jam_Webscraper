#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cctype>
#include <algorithm>

using namespace std;

const int maxn = 300;

int n, m[maxn];

char g[maxn][maxn];

bool inrange( int x, int y )
{
	return x >= 0 && x < 2*n-1 && y >= 0 && y < m[x] && isdigit(g[x][y]);
}

int withcenter( int x, int y )
{
	int cnt = 0;
	for(int i = 0; i < 2*n-1; i ++ )
		for(int j = 0; j < m[i]; j ++ )
		if( isdigit(g[i][j]) )
		{
			int ri, rj;
			ri = x+(x-i);
			rj = y+(y-j);
			
			cnt = max(cnt, abs(i-x)+abs(j-y));

			
			if( inrange( ri, j ) ){
				if( g[i][j] != g[ri][j] )
					return 0x3fffffff;
			};
		
			
			if( inrange( ri, rj ) ){
				if( g[i][j] != g[ri][rj] )
					return 0x3fffffff;
			};

			
			if( inrange( i, rj ) ){
				if( g[i][j] != g[i][rj] )
					return 0x3fffffff;
			};
	
		}
	cnt ++ ;
	int res = cnt*cnt;
	return res;
}
int main ()
{
	int cases, index; scanf("%d",&cases);
	for(index=0;index<cases;index++)
	{
		memset( g,0,sizeof(g) );
		scanf("%d",&n);
		char s[10];
		gets(s);
		
		for(int i = 0; i < 2*n-1; i++ )
			gets(g[i]);
		
		int mm = 0; 
		for(int i = 0; i < 2*n-1; i++ ) {
			m[i] = strlen(g[i]);
			mm = max(mm, m[i]);
		}

		// enum center
		int ans = 0x3fffffff;
		for(int i = 0; i < 2*n-1; i++ )
		for(int j = 0; j < mm; j ++ ) {
			int ret = withcenter( i, j );
			ans = min( ret, ans );
		}
		printf("Case #%d: %d\n", index+1, ans - n * n);
	}
	return 0;
}
