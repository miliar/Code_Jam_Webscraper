#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;

long long gcd(long long a, long long b)
{
	return b == 0? a: gcd(b, a % b);
}

int main()
{
	int T, z;
	cin >> T;
	for (int z = 1; z <= T; z++)
	{
		long long N, pd, pg;
 		cin >> N >> pd >> pg;
		long long d = 100 / gcd(pd, 100LL);
		printf("Case #%d: ", z);
		if (d > N || (pg == 0 && pd != 0) || (pg == 100 && pd != 100))
			puts("Broken");
		else
			puts("Possible");
	}
	return 0;
}
