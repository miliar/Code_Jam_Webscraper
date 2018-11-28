#include <iostream>
using namespace std;
const long long SIZE = 1024;

long long amount[SIZE];

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small.out","w",stdout);
	long long cases,cas = 1,i,k,n,r;
	cin>>cases;
	while(cases --)
	{
		cin>>r>>k>>n;
		for (i = 0; i < n; i++)
			cin>>amount[i];
		
		long long p = 0,sum = 0;
		long long money = 0;
		for (i = 1; i <= r; i++)
		{
			long long flag = p;
			while(sum +amount[p] <= k)
			{
				sum += amount[p++];
				p %= n;
				if (p == flag) break;
			}
			money += sum;
			sum = 0;
			if (p == 0)
			{
				break;
			}
		}
		long long ans = r/i*money;
		r %= i; p = 0; sum = 0; money = 0;
		for (i = 1; i <= r; i++)
		{
			long long flag = p;
			while(sum+amount[p] <= k)
			{
				sum += amount[p++];
				p %= n;
				if (flag == p) break;
			}
			money += sum;
			sum = 0;
		}
		ans += money;
		cout<<"Case #"<<cas++<<": "<<ans<<endl;
	}
	return 0;
}