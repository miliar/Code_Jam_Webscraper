#include <cstdio>
#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <ctype.h>
#include <string.h>
using namespace std;

const int NMAX = 30;

bool used[NMAX];
int ind[NMAX];

int main()
{
	int n, t, k;
	freopen("test.in", "a+", stdin);
	freopen("test.out", "w", stdout);
	memset(used, 0, sizeof(0));
	scanf("%d", &t);
	
	ind[0] = 1;
	for (int i = 1; i < NMAX; ++i)
	{
		ind[i] = ind[i-1]*2 + 1;
	}

	for (int l = 0; l < t; ++l)
	{
		printf("Case #%d: ", l+1);
		scanf("%d%d", &n, &k);

		if (k < ind[n-1])
			printf("OFF\n");
		else
		{
			if ((k - ind[n - 1]) % (ind[n-1] + 1) == 0)
				printf("ON\n");
			else
				printf("OFF\n");
		}
	}
	return 0;
}