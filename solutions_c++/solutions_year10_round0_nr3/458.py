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
ll a[10000], b[10000], c[10000];

ll solve(int r, int k, int n)
{
	for (int i = 0; i < n; ++i)
		scanf("%d", &a[i]);	
	memset(b, 0, sizeof(b));
	for (int i = 0; i < n; ++i)
	{
		ll sum = 0;
		int j = i;
		while (sum < k && b[i] < n)
		{
			if ((sum += a[j]) <= k) {++b[i]; c[i] = sum;}
			if (++j == n) j = 0;
		}
	}
	int cur = 0;
	ll sum = 0;
	for (int i = 0; i < r; ++i)
	{
		sum = sum + c[cur];
		cur = (cur + b[cur]) % n;		
	}
	return sum;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;	cin >> t;
	for (int i = 1; i <= t; ++i)
	{
		int r, k, n;
		cin >> r >>	 k >> n;
		cout << "Case #" << i << ": " << solve(r, k,n) << endl;
	}
	return 0;
}
