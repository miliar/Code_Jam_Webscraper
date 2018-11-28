#include<iostream>
#include<cstdio>
#include<string>
#include<cstring>
#include<cstdlib>
#include<vector>
#include<algorithm>
using namespace std;

long long T;
long long L,tm,N,C;

long long c[1000010];
bool cmp(long long a,long long b)
{
	return a>b;
}

int main()
{
	freopen("data.in","r",stdin);
	freopen("A-small.out","w",stdout);

	long long t;
	cin>>T;
	for(t=1;t<=T;++t)
	{
		
		cout<<"Case #"<<t<<": ";
		cin>>L>>tm>>N>>C;
		long long i;
		for(i=0;i<C;++i)
			cin>>c[i];
		for(i=C;i<N;++i)
			c[i]=c[i-C];
		long long sum=0;
		vector<long long> rest;
		for(i=0;i<N;++i)
		{
			sum+=c[i];
			if(sum>=tm/2)
			{
				break;
			}
		}
		rest.push_back(sum-tm/2);
		for(i=i+1;i<N;++i)
		{
			sum+=c[i];
			rest.push_back(c[i]);
		}
		sort(rest.begin(),rest.end(),cmp);
		long long ans=0;
		for(i=0;i<L;++i)
			ans+=rest[i];
		cout<<sum*2-ans<<endl;

	}

	return 0;
}
