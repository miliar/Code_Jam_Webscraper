#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

int minfact[1<<20];

int main() 
{
	for (int i = 2; i < 1 << 20; i++) {
		if (minfact[i] != 0)
			continue;
		for (int j = i; j < 1 << 20; j+=i)
			if (minfact[j] == 0)
				minfact[j] = i;
	}
	int test_num;
	scanf("%d", &test_num);
	for (int case_num = 1; case_num <= test_num; case_num++) {
		int D, n;
		int x[100];
		int minp = 2;
		scanf("%d%d", &D, &n);
		int D10 = 1;
		for (int i = 0; i < D; i++)
			D10 *= 10;
		for (int i = 0; i < n; i++) {
			scanf("%d", x+i);
			minp = max(minp, x[i] + 1);
		}
		if (n == 1) {
			printf("Case #%d: I don't know.\n", case_num);
			continue;
		}
		int ans = -1;
		bool multians = false;
		for (int p = minp; p <= D10; p++) {
			if (minfact[p] != p)
				continue;
			for (int a = 0; a < p; a++) {
				int b = (x[1] + p - (long long)x[0] * a%p) % p;
				bool check = true;
				for (int i = 1; i < n; i ++)
					if (((long long)x[i-1] * a + b) % p != x[i])
						check = false;
				if (!check)
					continue;
				int xn = ((long long)x[n-1] * a + b) % p;
				if (ans == -1) {
					ans = xn;
				} else if (ans != xn) {
					multians = true;
					break;
				}
			}
			if (multians)
				break;
		}
		if (multians) {
			printf("Case #%d: I don't know.\n", case_num);
		} else {
			printf("Case #%d: %d\n", case_num, ans);
		}
	}
}
