//c.cpp
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <cstdlib>
#include <algorithm>

using namespace std;

typedef long long ll;

int main()
{
	ll tc, N, res, t, C, L;
	cin>>tc;
	for(int T=1; T<=tc; T++)
	{
		res = 0;
		cin >> L >> t >> N >> C;
		vector<int> a(N);
		for(int i=0; i<C; i++)
		{	
			cin>>a[i];
			res += a[i]*2;
		}

		for(int i=C; i<N; i++)
		{	
			a[i] = a[i-C];
			res += a[i]*2;
		}
		cout<<"Case #"<<T<<": ";
		
		if(L==0)
		{
			cout<<res<<endl;
			continue;
		}

		if(L==1)
		{
			ll best = 0;
			ll rem = t;
			for(int i=0; i<N; i++)
			{
				if(rem >= 2*a[i])
				{
					rem -= 2*a[i];
					continue;
				}

				ll cur = 0;
				if(rem <= 0 )
					cur = a[i];
				else
					cur = a[i] - rem/2;

				if(best < cur)
					best = cur;
				rem = 0;
			}

			res -= best;
			cout<<res<<endl;
			continue;
		}


		if(L==2)
		{
			int best_i=0;
			ll best = 0;
			ll rem = t;
			for(int i=0; i<N; i++)
			{
				if(rem >= 2*a[i])
				{
					rem -= 2*a[i];
					continue;
				}

				ll cur = 0;
				if(rem <= 0 )
					cur = a[i];
				else
					cur = a[i] - rem/2;

				if(best < cur)
				{
					best = cur;
					best_i = i;
				}
				rem = 0;
			}

			res -= best;

			best = 0;
			rem = t;
			for(int i=0; i<N; i++)
			{
				if(rem >= 2*a[i])
				{
					rem -= 2*a[i];
					continue;
				}
				if(i==best_i)
				{
					rem = 0;
					continue;
				}

				ll cur = 0;
				if(rem <= 0 )
					cur = a[i];
				else
					cur = a[i] - rem/2;

				if(best < cur)
					best = cur;
				rem = 0;
			}

			res -= best;

			cout<<res<<endl;
			continue;
		}

	}

	return 0;
}
