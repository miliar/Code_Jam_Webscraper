
	#include <stdio.h>
	#include <stdlib.h>
	#include <memory.h>

	int f[40];
	int main()
	{
		freopen("C-small-attempt0.in", "r", stdin);
		freopen("ca.out", "w", stdout);
		f[1] = 5;	f[2] = 27;	f[3] = 143;	f[4] = 751;	f[5] = 935;
		f[6] = 607;	f[7] = 903;	f[8] = 991;	f[9] = 335;	f[10] = 47;
		f[11] = 943;f[12] = 471;	f[13] = 55;	f[14] = 447;	f[15] = 463;
		f[16] = 991;	f[17] = 95;	f[18] = 607;	f[19] = 263;	f[20] = 151;
		f[21] = 855;	f[22] = 527;	f[23] = 743;	f[24] = 351;	f[25] = 135;
		f[26] = 407;	f[27] = 903;	f[28] = 791;	f[29] = 135;	f[30] = 647;
		int test;
		scanf("%d", &test);
		int n;
		for (int i = 1; i <= test; i ++)
		{
			printf("Case #%d: ", i);
			scanf("%d", &n);
			printf("%d%d%d\n", f[n] / 100, f[n] / 10 % 10, f[n] % 10);
		}
		return 0;
	}
