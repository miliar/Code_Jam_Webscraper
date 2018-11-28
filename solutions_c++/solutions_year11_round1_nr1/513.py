#include <cstdio>
#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>
#include <utility>
#include <cmath>
#include <string>
using namespace std;

int gcd(int a, int b)
{
	int r;
	while ((r = a % b) != 0)
	{
		a = b;
		b = r;
	}
	return b;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	scanf("%d", &T);

	for (int t=1; t<=T; t++)
	{
		//TODO: implement your algorithm here
		long long N;
		int PD, PG;
		cin >> N >> PD >> PG;

		int gcd1 = gcd(PD, 100);
		int minD = 100 / gcd1;
		if (minD > N)
		{
			printf("Case #%d: Broken\n", t);
			continue;
		}

		if (PD != 100 && PG == 100)
		{
			printf("Case #%d: Broken\n", t);
			continue;
		}

		if (PD > 0 && PG == 0)
		{
			printf("Case #%d: Broken\n", t);
			continue;
		}

		printf("Case #%d: Possible\n", t);
	}
}