#include <stdio.h>
#include <map>
#include <algorithm>
#include <vector>
#include <string>
#include <memory.h>


using namespace std;

long long gcd(long long a, long long b)
{
	if (b == 0)
		return a;
	if (b > a)
		return gcd(b, a);
	return gcd(b, a % b);
}

int main()
{
	int T;
	
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &T);
	for (int t = 0; t < T; t++)
	{
		long long N, PD, PG;
		scanf("%lld%lld%lld", &N, &PD, &PG);
		bool res = false;
		if (PG == 100 && PD == 100)
			res =  true;
		else if (PG == 0 && PD == 0)
			res = true;
		else if (PG != 0 && PG != 100)
		{
			long long g = gcd(PD, 100);
			res = 100 / g <= N;
		}
		printf("Case #%d: %s\n", t+1, res ? "Possible" : "Broken");

	}
	return 0;
}