#include <iostream>
#include <algorithm>
#include <map>
#include <string>
#include <vector>
using namespace std;


int main()
{
	freopen("B-large.in" , "r" , stdin);
	freopen("output.txt" , "w" , stdout);

	int t;
	cin>>t;
	for (int caseid = 1; caseid <= t ; caseid++)
	{
		cout<<"Case #"<<caseid<<": ";

		long long n,k,b,t;
		cin>>n>>k>>b>>t;
		vector<long long> xs(n);

		for (int i = 0; i < n ; i++)
		{
			cin>>xs[i];
		}

		vector<long long> vel(n);
		for (long long i = 0; i < n ; i++)
		{
			cin>>vel[i];
		}

		vector< pair<long long,long long> > p;
		for (long long i = 0; i < n ; i++)
		{
			p.push_back( make_pair(xs[i] , vel[i]*t ) );
		}


		sort(p.begin() , p.end());

		
		vector<int> yesno;
		long long k1 = 0;
		for (long long i = 0; i < p.size() ; i++)
		{
			if(p[i].second+p[i].first >= b)
			{
				k1 += 1;
				yesno.push_back(1);
			}
			else
				yesno.push_back(0);
		}

		if(k1 < k)
		{
			cout<<"IMPOSSIBLE\n";
			continue;
		}

		long long sw = 0;
		long long ans = 0;

		k1 = 0;
		for(long long i = p.size()-1 ; i >= 0 ; i--)
		{
			if(yesno[i] == 1)
			{
				k1 += 1;
				ans += sw;
			}
			else
				sw += 1;
			if(k1 == k)
				break;
		}

		if(k1 < k)
			cout<<"IMPOSSIBLE\n";
		else
			cout<<ans<<endl;
	}
	return 0;
}