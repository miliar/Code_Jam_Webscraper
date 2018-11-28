#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>

#define ll long long

using namespace std;

inline long Min(long a,long b) {return (a>=b) ? b : a;}

ll modPow(ll a, ll x, ll p)
{
	ll res = 1;
	while(x > 0)
	{
		if( x % 2 != 0)
		{
			 res = (res * a) % p;
		}
		a = (a * a) % p;
		x /= 2;
	}
	return res;
}

ll modInverse(ll a, ll p)
{
	return modPow(a, p-2, p);
}

ll modBinomial(ll n, ll k, ll p = 100003)
{
	ll numerator = 1;
	for (ll i=0; i<k; i++)
	{
		numerator = (numerator * (n-i) ) % p;
	}
	
	ll denominator = 1;
	for (ll i=1; i<=k; i++)
	{
		denominator = (denominator * i) % p;
	}
	return ( numerator* modInverse(denominator,p) ) % p;
}

ll mem[501][501]={0};

ll rec(int n,int len)
{
	if (mem[n][len]!=-1) return mem[n][len];
	if (len==1) return mem[n][len]=1;
	ll ans=0;
	for(int i=1;i<len;i++)
	{
		if (n-len-1>=len-i-1) ans=(ans+modBinomial(n-len-1,len-i-1)*rec(len,i))%100003;
	}
	return mem[n][len]=ans;
}

int main()
{
	ifstream dat("c.in");
	ofstream sol("c.out");
	int n,t;
	dat >> t;
	for(int i=0;i<=500;i++)
		for(int j=0;j<=500;j++)
			mem[i][j]=-1;
	for(int y=0;y<t;y++)
	{
		dat >> n;
		ll ans=0;
		for(int i=1;i<=n;i++)
			ans=(ans+rec(n,i))%100003;
		sol << "Case #" << y+1 << ": " << ans << endl;
	}
	return 0;
}
