#include <cstdio>
#include <vector>
#include <iostream>
using namespace std;

int pow10[] = {1, 10, 100, 1000, 10000, 100000, 1000000};
int log10(int x)
{
	for (int i = 6; i >= 0; i--) {
		if (x / pow10[i]) return i;
	}
}

long long ans(int a, int b)
{
	long long cnt = 0;
	for (int n = a; n <= b; n++) {
		int ln = log10(n);
		vector<int> cd;
		for (int i = 1; i <= ln; i++) cd.push_back((n % pow10[i]) * pow10[ln - i + 1] + (n / pow10[i]));
		for (int i = 0; i < ln - 1; i++) {
			if (cd[i] == 0) continue;
			for (int j = i + 1; j < ln; j++) {
				if (cd[i] == cd[j]) cd[j] = 0;
			}
		}

		for (int i = 1; i <= ln; i++) {
			int nn = cd[i - 1];
			if (nn <= b && n < nn && log10(nn) == ln) cnt++;
		}
	}
	return cnt;
}

int main()
{
	int ncases;
	scanf("%d", &ncases);
	for (int cases = 1; cases <= ncases; cases++) {
		int a, b;
		scanf("%d %d", &a, &b);
		printf("Case #%d: %d\n", cases, ans(a, b));
	}

	return 0;
}