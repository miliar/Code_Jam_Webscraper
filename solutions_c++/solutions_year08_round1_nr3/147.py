#include <stdio.h>
#include <math.h>

int ans[] = {5, 27, 143, 751, 935, 607, 903, 991, 335, 47, 943, 471, 55, 447, 463, 991, \
95, 607, 263, 151, 855, 527, 743, 351, 135, 407, 903, 791, 135, 647};

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t; 
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i)
	{
		int n;
		scanf("%d", &n);
		n--;
		printf("Case #%d: %d%d%d\n", i, ans[n] / 100, ans[n] / 10 % 10, ans[n] % 10);
	}
}