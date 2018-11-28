#include<iostream>
#include<cstdio>

using namespace std;

int L, D, N;
char code[5100][20];
char question[1000];
bool val[20][50];

int main()
{
	//freopen( "in.txt", "r", stdin );
	//freopen( "out.txt", "w", stdout );
	scanf( "%d %d %d", &L, &D, &N );
	for (int i = 0; i < D; i++ )
		scanf( "%s", code[i] );
	for (int T = 0; T < N; T++ )
	{
		scanf( "%s", question );
		memset( val, false, sizeof( val ) );
		int ans = 0, len = strlen( question ), j = 0;
		for (int i = 0; i < L; i++ )
		{
			if ( question[j] == '(' )
			{
				j ++;
				while ( question[j] != ')' )
					val[i][question[j++] - 'a'] = true;
				j ++;
			}
			else val[i][question[j++] - 'a'] = true;
		}
		for (int i = 0; i < D; i++ )	
		{
			bool ok = true;
			for (int k = 0; k < L; k++ )
				if ( !val[k][code[i][k] - 'a'] ) ok = false;
			if ( ok ) ans ++;
		}
		printf( "Case #%d: %d\n", T + 1, ans );
	}
}
