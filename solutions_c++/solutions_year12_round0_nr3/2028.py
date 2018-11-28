#include <cstdio>
#include <cstdlib>
#include <cstring>

//#define TC_DEBUG

int shiftMask[] = { 1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000 };

int main(int argc, char* argv[])
{
	int T;

	scanf("%d", &T);

	for (int tc = 1; tc <= T; ++tc)
	{
		int A, B;
		scanf("%d %d", &A, &B);

		int digits = 0;
		if (A < 10)
			digits = 1;
		else if (A < 100)
			digits = 2;
		else if (A < 1000)
			digits = 3;
		else if (A < 10000)
			digits = 4;
		else if (A < 100000)
			digits = 5;
		else if (A < 1000000)
			digits = 6;
		else if (A < 10000000)
			digits = 7;
		else if (A < 100000000)
			digits = 8;
		else if (A < 1000000000)
			digits = 9;

		int countDiff = 0;
		for (int n = A; n <= B; ++n)
		{
			int m;
			int m1=0, m2=0, m3=0, m4=0, m5=0;

			// Shift 1
			if (digits >= 2)
			{
				m = (n / 10) + (n % 10) * shiftMask[digits - 1]; 
				if (m > n && m <= B)
				{
					countDiff++;
					m1=m;
#ifdef TC_DEBUG
					printf("%d %d\n", n, m);
#endif
				}
			}

			// Shift 2
			if (digits >= 3)
			{
				m = (n / 100) + (n % 100) * shiftMask[digits - 2]; 
				if (m > n && m <= B && m != m1)
				{
					countDiff++;
					m2 = m;
#ifdef TC_DEBUG
					printf("%d %d\n", n, m);
#endif
				}
			}

			// Shift 3
			if (digits >= 4)
			{
				m = (n / 1000) + (n % 1000) * shiftMask[digits - 3]; 
				if (m > n && m <= B && m != m1 && m != m2)
				{
					countDiff++;
					m3 = m;
#ifdef TC_DEBUG
					printf("%d %d\n", n, m);
#endif
				}
			}

			// Shift 4
			if (digits >= 5)
			{
				m = (n / 10000) + (n % 10000) * shiftMask[digits - 4]; 
				if (m > n && m <= B && m != m1 && m != m2 && m != m3)
				{
					countDiff++;
					m4 = m;
#ifdef TC_DEBUG
					printf("%d %d\n", n, m);
#endif
				}
			}

			// Shift 5
			if (digits >= 6)
			{
				m = (n / 100000) + (n % 100000) * shiftMask[digits - 5]; 
				if (m > n && m <= B && m != m1 && m != m2 && m != m3 && m != m4)
				{
					countDiff++;
					m5 = m;
#ifdef TC_DEBUG
					printf("%d %d\n", n, m);
#endif
				}
			}

			// Shift 6
			if (digits >= 7)
			{
				m = (n / 1000000) + (n % 1000000) * shiftMask[digits - 6]; 
				if (m > n && m <= B && m != m1 && m != m2 && m != m3 && m != m4 && m != m5)
				{
					countDiff++;
#ifdef TC_DEBUG
					printf("%d %d\n", n, m);
#endif
				}
			}
		}

		printf("Case #%d: %d\n", tc, countDiff);
	}

	return 0;
}
