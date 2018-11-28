#include <cstdio>
#include <map>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

map<string, int> m;
map<int, vector<int> > v;
map<int, int> memo;

int go( int x )
{
	if( memo.count(x) )
		return memo[x];

	vector<int> &w = v[x];
	vector<int> values;

	for(int i = 0; i < w.size(); i++)
		if( w[i] != -1 )
			values.push_back( go( w[i] ) );

	sort( values.begin(), values.end() );
	reverse( values.begin(), values.end() );

	int res = 1 + w.size();
	for(int i = 0; i < values.size(); i++)
		res = max( res, i + values[i] );
	memo[x] = res;
	
	return res;
}

int main()
{
	int K;
	scanf("%d", &K);
	for(int k = 1; k <= K; k++)
	{
		int N;
		scanf("%d", &N);

		m.clear();
		v.clear();
		memo.clear();

		int numS = 0;
		for(int i = 0; i < N; i++)
		{
			string s;
			cin >> s;

			int d;
			cin >> d;
			
			if( m.count(s) == 0 )
				m[s] = numS++;

			vector< int > w;
			for(int j = 0; j < d; j++)
			{
				string t;
				cin >> t;
				if( t[0] <= 'Z' )
				{
					if( m.count(t) == 0 )
						m[t] = numS++;
					w.push_back( m[t] );
				}
			}

			v[ m[s] ] = w;
		}

		printf("Case #%d: %d\n", k, go(0));

	}
}

