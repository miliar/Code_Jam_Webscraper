#include <iostream>
#include <algorithm>

using namespace std;

int num[1010], dif[1010];
int n;

int GCD(int a, int b)
{
	while (a > b ? a = a % b : b = b % a);
	return a + b;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	int caseID = 1;
	while (caseID <= t)
	{
		printf("Case #%d: ", caseID++);
		scanf("%d", &n);
		int i;
		for (i = 0; i < n; i++)
			scanf("%d", &num[i]);
		sort(num, num + n);
		for (i = 0; i < n - 1; i++)
			dif[i] = num[i + 1] - num[i];
		int maxF = dif[0];
		if (maxF == 0) maxF = dif[1];
		for (i = 1; i < n - 1; i++)
			if (dif[i] != 0) maxF = GCD(maxF, dif[i]);
		__int64 inc = (__int64) (num[0] / maxF + 1) * maxF - num[0];
		if (num[0] % maxF == 0) inc--;
		printf("%I64d\n", inc);
	}
	return 0;
}