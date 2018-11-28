#include <cstdio>
#include <vector>
#include <utility>
#include <iostream>
#include <string>

using namespace std;

struct Problem
{
	void operator()()
	{
		int T;
		scanf("%d", &T);

		for( int i = 0; i < T; ++i )
		{
			int R, K, N;
			scanf( "%d%d%d", &R, &K, &N );

			vector<int> g(N);
			for( int j = 0; j < N; ++j )
				scanf( "%d", &g[j] );

			solve(R, K, g, i+1);
		}
	}

	void solve( int R, int K, vector<int> const& g, int number )
	{
		const int G = g.size();
		long long money = 0;
		vector< pair<long long, int> > cache(G, pair<long long, int>(-1, -1) );

		for( int i = 0, pos = 0; i < R; ++i )
		{
			if ( cache[pos].first != - 1 )
			{
				money += cache[pos].first;
				pos = cache[pos].second;
			}
			else
			{
				int j = pos;
				long long y = 0;
				for( ; j < G && y + g[j] <= K; ++j )
					y += g[j];
				if ( j == G )
					for( j = 0; j < pos && y + g[j] <= K; ++j )
						y += g[j];
				cache[pos] = make_pair( y, j );
				money += y;
				pos = j;
			}
		}
		cout << "Case #" << number << ": " << money << endl;
	}
};

int main()
{
	freopen( "input.txt", "rt", stdin );
	freopen( "output.txt", "wt", stdout );

	Problem()();
}
