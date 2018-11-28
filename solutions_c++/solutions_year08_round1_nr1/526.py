#include <cstdio>
#include <algorithm>

using namespace std;

int brt;
int n;
long long mas1[804];
long long mas2[804];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("task1.out", "w", stdout);

	scanf("%d", &brt);

	for(int gi=1; gi<=brt;gi++)
	{
		scanf("%d", &n);
		for(int i=0;i<n;i++)
			scanf("%lld", &mas1[i]);

		for(int i=0;i<n;i++)
			scanf("%lld", &mas2[i]);

		sort(mas1, mas1+n);
		sort(mas2, mas2+n);

		long long ans = 0;
		for(int i=0;i<n;i++)
			ans += mas1[i] * mas2[n-i-1];

		printf("Case #%d: %lld\n", gi, ans);
	}

	return 0;
}
