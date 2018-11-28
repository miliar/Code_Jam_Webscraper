#include <stdio.h>
#include <stdlib.h>

int gcd(int a, int b)
{
	if(a == 0)
		return b;
	while(b != 0)
		if(a > b)
			a -= b;
		else
			b -= a;
	return a;
}

void main()
{
	FILE* in = ::fopen("b.in", "r");
	FILE* out = ::fopen("b.out", "w");

	int c;
	::fscanf(in, "%d", &c);

	for(int i = 0; i < c; ++i)
	{
		int n;
		::fscanf(in, "%d", &n);

		if(n == 2)
		{
			int a1;
			int a2;

			::fscanf(in, "%d%d", &a1, &a2);
			int t = a1 >= a2? a1 - a2: a2 - a1;

			::fprintf(out, "Case #%d: %d\n", i + 1, (t - (a1 % t)) % t);
		}
		else if (n == 3)
		{
			int a1;
			int a2;
			int a3;

			::fscanf(in, "%d%d%d", &a1, &a2, &a3);
			int t = gcd(a1 >= a2? a1 - a2: a2 - a1, a1 >= a3? a1 - a3: a3 - a1);
			::fprintf(out, "Case #%d: %d\n", i + 1, (t - (a1 % t)) % t);
		}
	}

	::fclose(out);
	::fclose(in);
}