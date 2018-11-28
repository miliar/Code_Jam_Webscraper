#include <stdio.h>
#include <memory.h>
#include <algorithm>
#include <vector>

using namespace std;

int n;
vector< pair<char, int> > events;

int cache[101][101][101];

int get_next(char t, int f)
{
	for(; f < n; ++ f)
	{
		if(events[f].first == t)
			return events[f].second;
	}
	return 50;
}
int sgn(int x)
{
	return (x > 0) - (x < 0);
}
int go(int idx, int b, int o)
{
	if(b < 0 || b > 100) return 987654321;

	int &res = cache[idx][b][o];
	if(res != -1) return res;

	if(idx >= n)
		return 0;

	res = 987654321;
	if( events[idx].first == 'B' && events[idx].second == b )
	{
		res = min(res, go(idx + 1, b, o - 1) + 1 );
		res = min(res, go(idx + 1, b, o    ) + 1 );
		res = min(res, go(idx + 1, b, o + 1) + 1 );
	}
	else if( events[idx].first == 'O' && events[idx].second == o )
	{
		res = min(res, go(idx + 1, b + 1, o) + 1 );
		res = min(res, go(idx + 1, b    , o) + 1 );
		res = min(res, go(idx + 1, b - 1, o) + 1 );
	}
	else
	{
		int b_dir = sgn( get_next('B', idx) - b );
		int o_dir = sgn( get_next('O', idx) - o );
		res = min(res, go(idx, b + b_dir, o + o_dir) + 1 );
	}
	return res;
}

int sol()
{
	memset(cache, -1, sizeof(cache));
	return go(0, 1, 1);
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int T;
	scanf("%d", &T);
	for(int tt=1; tt<=T; ++ tt)
	{
		scanf("%d", &n);
		events.clear();
		for(int i= 0; i < n; ++ i )
		{
			char type[2]; int at;
			scanf("%s %d", type, &at);
			events.push_back( make_pair(type[0], at) );
		}

		printf("Case #%d: %d\n", tt, sol());
	}
	return 0;
}