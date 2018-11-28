#include <cstdio>
#include <vector>
#include <algorithm>
#include <functional>

using namespace std;
int main()
{
	int t;
	scanf("%d",&t);
	for(int z=1;z<=t;z++)
	{
		long long n,x;
		vector<long long> a,b;

		scanf("%lld",&n);
		for(int i=0;i<n;i++)
		{
			scanf("%lld",&x);
			a.push_back(x);
		}


		for(int i=0;i<n;i++)
		{
			scanf("%lld",&x);
			b.push_back(x);
		}

		sort(a.begin(),a.end(),less<long long>());
		sort(b.begin(),b.end(),greater<long long>());

		long long res = 0;
		for(int i=0;i<n;i++)
			res += a[i]*b[i];

		printf("Case #%d: %lld\n",z,res);
	}
	return 0;
}
