#include<iostream>
#include<cstring>
#include<stdio.h>
#include<algorithm>
#include<stdlib.h>

using namespace std;

int main(void)
{
	int cas, goal, tmp, k, n;

	freopen("D:\\A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	scanf("%d", &cas);

	for (int t = 1; t <= cas; t++)
	{
		scanf("%d%d", &n, &k);

		printf("Case #%d: ", t);

		tmp = 1;
		
		tmp = tmp<< n;
		if (k % tmp == tmp-1)
			printf("ON\n");
		else
			printf("OFF\n");
	}
	return 0;
}