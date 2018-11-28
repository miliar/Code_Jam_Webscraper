#include <iostream>
using namespace std;

int findmax( long long int * f, int l)
{
	int m = f[0];
	int ind = 0;
	for(int i = 1; i < l; i++)
		if(m < f[i])
		{
			ind = i;
			m = f[i];
		}
	f[ind] = 0;
	return m;
}

int main()
{
	int n,max;
	long long int p,k,l,freq[1100]={0};

	cin>>n;

	for(int count = 1; count <= n; count++)
	{
		cin>>p>>k>>l;
		for(int i = 0; i < l;i++)
			cin>>freq[i];
		long long int ans = 0;
		int pos = 1;
		int nav = 1;

		for(int i = 0; i < l; i++)
		{
			if(nav > k)
			{
				pos++;
				nav = 1;
			}

			max = findmax(freq,l);
			ans += (max*pos);
			nav++;
		}
		printf("Case #%d: %lld\n", count, ans);
		//
		//cout<<"Case #"<<count<<": "<<ans<<'\n';
	}
}
