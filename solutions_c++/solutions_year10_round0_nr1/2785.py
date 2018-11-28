#include <iostream>
#include <cstdio>
using namespace std;

int nPow(int base, int n);

int main()
{
	int n;
	int k;
	int div;
	int tc;
	cin >> tc;
	for(int i=1; i<=tc; i++)
	{
		cin >> n;
		cin >> k;
		div = nPow(2, n);
		k = k%div;
		
		cout << "Case #" << i << ": ";
		if(k == div-1)
		{
			cout << "ON" << endl;
		}
		else
		{
			cout << "OFF" << endl;
		}
	}
	return 0;
}

int nPow(int base, int n)
{
	int res = 1;
	for(int i=0; i<n; i++)
	{
		res = res*base;
	}
	return res;
}
