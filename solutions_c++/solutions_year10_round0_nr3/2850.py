#include <iostream>
#include <map>

using namespace std;

long long t;
long long r,k,n;
long long group[1001];
long long towhere[1001],howmany[1001];

int main()
{
	cin >> t;
	for (long long i=1;i<=t;i++)
	{
		cin >> r >> k >> n;
		for (long long j=1;j<=n;j++)
			cin >> group[j];
		for (long long i=1;i<=n;i++)
		{
			long long thismany = 0,tonow =i,startnow = tonow;
			do
			{
				thismany+=group[tonow];
				tonow++;
				if (thismany > k)
				{
					thismany-=group[--tonow];
					break;
				}
				if (tonow > n)
				{
					tonow = 1;
				}
				if (tonow == startnow) break;
			} while (true);
			towhere[i] = tonow;
			howmany[i] = thismany;
		}
		long long money = 0;
		long long now = 1;
		for (long long i=1;i<=r;i++)
		{
			money+=howmany[now];
			now=towhere[now];
		}
		cout << "Case #" << i << ": " << money << endl;
	}
}
