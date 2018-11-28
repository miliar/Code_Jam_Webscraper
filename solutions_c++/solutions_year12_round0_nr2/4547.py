#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n, s, p;

int arr[300];

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("a.out", "w", stdout);

	int t;
	scanf("%d\n", &t);

	for(int tt = 0; tt < t; tt++)
	{
		scanf("%d%d%d", &n, &s, &p);
		for(int i = 0; i < n; i++)
			scanf("%d", &arr[i]);
		sort(arr, arr + n);
		int ans = 0;
		for(int i = n-1; i >= 0; i--)
		{
			int cnt = arr[i] / 3;
			if(cnt * 3 != arr[i])
				cnt++;
			if(cnt >= p)
				ans++;
			else if(s > 0 && (arr[i] % 3 != 1) && cnt+1 >= p && arr[i] > 0)
			{
				s--;
				ans++;
			}
		}
		printf("Case #%d: %d\n", tt+1, ans);
	}


	return 0;
}