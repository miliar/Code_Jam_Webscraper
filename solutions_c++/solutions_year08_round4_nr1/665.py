#include <cstdio>
#include <vector>
#include <cstring>

using namespace std;

vector< pair<int, int> > v;
int M, V;
int memo[11000][2];

int go( int x, int st )
{
	//printf("go %d %d\n", x, st);
	if( v[x].second == -1 )
		return st == v[x].first ? 0 : 100000;
	if( memo[x][st] != -1 )
		return memo[x][st];
	
	int ok = 100000;
	if( v[x].first == 1 )
	{
		if( st == 1 )
		{
			ok = min( ok, go( 2*x+1, 1 ) + go( 2*x+2, 1 ) );
		}
		else
		{
			ok = min( ok, min( go( 2*x+1, 0 ), go( 2*x+2, 0 ) ) );
		}
	}
	else
	{
		if( st == 1 )
		{
			ok = min( ok, min( go( 2*x+1, 1 ), go( 2*x+2, 1 ) ) );
		}
		else
		{
			ok = min( ok, go( 2*x+1, 0 ) + go( 2*x+2, 0 ) );
		}
	}
	//printf("temp %d %d = %d\n", x, st, ok);

	if( v[x].second )
	{
		if( v[x].first != 1 )
		{
			if( st == 1 )
			{
				ok = min( ok, go( 2*x+1, 1 ) + go( 2*x+2, 1 ) + 1 );
			}
			else
			{
				ok = min( ok, min( go( 2*x+1, 0 ), go( 2*x+2, 0 ) ) + 1 );
			}
		}
		else
		{
			if( st == 1 )
			{
				ok = min( ok, min( go( 2*x+1, 1 ), go( 2*x+2, 1 ) ) + 1 );
			}
			else
			{
				ok = min( ok, go( 2*x+1, 0 ) + go( 2*x+2, 0 ) + 1 );
			}
		}
	}

	//printf("resp %d %d = %d\n", x, st, ok);
	return memo[x][st] = ok;
}

int main()
{
	int N;
	scanf("%d", &N);
	for(int n = 1; n <= N; n++)
	{
		printf("Case #%d: ", n);

		scanf("%d %d", &M, &V);

		v.resize(M);
		for(int i = 0; i < (M-1)/2; i++)
		{
			scanf("%d %d", &v[i].first, &v[i].second);
			//printf("%d %d\n", v[i].first, v[i].second);
		}

		for(int i = (M-1)/2; i < M; i++)
		{
			scanf("%d", &v[i].first);
			v[i].second = -1;
			//printf("%d %d\n", v[i].first, v[i].second);
		}

		memset( memo, -1, sizeof(memo) );
		int res = go( 0, V );
		if( res >= M )
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", res);
	}
}