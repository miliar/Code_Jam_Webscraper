#include <string>
#include <iostream>
#include <algorithm>
#include <cstdio>
using namespace std;

int a[1005];

void solve(int cID)
{
	int N;
	cin >> N;
	int s = 0, sum = 0;
	int m = 100000000;
	for (int i = 0; i < N; i ++) {
		cin >> a[i];
		s ^= a[i];
		sum += a[i];
		m = min(a[i], m);
	}

	printf("Case #%d: ", cID);
	if (s != 0) {
		printf("NO\n");
		return;
	}
	else printf("%d\n", sum - m);
}

int main()
{
	int T;
	cin >> T;
	for (int i = 1; i <= T; i ++)
		solve(i);
}
