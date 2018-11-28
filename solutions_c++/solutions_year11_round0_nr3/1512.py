#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <climits>
#define maxN 10000

using namespace std;

int N, a[maxN];

int main()
{
	int T, z;
	cin >> T;
	for (int z = 1; z <= T; z++)
	{
		int N, t = 0, S = 0, m = INT_MAX;
		cin >> N;
		for (int i = 0; i < N; i++)
		{
			cin >> a[i];
			t ^= a[i];
			S += a[i];
			m = min(a[i], m);
		}
		printf("Case #%d: ", z);
		if (t)
			puts("NO");
		else
			printf("%d\n", S - m);
	}
	return 0;
}
