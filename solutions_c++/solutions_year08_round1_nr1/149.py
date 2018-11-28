#include <stdio.h>
#include <algorithm>

typedef __int64 int64;

int a1[1000], a2[1000];

void solve(int test_case)
{
	int n;
	int64 ans = 0;
	scanf("%d", &n);
	for(int i = 0; i < n; i++)
		scanf("%d", &a1[i]);
	for(int i = 0; i < n; i++)
		scanf("%d", &a2[i]);
	std::sort(a1, a1 + n);
	std::sort(a2, a2 + n);
	for(int i = 0; i < n; i++)
		ans += a1[i] * a2[n - i - 1];

	


	printf("Case #%d: %I64d\n", test_case, ans);

}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n;
	scanf("%d", &n);
	for(int i = 1; i <= n; i++)
		solve(i);

	return 0;
}
