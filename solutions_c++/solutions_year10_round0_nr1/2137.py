#include<iostream>
using namespace std;
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin>>t;
	for(int x = 0; x<t;x++)
	{
		int n;
		long long k;
		cin>>n>>k;
		k++;
		bool b = 1;
		for(int i = 0; i< n;i++)
		{
			if(k%2)
			{
				cout<<"Case #"<<x+1<<": OFF\n";
				b = 0;
				break;
			}
			k/=2;
		}
		if(b)
			cout<<"Case #"<<x+1<<": ON\n";
	}
	return 0;
}

