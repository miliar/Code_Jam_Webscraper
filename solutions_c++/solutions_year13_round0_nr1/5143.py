#include <cstdio>
#include <algorithm>
#include <cstring>
#include <map>

using namespace std;

char s[10][10];

int chk( int x, int y, int dx, int dy )
{
	int cnt[200] = {0};
	for( int i = 0; i < 4; ++i )
	{
		cnt[ s[x][y] ]++;
		x += dx, y += dy;
	}

	if( cnt['X'] == 4 )	return 1;
	if( cnt['X'] == 3 && cnt['T'] == 1 )	return 1;
	if( cnt['O'] == 4 )	return -1;
	if( cnt['O'] == 3 && cnt['T'] == 1 )	return -1;
	return 0;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int T, cases = 1;
	int i, j, k, t;
	int st;

	scanf("%d", &T);
	while( T-- )
	{
		for( i = 0; i < 4; ++i )
			scanf("%s", s[i]);
		
		st = 0;
		for( i = 0; st == 0 && i < 4; ++i )
			st = chk(i, 0, 0, 1);
		for( i = 0; st == 0 && i < 4; ++i )
			st = chk(0, i, 1, 0);
		if( st == 0 )
			st = chk(0, 0, 1, 1);
		if( st ==0 )
			st = chk(3, 0, -1, 1);

		printf("Case #%d: ", cases++);
		if( st == 1 )
			puts("X won");
		else if( st == -1 )
			puts("O won");
		else
		{
			k = 0;
			for( i = 0; i < 4; ++i )
				for( j = 0; j < 4; ++j )	if( s[i][j] == '.' )
					k++;
			if( k )
				puts("Game has not completed");
			else
				puts("Draw");
		}
	}

	return 0;
}