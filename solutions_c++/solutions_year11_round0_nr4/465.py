#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

void test(int x)
{
	int a[x], cnt[x + 1];
	for (int i = 0; i < x; i ++) a[i] = i;
	for (int i = 0; i <= x; i ++) cnt[i] = 0;
	do {
		int s = 0;
		for (int i = 0; i < x; i ++)
			s += (a[i] != i);
		cnt[s] ++;
	} while (next_permutation(a, a + x));
	for (int i = 0; i <= x; i ++) cout << cnt[i] << endl;
}

void solve(int cID)
{
	int N, x;
	cin >> N;
	double ans = 0;
	for (int i = 1; i <= N; i ++) {
		cin >> x;
		ans += (x != i);
	}
	printf("Case #%d: %lf\n", cID, ans);

}

int main()
{
//	int N;
//	cin >> N;
//	test(N);
	int T;
	cin >> T;
	for (int i = 1; i <= T; i ++)
		solve(i);
}
