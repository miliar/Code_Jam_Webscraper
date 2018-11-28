#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

const int MAXP = 1000*1000+10;
int np[MAXP];

typedef long long ll;
vector<ll> p;

ll rp(ll n, ll p)
{
	int r = 0;
	while(n >= p)
	{
		n /= p;
		r++;
	}
	return r;
}

int main()
{
	np[1] = true;
	for(int i=2; i<MAXP; i++)
		if(!np[i])
		{
			p.push_back(i);
			for(int j=2*i; j<MAXP; j+=i)
				np[j] = true;
		}
	
	int TC;
	cin >> TC;
	for(int T=1; T<=TC; T++)
	{
		ll n;
		cin >> n;
		int r = 0;
		for(int i=0; i<p.size(); i++)
		{
			int d = rp(n, p[i]);
			if(!d)
				break ;
//			cout << "@ " << d << endl;
			r += d - 1;
		}
		if(n > 1)
			r++;
		cout << "Case #" << T << ": " << r << endl;
	}
	return 0;
}

