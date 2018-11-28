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

bool solve2(int n, int k)
{	
	return k % (1 << n) >= 1 << (n-1);	
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int i = 1; i <=t; ++i)
	{
		int n, k; 
		scanf("%d%d", &n, &k);
		string ans = "OFF";
		if (solve2(n,k)) ans = "ON";
		cout << "Case #" << i << ": " << ans << endl;
	}
	return 0;
}

