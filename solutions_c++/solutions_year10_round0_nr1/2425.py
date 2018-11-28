#include <iostream>
using namespace std;

int main()
{
	int n, k, t, i, m;
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	cin>>t;
	for (i = 1; i <= t; i++)
	{
		cin>>n>>k;
		m = (1 << n) - 1;
		k = k & m;
		cout<<"Case #"<<i<<": ";
		if (k == m)
		{
			cout<<"ON"<<endl;
		}
		else
		{
			cout<<"OFF"<<endl;
		}
	}
	return 0;
}