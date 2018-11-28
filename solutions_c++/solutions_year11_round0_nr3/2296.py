#define _CRT_SUCURE_NO_DEPRECATE
#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <algorithm>

using namespace std;

int kol_test;
int n;
int a[10000];

int MyAdd(int a, int b)
{
	int res = 0;
	int st2 = 1;
	while (a > 0 || b > 0)
	{
		int res1 = (a & 1) ^ (b & 1);
		res += res1 * st2;
		st2 <<= 1;
		a >>= 1;
		b >>= 1;
	}
	return res;
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	scanf("%d", &kol_test);
	for (int nom_test = 0; nom_test < kol_test; ++nom_test)
	{
		scanf("%d", &n);
		for (int i = 0; i < n; ++i)
		{
			scanf("%d", &a[i]);
		}
		sort(a, a + n);
		int res = 0;
		int sum = 0;
		for (int i = 0; i < n; ++i)
		{
			res = MyAdd(res, a[i]);
			sum += a[i];
		}
		printf("Case #%d: ", nom_test + 1);
		if (res == 0)
		{
			printf("%d", sum - a[0]);
		}
		else
		{
			printf("NO");
		}
		printf("\n");
	}

	return 0;
}