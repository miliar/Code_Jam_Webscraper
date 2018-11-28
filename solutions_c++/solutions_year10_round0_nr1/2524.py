#include <iostream>
using namespace std;

int t, n;
long long k;
int bit[50];

int fun()
{
	int i;
	for (i = 1; i <= n; i++)
	{
		bit[i] = k % 2;
		k = k / 2;
		//cout<<bit[i]<<endl;
		if (!bit[i])
		{
			return 2;
		}
	}
	return 1;
}

int main()
{
	//freopen("A-small-attempt0.in", "r", stdin);
	//freopen("out.txt", "w", stdout);
	int i, result;
	cin>>t;
	for (i = 1; i <= t; i++)
	{
		cin>>n>>k;
		memset(bit, 0, sizeof(bit));
		result = fun();
		if (result == 1)
		{
			cout<<"Case #"<<i<<": ON"<<endl;
		}
		if (result == 2)
		{
			cout<<"Case #"<<i<<": OFF"<<endl;
		}
	}
	return 0;
}
