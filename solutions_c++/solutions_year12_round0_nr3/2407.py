#include <stdio.h>
#include <set>

using namespace std;

int main()
{
	int T;
	scanf("%d", &T);
	int a, b;
	for (int k = 0; k < T; k++)
	{
		set<long long> data;
		scanf("%d %d", &a, &b);

		int base = 1;
		int numdigs = 0;
		while (a / base)
		{
			base *= 10;
			numdigs++;
		}
		base /= 10;

		for (int z = a; z <= b; z++)
		{
			int c = z;
			for (int t = 0; t < numdigs - 1; t++)
			{
				int dig = c / base;
				c %= base;
				c *= 10;
				c += dig;

				if (c < a || c > b) continue;
				if (c == z) continue;
				int z2 = z;
				int c2 = c;

				if (c < z2) swap(c2, z2);

				long long val = z2;
				val *= 100000000;
				val += c2;
				data.insert(val);
			}
		}

		printf("Case #%d: %d\n", k + 1, data.size());
	}
}
