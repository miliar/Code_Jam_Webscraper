#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

__int64 N, Pd, Pg;

__int64 gcd(__int64 a, __int64 b)
{
	if(b == 0)  return a;
	return gcd(b, a % b);
}

bool go()
{
	__int64 g = gcd(Pd, 100);
	__int64 tmp = 100 / g;

	if(tmp <= N)
	{
		if(Pd != 100 && Pg == 100)  return false;
		if(Pd && Pg == 0)  return false;

		return true;
	}
	else  return false;
}

int main()
{
	__int64 T, c = 0;
	scanf("%I64d", &T);
	while(T--)
	{
		
		scanf("%I64d%I64d%I64d",&N, &Pd, &Pg);
		printf("Case #%I64d: %s\n", ++c, go() ? "Possible" : "Broken");
	}
}