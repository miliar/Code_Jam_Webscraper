#include <stdio.h>
#include <algorithm>
#include <functional>
using namespace std;

#define N 1000000

int L, t, n, C, a[N], b[N];

int main()
{
	int T, TT;
	scanf("%d", &TT);
	for (T = 1; T <= TT; ++T)
	{
		scanf("%d%d%d%d", &L, &t, &n, &C);
		for (int i = 0; i < C; ++i) scanf("%d", a + i);
		for (int i = 0; i < n; ++i) b[i] = a[i%C];
		int sum = 0;
		int k = 0;
		while (sum<t && k<n) sum += 2*b[k++];
		if (sum > t) b[--k] = (sum - t)/2, sum = t;
		sort(b+k, b+n, greater<int>());
		while (k<n && L--) sum += b[k++];
		while (k < n) sum += 2*b[k++];
		printf("Case #%d: %d\n", T, sum);
	}
	return 0;
}
