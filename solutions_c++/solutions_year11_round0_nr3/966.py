#include <cstdio>
#include <cmath>
#include <algorithm>

const int N = 200;
int n;
int arr[N];

void Scan()
{
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
		scanf("%d", &arr[i]);
}

void Solve()
{
	int res = 0;
	for (int i = 0; i < n; i++)
	{
		res = res ^ arr[i];
	}
	if (res != 0)
	{
		printf("NO\n");
		return;
	}
	std::sort(arr, arr+n);
	int sum = 0;
	for (int i = 1; i < n; i++)
		sum += arr[i];
	printf("%d\n", sum);	
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		Scan();
		printf("Case #%d: ", i+1);
		Solve();
	}
	return 0;
}