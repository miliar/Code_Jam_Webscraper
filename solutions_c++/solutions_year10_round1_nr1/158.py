#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int N, K;
char mp[100][100];

int move[8][2] = {{0,1},{1,0},{0,-1},{-1,0},{1,1},{-1,1},{1,-1},{-1,-1}};

bool inrange( int x, int y )
{
	return x >= 0 && x < N && y >= 0 && y < N; 
}

int check ( int x, int y )
{
	if( mp[x][y] == '.' ) return 0 ;
	
	int t = ( mp[x][y] == 'B' ? 2 : 1 );
	for(int j = 0; j < 8; j ++ ) {
		bool ok = 1;

		for(int i = 0; ok && i < K; i ++ )
		{
			int dx = x + i * move[j][0];
			int dy = y + i * move[j][1];
			if( inrange(dx, dy) && mp[dx][dy] == mp[x][y] )
			{
			} else ok = 0;
		}
		
		if( ok ) return t;
	}	
	return 0;
}

int main ()
{
	int cases, index; scanf("%d",&cases);
	for(index = 0; index < cases; index ++ )
	{
		scanf("%d%d",&N,&K);
		for(int i = 0; i < N; i ++ )
			scanf("%s", mp[i]);
			
		for(int i = 0; i < N; i ++ )
		{
			for(int j = N-1; j >= 0; j -- )
			{
				for(int k = j; k >= 0; k -- )
					if( mp[i][k] != '.' ) {
						swap( mp[i][j], mp[i][k] );
						break;
					}
			}
		}
		
//		for(int i = 0; i < N; i ++ ) printf("%s\n", mp[i]);
		
		int ans = 0;
		for(int i = 0; i < N; i ++ )
			for(int j = 0; j < N; j ++ )
				ans |= check(i, j);
				
		printf("Case #%d: ", index+1);
		if( ans == 0 ) printf("Neither\n");
		if( ans == 1 ) printf("Red\n");
		if( ans == 2 ) printf("Blue\n");
		if( ans == 3 ) printf("Both\n");
	}
	return 0;
}
