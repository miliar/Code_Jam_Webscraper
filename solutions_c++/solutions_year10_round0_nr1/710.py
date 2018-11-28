#include <cstdio>
#include <iostream>
#include <string>
using namespace std;

const int step(const int v, const int st)
{
	if (st==0)
		return 1;
	else 
		return v*step(v, st-1);
}

const string solve(const int n, const int k)
{
	int st;
	st= step(2, n);
	if ((st-1)==(k%st))
		return "ON";
	else
		return "OFF";
}

int main()
{
	int i, j, t, n, k;
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	cin >> t;
	for(i=1; i<=t; ++i)
	{
		cin >> n;
		cin >> k;
		cout <<"Case #" <<i <<": " <<solve(n, k) <<endl;  
	}
	return 0;
}
