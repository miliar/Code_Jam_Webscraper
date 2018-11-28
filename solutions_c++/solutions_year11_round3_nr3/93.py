#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

typedef long long ll;

const int MAXN = 10*1000+10;
ll d[MAXN];
vector<ll> cs;

ll gcd(ll a, ll b)
{
	return b ? gcd(b, a%b) : a;
}

int main()
{
	int t;
	cin >> t;
	for(int T=1; T<=t; T++)
	{
		cs.clear();
		ll n, l, h;
		cin >> n >> l >> h;
		for(int i=0; i<n; i++)
			cin >> d[i];

/*
		sort(d, d+n);

		ll lca = 1;
		for(int i=0; i<n; i++)
		{
			lca = (d[i] * lca) / gcd(d[i], lca);
			cs.push_back(lca);
			for(int j=1; j*j<=d[i]; j++)
				if(d[i] % j == 0)
				{
					cs.push_back(j);
					cs.push_back(d[i]/j);
				}
		}
		sort(cs.begin(), cs.end());
*/
		for(int i=l; i<=h; i++)
			cs.push_back(i);

		int f = -1;
		for(int i=0; i<cs.size(); i++)
		{
			bool o = true;
			for(int j=0; j<n; j++)
				if((d[j] % cs[i]) && (cs[i] % d[j]))
					o = false;
			if(o && cs[i] >= l && cs[i] <= h)
			{
				f = cs[i];
				break;
			}
		}

		cout << "Case #" << T << ": ";
		if(f == -1)
			cout << "NO" << endl;
		else
			cout << f << endl;
	}
	return 0;
}

