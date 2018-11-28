#include <iostream>
#include <algorithm>
#include <cassert>

using namespace std;

int T;
int N;
char buf[64];
int a[64];
int b[64];

bool canComplete(int i)
{
	memcpy(b + i, a + i, (N - i) * sizeof(a[0]));
	sort(b + i, b + N);
	for (int j = i; j < N; ++j)
		if (b[j] > j)
			return false;
	return true;
}

int minSwaps()
{
	int res = 0;
	for (int i = 0; i < N; ++i) {
		int j;
		for (j = i; j < N; ++j) if (a[j] <= i) {
			bool ok;
			swap(a[i], a[j]);
			ok = canComplete(i + 1);
			swap(a[i], a[j]);
			if (ok)
				break;
		}
		assert(j < N);
		for (int k = j; k > i; --k)
			swap(a[k], a[k - 1]);
		res += j - i;
	}
	return res;
}

int main()
{
	scanf("%d", &T);
	for (int ncase = 1; ncase <= T; ++ncase) {
		scanf("%d", &N);
		for (int i = 0; i < N; ++i) {
			scanf("%s", buf);
			int j;
			for (j = N - 1; j >= 0; --j)
				if (buf[j] == '1')
					break;
			a[i] = j;
		}
		printf("Case #%d: %d\n", ncase, minSwaps());
	}

	return 0;
}
