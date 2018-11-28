#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>

using namespace std;

const int MAX = 2000;

int main()
{
	int n, t, i, j, a[MAX], b[MAX], s;
	freopen("d.in", "r", stdin);
	freopen("d.out", "w", stdout);
	scanf("%d", &t);
	for(i = 0; i < t; i++)
	{
		s = 0;
		scanf("%d", &n);
		for(j = 0; j < n; j++)
		{
			scanf("%d", a + j);
			if(a[j] == j + 1) s++;
			b[j] = a[j];
		}
		sort(b, b + n);
		printf("Case #%d: %.6lf\n", i + 1, 1.0 * n - s);
	}
    return 0;
}
