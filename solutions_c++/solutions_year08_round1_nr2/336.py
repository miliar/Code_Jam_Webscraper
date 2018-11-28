#include <iostream>
#include <vector>

using namespace std;

vector< vector< int > > like;

int works( int n, int m, int x )
{
	for(int i = 0; i < m; i++)
	{
		bool ok = false;
		for(int j = 0; j < n; j++)
		{
			int st = ( x & (1 << j) ) > 0;
			if( like[i][j] & 1 << st )
				ok = true;
		}
		if( !ok )
			return 0;
	}
	return 1;
}

int count( int x)
{
	int res = 0;
	while( x )
	{
		x &= x-1;
		res++;
	}
	return res;
}

int go( int n, int m)
{
	bool found = false;
	int minv = (1 << n)-1;
	for(int i = 0; i < (1 << n); i++)
	{
		if( works( n, m, i) )
		{
			found = true;
			if( count( i ) < count( minv ) )
				minv = i;
		}
	}
	if( !found )
		return -1;
	return minv;
}

int main()
{
	int K;
	cin >> K;
	for(int k = 1; k <= K; k++)
	{
		int n, m;
		cin >> n >> m;
		like.assign( m, vector<int>(n, 0) );
		
		for(int i = 0; i < m; i++)
		{
			int qt, x, y;
			cin >> qt;
			while( qt-- )
			{
				cin >> x >> y;
				x--;
				like[i][x] |= 1 << y;
			}
		}
		
		int res = go(n, m);
		if( res == -1 )
			cout << "Case #" << k << ": IMPOSSIBLE" << endl;
		else
		{
			cout << "Case #" << k << ":";
			for(int i = 0; i < n; i++)
				cout << ' ' << ((res & (1 << i)) > 0);
			cout << endl;
		}
	}
}