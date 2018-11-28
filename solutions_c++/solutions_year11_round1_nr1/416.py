#include<iostream>
#include<algorithm>
#include<vector>
#include<set>
#include<queue>

#include<cmath>
#include<cassert>
#include<cstdio>

using namespace std;

#define y0 y1985713
#define y1 y0298987

typedef long long ll;

template<class T> inline int size( T x )
{
	return x.size( );
}

void calc(ll n, int pd, int pg)
{
	if (pg == 0)
	{
		if (pd == 0)
		{
			cout << "Possible";
		}
		else
		{
			cout << "Broken";
		}
	}
	else if (pg == 100)
	{
		if (pd == 100)
		{
			cout << "Possible";
		}
		else
		{
			cout << "Broken";
		}
	}
	else
	{
		if (pd == 0)
		{
			cout << "Possible";
		}
		else
		{
			int g = __gcd(pd, 100);
			int den = 100 / g;
			if (den <= n)
			{
				cout << "Possible";
			}
			else
			{
				cout << "Broken";
			}
		}
	}
}

int main( )
{
	int tc; cin >> tc;
	for (int i = 1; i <= tc; i++)
	{
		ll n; int pd, pg; cin >> n >> pd >> pg;
		cout << "Case #" << i << ": "; calc(n, pd, pg);
		cout << endl;
	}
}
