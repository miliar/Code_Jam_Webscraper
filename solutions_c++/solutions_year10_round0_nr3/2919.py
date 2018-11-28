// park.cpp : Defines the entry point for the console application.
//

#include <iostream>
using namespace std;

long long mas[1005];
pair<long long, long long> m[1005];

void out(long long i, long long x)
{
	cout<<"Case #"<<i<<": "<<x<<endl;
}


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	cin>>t;
	for (int tt=1; tt<=t; tt++)
	{
		long long r,k,n;
		cin>>r>>k>>n;
		for (int i=0; i<n; i++)
			cin>>mas[i];

		for (int i=0; i<n; i++)
		{
			int j = (i+1)%n;
			int s = mas[i];
			int u = 1;
			int o = i;
			while (s + mas[j] <= k)
			{
				if (j == o)
					break;
				u++;
				s+=mas[j];
				j = (j+1)%n;				
			}
			m[i] = make_pair(u, s);			
		}
		
		int rez = 0;
		int j = 0;
		for (int i=1; i<=r; i++)
		{
			rez+=m[j].second;
			j = (m[j].first + j)%n;
		}
		out(tt, rez);
	}
	return 0;
}

