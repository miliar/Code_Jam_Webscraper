#include <iostream>
using namespace std;

int N, P, K, L;
int fre[1000];
int comp(const void* a, const void* b)
{
	return *(int *)b - *(int *) a;
}
int main()
{
	cin >> N;
	for (int i = 1; i <= N; ++i) {
		cout << "Case #" << i << ": ";
		cin >> P >> K >> L;
		for (int j = 0; j < L; ++j)
			cin >> fre[j];
		if (P * K < L) {
			cout << "Impossible\n";
			continue;
		}
		qsort(fre, L, sizeof(int), comp);
		int times = 1, ans = 0;
		for (int j = 0; j < L; j += K, ++times) {
			for (int k = 0; k < K && j + k < L; ++k)
				ans += fre[j + k] * times;
		}
		cout << ans << endl;
	}
}