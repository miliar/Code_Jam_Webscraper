#include <iostream>

using namespace std;

#define MAX 1024

int a[MAX];
bool flag[MAX];

int main()
{
	//freopen("D-large.in", "r", stdin);
	//freopen("D.out", "w", stdout);
	int t;
	cin >> t;
	for (int ti = 1; ti <= t; ++ti)
	{
		int n;
		cin >> n;
		for (int i = 1; i <= n; ++i)
		{
			scanf("%d", &a[i]);
		}
		double ans = 0.0;
		int cnt = 0;
		for (int i = 1; i <= n; ++i)
		{
			if (a[i] != i) ++cnt;
		}
		ans = cnt;
		printf("Case #%d: %.6lf\n", ti, ans);
	}
	return 0;
}
