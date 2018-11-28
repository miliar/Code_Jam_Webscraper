#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
using namespace std;

inline int abs( int x ) { return x < 0 ? -x : x; };

int D, I, M;
int n ;
int a [300];
int opt[300][300];

void update( int &x, int y ) {
	if( x == -1 || x > y ) x = y;
}

int cost ( int dis )
{
	return (dis+M-1)/M*I;
}

bool mk[300];

void tryinsert( int dep )
{
	memset( mk, 0, sizeof( mk ) );
	while(1)
	{
		int rec = -1;
		for(int i = 0; i < 256; i ++ ) if( !mk[i] && opt[dep][i] != -1 && ( rec == -1 || opt[dep][rec] > opt[dep][i] ) )
			rec = i;
		if( rec == -1 ) break;
		mk[rec] = 1;
		for(int i = 0; i < 256; i ++ ) if( !mk[i] )
			update(opt[dep][i], opt[dep][rec] + cost( abs(rec-i) ) );
	}
}

int main ()
{
	int cases, index; scanf("%d",&cases);
	for( index = 0; index < cases; index ++ )
	{
		scanf("%d%d%d%d",&D,&I,&M,&n);
		for( int i = 0; i < n; i ++ )
			scanf("%d", a+i);
		
		memset( opt, 0xff, sizeof( opt ) );
		
		for(int i = 0; i < 256; i ++ ) {
			opt[0][i] = 0;
		}
		
		for(int i = 0; i < n; i ++ ) {
			for(int j = 0; j < 256; j ++ ) if( opt[i][j] != -1 ) 
			{
				// just keep it
				if( abs(j-a[i]) <= M )
					update( opt[i+1][a[i]], opt[i][j] );
					
				// delete
				update( opt[i+1][j], opt[i][j] + D );
				
				// modify
				for(int k = 0; k < 256; k ++ )
					if( abs(j-k) <= M )
						update( opt[i+1][k], opt[i][j] + abs(a[i]-k) );
			}
			if( M ) tryinsert(i+1);
		}
		
		int ans = -1;
		for(int i = 0; i < 256; i ++ ) update( ans, opt[n][i] );
		printf("Case #%d: %d\n", index+1, ans);
	}
	return 0;
}
