#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>

const int N = 10001;
int n;
int arr[N];

void Scan()
{
	scanf("%d",&n);
	for(int i = 1; i <= n; i++)
		scanf("%d", &arr[i]);
}

void Solve()
{
	int cnt = 0;
	for (int i = 1; i <= n; i++)
	{
		if (arr[i] != i) cnt++;
	}
	printf("%d.000000\n", cnt);
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