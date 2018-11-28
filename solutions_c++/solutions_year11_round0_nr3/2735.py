#include <iostream>
#include <algorithm>
using namespace std;

int c[1010];

int main()
{
	freopen("pc.in", "r", stdin);
	freopen("pc.out", "w", stdout);

	int T,t;
	int n,i,sum,minc,xor;

	cin>>T;
	for(t=1; t<=T; t++)
	{
		cin>>n;
		for(i=0; i<n; i++)
		{
			cin>>c[i];
		}

		minc = 10000000;
		sum = 0;
		xor = 0;
		for(i=0; i<n; i++)
		{
			minc = min(minc,c[i]);
			sum = sum + c[i];
			xor = xor ^ c[i];
		}

		if(xor != 0)
			cout<<"Case #"<<t<<": NO\n";
		else
			cout<<"Case #"<<t<<": "<<sum-minc<<endl;
	}
	return 0;
}
