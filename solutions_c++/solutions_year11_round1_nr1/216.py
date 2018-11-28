#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int PD, PG;
long long N;

int main ()
{
//freopen ("in.txt", "r", stdin);
//freopen ("ou.txt", "w", stdout);


	int T, flag;
	scanf ("%d", &T);

	for (int i = 1; i <= T; i++) {
		scanf ("%lld%d%d", &N, &PD, &PG);

		flag = 1;

		if (PG == 0 && PD != 0) flag = 0;
		if (PG == 100 && PD != 100) flag = 0;

		if (flag == 0) {
			printf ("Case #%d: Broken\n", i);
			continue;
		}
		
		int x = 100;
		if (PD % 2 == 0) PD /= 2, x /= 2;
		if (PD % 2 == 0) PD /= 2, x /= 2;
		if (PD % 5 == 0) PD /= 5, x /= 5;
		if (PD % 5 == 0) PD /= 5, x /= 5;

		printf ("Case #%d: %s\n", i, N / x != 0 ? "Possible" : "Broken");
	}
	
	return 0;
}


