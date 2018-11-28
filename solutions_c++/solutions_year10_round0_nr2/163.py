// p.cpp : Defines the entry point for the console application.
//
#include <string>
#include <vector>
#include <sstream>
#include <set>
#include <iostream>
typedef long long ll;

using namespace std;

string its(ll t)
{
	stringstream s;
	s << t;
	return s.str();
}

ll sti(string s)
{
	stringstream ss;
	ss << s;
	ll t;
	ss >> t;
	return t;
}

ll a[10000];

ll gcd(ll a, ll b)
{
	if (!b) return a;
	return gcd(b, a % b);
}
ll nod;

int solve2(int n)
{
	ll mm = 232332;
	for (int i = 0; i < n; ++i)
	{
		scanf("%lld", &a[i]);		
		mm = max(mm, a[i]);
	}
	int ans = 0;
	for (int i = 1; i <= mm; ++i)
	{
		ll m = a[0] % i; 
		bool ok = true;
		for (int j = 1; j < n; ++j)
		{
			if (m != a[j] % i)
				ok = false;
		}
		if (ok)
			if (m == 0)
				ans = 0;
			else
				ans = i - m;
		nod = m;
	}
	return ans;
}

int solve(int n)
{
	for (int i = 0; i < n; ++i)
		scanf("%lld", &a[i]);		
	ll mx = a[0]; ll mn = a[0];
	for (int i = 1; i < n; ++i) {
		if (a[i] > mx) mx = a[i];
		if (a[i] < mn) mn = a[i];
	}

	 nod = abs(mx - mn);
	for (int i = 0; i < n; ++i)
		for (int j = i+1; j < n; ++j)
			if (nod > 0 && a[i] != a[j])
				nod = gcd(nod, abs(a[i] - a[j]));
	if (a[0] % nod == 0) return 0;
	return nod - a[0] % nod;
}


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;	cin >> t;
	for (int i = 1; i <= t; ++i)
	{
		int n;
		cin >> n;
		ll r = solve(n);
		cout << "Case #" << i << ": " << r << /*" " << nod<<  */endl;
	}
	return 0;
}

