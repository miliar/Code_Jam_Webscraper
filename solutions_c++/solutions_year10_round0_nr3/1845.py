#include <stdio.h>
#include <string.h>

int gn[1000]; //nubmer of every group

int nn[1000]; //the next starting position every time when starting at group i(index)
__int64 tn[1000];// total number every time the train would hold when starting at group i(index)

void calcnntn(int n, __int64 k)
{
	for (int i=0; i<n; i++)
	{
		int j = i;
		__int64 t = gn[j];

		for (int m = 1; m < n; m++)
		{
			j++;
			if ( j==n ) j = 0;

			if ( (t + gn[j]) > k ) break;

			t += gn[j];
		}
		
		nn[i] = j;
		tn[i] = t;

	}
}

int main(int argc, char* argv[])
{
	FILE* is = freopen(argv[1], "r", stdin);
	FILE* os = freopen(argv[2], "w", stdout);

	int t;

	scanf("%d", &t);

	__int64 k, r;
	int n;

	for (int i = 1; i<=t; i++)
	{
		scanf("%I64d%I64d%d", &r, &k, &n);

		for (int j=0; j<n; j++)
			scanf("%d", &gn[j]);
		
		calcnntn(n, k);

		int inipos = 0;
		__int64 money = 0;

		for (__int64 m = 1; m <= r; m++)
		{
			money += tn[inipos];
			inipos = nn[inipos];
		}

		printf("Case #%d: %I64d\n", i, money);
	}

	fclose(is);
	fclose(os);
	return 0;
}