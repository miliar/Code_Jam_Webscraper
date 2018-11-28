#include <algorithm>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <sstream>
#include <stack>
#include <vector>

#include <limits.h>
#include <math.h>
#include <stdio.h>

using namespace std;

#define foreach(k, b, N) for (int k = b; k <= N; k++)
#define foreach_r(k, b, N) for (int k = b; k >= N; k--)

int primes[200];
int factors[100];

int
main()
{
	int cases; 
	int result = 0;
	int k = 0;
	int value;

	cin >> cases;

#if 0	
	memset(primes, 1, sizeof(primes));

	primes[1] = 0;
	foreach(i, 2, 100) {
		if (primes[i] == 0)
			continue;

		for (int j = i + i; j <= 100; j += i)
			primes[j] = 0;
	}	
#endif

	foreach(i, 1, cases) {
		long long N, PD, PG;
		
		cin >> N >> PD >> PG;

		if (PD != 100 && PG == 100)
			goto nope;
		
		if (PD != 0 && PG == 0)
			goto nope;

#if 0		
		memset(factors, 0, sizeof(factors));
		
		value = PD;
		foreach(j, 2, 100) {
			while (value % j == 0) {
				factors[k++] = j;
				value = value / j;

				printf("factor %d\n", j);
			}

			if (value == 1)
				break;
		}
#endif
		for (long long j = 1; j <= N; j++) {
			for (long long k = 0; k <= j; k++) {
				if ((((k * 100) % j) == 0) && (k * 100 == PD * j)) {
					goto done;
				}
			}
		}
nope:		
		printf("Case #%d: Broken\n", i);
		continue;
done:		
		printf("Case #%d: Possible\n", i);
	}

	return 0;
}
