#include<iostream>
#include<algorithm>

#define N 1000

using namespace std;

int a[N], b[N];

int main()
{
	//freopen("a.txt", "r", stdin);
	//freopen("b.txt", "w", stdout);
	int t, n;
	scanf("%d", &t);
	int caseID = 1;
	while (t--)
	{
		printf("Case #%d: ", caseID++);
		scanf("%d", &n);
		int i;
		for (i = 0; i < n; i++)
			scanf("%d", &a[i]);
		for (i = 0; i < n; i++)
			scanf("%d", &b[i]);
		double sum = 0;
		sort(a, a + n);
		sort(b, b + n);
		for (i = 0; i < n; i++)
			sum += a[i] * b[n - 1 - i];
		printf("%.0lf\n", sum);
	}
	return 0;
}