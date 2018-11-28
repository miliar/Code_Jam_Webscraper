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
	int tc, N;
	ll L, H;
	cin>>tc;
	for(int T=1; T<=tc; T++)
	{
		cin>>N>>L>>H;
		vector<ll> a(N);
		for(int i=0; i<N; i++)
			cin>>a[i];
		
		cout<<"Case #"<<T<<": ";

		bool good = true;
		for(int i=L; i<=H; i++)
		{
			good = true;
			for(int j=0; j<N; j++)
			{
				if( ((a[j]%i)!=0) && ((i%a[j])!=0) )
				{
					good = false;
					break;
				}
			}
			if(good)
			{
				cout<< i <<endl;
				break;
			}
		}
		if(!good)
		{
			cout<<"NO"<<endl;
		}
	}
	return 0;
}
