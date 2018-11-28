#include <iostream>
#include <stdio.h>
#include <vector>
using namespace std;

int main()
{
	int T,ca;
	int i,j,k;
	cin >> T;
	for(ca=1; ca<=T; ca++)
	{
		int N;
		cin >> N;
		long long sum = 0;
		long long x = 0;
		vector<long long> v;
		for(i=0; i<N; i++)
		{
			long long d;
			cin >> d;
			v.push_back(d);
			sum += d;
			x ^= d;
		}
		long long r = -1;
		for(i=0; i<N; i++)
			if ((x ^ v[i]) == v[i])
			{
				long long a = v[i]; long long b = sum-v[i];
				r = max(r, max(a,b));
			}
		printf("Case #%d: ", ca);
		if (r == -1)
			printf("NO\n");
		else
			printf("%lld\n", r);
	}
}
