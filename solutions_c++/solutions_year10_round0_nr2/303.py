#include <cstdio>
#include <iostream>
#include <algorithm>

using namespace std;

unsigned long long gcd(unsigned long long a, unsigned long long b)
{
	if (b == 0)
		return a;
	return gcd(b, a%b);
}

unsigned long long a[1000];

bool dAll(unsigned long long M, unsigned long long*start, unsigned long long*end)
{
	for (unsigned long long* i = start; i < end; i++)
		if (*i % M != 0)
			return false;
	return true;
}

int main()
{
	int T;
	scanf("%d", &T);
	
	for (int t = 1; t <= T; t++)
	{
		int n;
		scanf("%d", &n);
		for (int i = 0; i < n; i++)
		{
			scanf("%llu", &a[i]);
		}
		
		sort(a, a+n);
		unsigned long long* end = unique(a, a+n);
		unsigned long long* start = &a[0];
		
		unsigned long long M(a[1]-a[0]);
		for (unsigned long long* i = start; i < end; i++)
			for (unsigned long long* j = i+1; j < end; j++)
				M = gcd(M, *j - *i);
		
		//printf("%d %lld\t", n, a[0]);
		if (dAll(M, start, end))
			cout << "Case #" << t << ": " << 0 << endl;
		else
			cout << "Case #" << t << ": " << M-(a[0]%M) << endl;
	}
	
	return 0;
}
